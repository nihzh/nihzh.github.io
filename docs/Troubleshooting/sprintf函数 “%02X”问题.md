## Situations
- c语言中使用`sprintf`函数转换integer类型为十六进制字符串时，出现了内存越界修改的问题，访问并污染了程序内其它变量
- 所使用的格式化符号是`%02X`，转换为长度为2的十六进制字符串

## Resons
- `sprintf`函数将任意变量转换为char并赋值到指定字符串（char数组）
- `%02X`指定输出为两位十六进制，二进制长度8 bits，将占用**1 Byte**空间
- `sprintf`函数的十六进制转换方式为直接读取十六进制数再分别转换为char
- 所以对于两位十六进制数，传入变量的**最大长度为1 Byte**，数据类型应为*unsigned char*，取值范围0-255
- 同时，如果传入大于该长度的变量如*int*，即使值在0-255之间，该函数仍旧会将空白部分转换，并越界存储转换的值`\000`

## Reference
1. BingGoow: https://blog.csdn.net/libingw21/article/details/50593885