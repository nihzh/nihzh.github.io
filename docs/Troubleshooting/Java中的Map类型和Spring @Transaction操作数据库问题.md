## Situation
- *SpringBoot*开发网络应用, Entity-Dao-Service-Controller架构
- Entity层使用`@Entity`注解, Dao层使用*JpaRepository*, Service层实现使用`@Transactional`
- 智能库存和营养管理推荐系统, 其中需要**根据用户的原料库推荐菜品**, 并持续多轮, 这就需要每次用户选择菜品后, 模拟用户制作完该菜品后原料库中的剩余, 用剩余原料进行新一轮推荐
- 在代码中使用了`Map<Integer, Inventory>`类型来封装原料库, 然后根据已选的列表`selected`, 循环减去目标食材, 来得到制作菜品后的原料库, 代码如下

```java
// list of available inventory, to be edit  
Map<Integer, Inventory> invMap = getInventoryMap(sessionUser.getUser_id());   
// for all selected recipes  
for (int selRecId : selected) {  
    ...
    // 获取菜品原料关联信息  
    List<RecipeIngredientAssoc> recipeAssoc = recipeIngredientAssocService.findByRecipeId(selRecId); 
    // 对菜品的所有原料进行处理 
    for (RecipeIngredientAssoc eachAssoc : recipeAssoc) {  
	    // 获取原料库中的对应原料
        Inventory inv = invMap.get(eachAssoc.getIngredientId()));
        // 减去菜品中的原料数量  
        float invGram = inv.getCurrentStockGram();  
        inv.setCurrentStockGram(invGram - Float.parseFloat(eachAssoc.getAmount())); 
    }  
}
```

- 但在运行时, 在此处的针对原料库的减法**直接反应到了数据库**, Inventory表的对应值被减少了, 而所有相关代码没有对数据库的修改操作

## Reason
- `java.util.Map`中的`get()`方法, 对于java的基本类型使用的是*值传递*; 而其余的使用的是*地址传递*, 也就是返回一个value对象的引用, 此时操作对象则会直接反应到map中的对象中
- `put()`方法对于自定义类同样也是插入一个对象的引用
- 在Entity层使用了SpringBoot的`@Entity`注释, 如果在事务提交时（或自动刷新时）处于*托管状态（managed state）*，则这些修改会直接反映到数据库中
-  在Dao层和Service层使用了*JpaRepository*和`@Transactional`, 可以直接操作实体对象和标记事务边界, 都会使实体对象进入托管状态, 并在方法调用结束时**自动提交**
- 在`getInventoryMap`方法中使用service取出了实体对象, 直接`put`到*Map*中, 此时**Map中的对象就是service返回的对象**, 会处于托管状态
- 在以上的代码中, 使用service对`RecipeIngredientAssoc`对象进行循环的获取, 每一次都将进入事务并提交, 此时在foreach循环体内处于托管状态的未提交Inventory内容也一并被提交了.

## Solution
- 使用深拷贝, 每次需要修改元素内容时, 将`invMap`中的元素完全拷贝到另一变量, 而不是使用引用, 在修改后重新放入`invMap`, 代码如下
```java
// let available ingredients minus the amount of selected recipe  
List<RecipeIngredientAssoc> recipeAssoc = recipeIngredientAssocService.findByRecipeId(selRecId);  
for (RecipeIngredientAssoc eachAssoc : recipeAssoc) {  
    Inventory inv = new Inventory(invMap.get(eachAssoc.getIngredientId()));  
    float invGram = inv.getCurrentStockGram();  
    inv.setCurrentStockGram(invGram - Float.parseFloat(eachAssoc.getAmount()));  
    invMap.put(eachAssoc.getIngredientId(), inv);  
}
```

- 此时就不会再产生任何对数据库的非法操作了

## References
1. [J. Yue(2023) 将map中的value赋值给list，list改变为什么会引起map也变呢](https://blog.csdn.net/m0_52656317/article/details/129519740)
2. ChatGPT https://chat.openai.com/

2024-04-18