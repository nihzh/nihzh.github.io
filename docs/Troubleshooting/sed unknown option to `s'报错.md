## Situation
- 使用sed语句, `sed -i "s/viper/$VIPER/g" docker-compose.yml`时, 产生报错如标题

## Reason
- 语句中使用了`/`作为分隔符, 与路径中的`/`引发混淆

## Solution
- 将分隔符使用`|`或`!`等符号代替即可
- `sed -i "s|viper|$VIPER|g" docker-compose.yml` 执行成功

## References
1. https://blog.csdn.net/bang152101/article/details/104491529
2. [bash - Sed - unknown option to \`s' - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/91630/sed-unknown-option-to-s)