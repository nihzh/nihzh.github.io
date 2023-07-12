## REST简介
- REST (Representational State Transfer), 表现形式状态转换, 访问网络资源的格式
![[Pasted image 20230214133633.png]]
- 所有数据通过post提交
- 隐藏资源的访问行为,无法通过地址得知对资源是何种操作
- 书写简化
- 按照REST风格访问资源时使用**行为动作--method**区分对资源进行了何种操作
	- get, post, put, delete......
![[Pasted image 20230214150851.png]]
- 仅作为一种风格, 约束了资源的访问形式, 是约定方式不是规范,可以打破
- 根据REST风格对资源进行访问称为***RESTful***

## 案例
#### @RequestMapping
- 方法注解, 位于SpringMVC控制器方法定义上方, 用于设置当前控制器啊方法请求访问路径. 属性value(默认): 请求访问路径, method: http请求动作
#### @PathVariable
- 形参注解, 在SpringMVC控制器方法形参定义前面, 用于绑定路径参数于处理器方法形参间的关系, 要求路径参数名与形参名一一对应

- @RequestBody 用于接收json数据, 当请求参数超过一个时适用
- @RequestParam 用于接收url地址传参或表单传参, 适用于非json格式
- @PathVariable用于接收路径参数, 使用{参数名称}描述路径参数, 通常用于传递id值

#### 示例
- GET方法主要用作查询
```java
@RequestMapping(value = "/users/{id}", method = RequestMethod.GET)
@ResponseBody
public String getById(@PathVariable Integer id){
	System.out.println("user getById..." + id);
	return "{'module':'user getById'}";
}
```

```java
@RestController
@RequestMapping("/books")
public class BookController{
	@PostMapping
	public String save(@RequestBody Book book){
		System.out.println("book save..." + book);
		return "{'module':'book save'}";
	}

	@DeleteMapping("/{id}")
	public String delete(@PathVariable Integer id){
		System.out.println("Book delete..." + id);
		return "{'module':'book delete'}";
	}
}
```
