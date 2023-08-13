*Magic Number 幻数*也称*魔数*, 在计算机编程中有多重含义:
1. 一个独一无二的值, 需要在程序里多次出现, 但未被赋值为常量
2. 一段固定的数字或文字值, 用于定义文件格式和协议, 一般被声明于文件hex头部或协议头部
3. 一个无歧义的, 独特的值

## 未赋值常量的值
也被称为magic constant魔法常量, 是一种在程序源码中直接使用数值的*反模式*用法, 这种数字掩盖了开发人员选择该数字的意图, 增加了出现细微错误的机会, 增加了扩展和改编程序的难度, 所以, **使用有意义的名称对固定常量赋值**, 可以使程序更加容易阅读, 理解和维护

## 文件格式和协议
### 文件格式
幻数实现了一种强类型数据, 在程序运行中提供一种内部信号, 控制程序读取数据的方法. 大多数文件包含了这样的数据, 可以简单有效地区分文件格式, 并且可以产生进一步的运行中信息.
```
JPEG (jpg)，文件头：FFD8FF
PNG (png)，文件头：89504E47
GIF (gif)，文件头：47494638
TIFF (tif)，文件头：49492A00
Windows Bitmap (bmp)，文件头：424D
CAD (dwg)，文件头：41433130
Adobe Photoshop (psd)，文件头：38425053
Rich Text Format (rtf)，文件头：7B5C727466
XML (xml)，文件头：3C3F786D6C
HTML (html)，文件头：68746D6C3E
Email [thorough only] (eml)，文件头：44656C69766572792D646174653A
Outlook Express (dbx)，文件头：CFAD12FEC5FD746F
Outlook (pst)，文件头：2142444E
MS Word/Excel (xls.or.doc)，文件头：D0CF11E0
MS Access (mdb)，文件头：5374616E64617264204A
WordPerfect (wpd)，文件头：FF575043
Adobe Acrobat (pdf)，文件头：255044462D312E
Quicken (qdf)，文件头：AC9EBD8F
Windows Password (pwl)，文件头：E3828596
ZIP Archive (zip)，文件头：504B0304
RAR Archive (rar)，文件头：52617221
Wave (wav)，文件头：57415645
AVI (avi)，文件头：41564920
Real Audio (ram)，文件头：2E7261FD
Real Media (rm)，文件头：2E524D46
MPEG (mpg)，文件头：000001BA
MPEG (mpg)，文件头：000001B3
Quicktime (mov)，文件头：6D6F6F76
Windows Media (asf)，文件头：3026B2758E66CF11
MIDI (mid)，文件头：4D546864
```

### 协议
- The [OSCAR protocol](https://en.wikipedia.org/wiki/OSCAR_protocol "OSCAR protocol"), used in [AIM](https://en.wikipedia.org/wiki/AOL_Instant_Messenger "AOL Instant Messenger")/[ICQ](https://en.wikipedia.org/wiki/ICQ "ICQ"), prefixes requests with `2A`.
- In the [RFB protocol](https://en.wikipedia.org/wiki/RFB_protocol "RFB protocol") used by [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing "Virtual Network Computing"), a client starts its conversation with a server by sending "RFB" (`52` `46` `42`, for "Remote Frame Buffer") followed by the client's protocol version number.
- In the [SMB](https://en.wikipedia.org/wiki/Server_Message_Block "Server Message Block") protocol used by Microsoft Windows, each SMB request or server reply begins with '`FF` `53` `4D` `42`', or `"\xFFSMB"` at the start of the SMB request.
- In the [MSRPC](https://en.wikipedia.org/wiki/MSRPC "MSRPC") protocol used by Microsoft Windows, each TCP-based request begins with `05` at the start of the request (representing Microsoft DCE/RPC Version 5), followed immediately by a `00` or `01` for the minor version. In UDP-based MSRPC requests the first byte is always `04`.
- In [COM](https://en.wikipedia.org/wiki/Component_Object_Model "Component Object Model") and [DCOM](https://en.wikipedia.org/wiki/Distributed_Component_Object_Model "Distributed Component Object Model") marshalled interfaces, called [OBJREFs](https://en.wikipedia.org/wiki/OBJREF "OBJREF"), always start with the byte sequence "MEOW" (`4D` `45` `4F` `57`). Debugging extensions (used for DCOM channel hooking) are prefaced with the byte sequence "MARB" (`4D` `41` `52` `42`).
- Unencrypted [BitTorrent tracker](https://en.wikipedia.org/wiki/BitTorrent_tracker "BitTorrent tracker") requests begin with a single byte containing the value `19` representing the header length, followed immediately by the phrase "BitTorrent protocol" at byte position 1.
- [eDonkey2000](https://en.wikipedia.org/wiki/EDonkey2000 "EDonkey2000")/[eMule](https://en.wikipedia.org/wiki/EMule "EMule") traffic begins with a single byte representing the client version. Currently `E3` represents an eDonkey client, `C5` represents eMule, and `D4` represents compressed eMule.
- The first 4 bytes of a block in the [Bitcoin](https://en.wikipedia.org/wiki/Bitcoin "Bitcoin") Blockchain contains a magic number which serves as the network identifier. The value is a constant `0xD9B4BEF9`, which indicates the main network, while the constant `0xDAB5BFFA` indicates the testnet.
- [SSL](https://en.wikipedia.org/wiki/Secure_Sockets_Layer "Secure Sockets Layer") transactions always begin with a "client hello" message. The record encapsulation scheme used to prefix all SSL packets consists of two- and three- byte header forms. Typically an SSL version 2 client hello message is prefixed with a `80` and an SSLv3 server response to a client hello begins with `16` (though this may vary).
- [DHCP](https://en.wikipedia.org/wiki/DHCP "DHCP") packets use a "magic cookie" value of '`0x63` `0x82` `0x53` `0x63`' at the start of the options section of the packet. This value is included in all DHCP packet types.
- [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2 "HTTP/2") connections are opened with the preface '`0x505249202a20485454502f322e300d0a0d0a534d0d0a0d0a`', or "`PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n`". The preface is designed to avoid the processing of frames by servers and intermediaries which support earlier versions of HTTP but not 2.0.

### 接口
- [IBM PC](https://en.wikipedia.org/wiki/IBM_PC "IBM PC")-compatible [BIOSes](https://en.wikipedia.org/wiki/BIOS "BIOS") use magic values `0000` and `1234` to decide if the system should count up memory or not on reboot, thereby performing a cold or a warm boot. Theses values are also used by [EMM386](https://en.wikipedia.org/wiki/EMM386 "EMM386") memory managers intercepting boot requests.[[12]](https://en.wikipedia.org/wiki/Magic_number_(programming)#cite_note-Paul_2002_MAGIC-12) BIOSes also use magic values `55 AA` to determine if a disk is bootable.[[13]](https://en.wikipedia.org/wiki/Magic_number_(programming)#cite_note-13)
- The [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS "MS-DOS") disk cache [SMARTDRV](https://en.wikipedia.org/wiki/SMARTDRV "SMARTDRV") (codenamed "Bambi") uses magic values BABE and EBAB in API functions.[[12]](https://en.wikipedia.org/wiki/Magic_number_(programming)#cite_note-Paul_2002_MAGIC-12)
- Many [DR DOS](https://en.wikipedia.org/wiki/DR_DOS "DR DOS"), [Novell DOS](https://en.wikipedia.org/wiki/Novell_DOS "Novell DOS") and [OpenDOS](https://en.wikipedia.org/wiki/OpenDOS "OpenDOS") drivers developed in the former _European Development Centre_ in the UK use the value 0EDC as magic token when invoking or providing additional functionality sitting on top of the (emulated) standard DOS functions, NWCACHE being one example.[[12]](https://en.wikipedia.org/wiki/Magic_number_(programming)#cite_note-Paul_2002_MAGIC-12)

### 其它用法
- 在`Texas Instruments`的SOC上的默认MAC地址是`DE:AD:BE:EF:00:00`

## 数据类型的极值
|Decimal|Hex|Description|
|---|---|---|
|[18,446,744,073,709,551,615](https://en.wikipedia.org/wiki/18,446,744,073,709,551,615 "18,446,744,073,709,551,615")|FFFF FFFF FFFF FFFF|The maximum unsigned 64 bit value (264 − 1)|
|[9,223,372,036,854,775,807](https://en.wikipedia.org/wiki/9,223,372,036,854,775,807 "9,223,372,036,854,775,807")|7FFF FFFF FFFF FFFF|The maximum signed 64 bit value (263 − 1)|
|[4,294,967,295](https://en.wikipedia.org/wiki/4,294,967,295 "4,294,967,295")|FFFF FFFF|The maximum unsigned 32 bit value (232 − 1)|
|[2,147,483,647](https://en.wikipedia.org/wiki/2,147,483,647 "2,147,483,647")|7FFF FFFF|The maximum signed 32 bit value (231 − 1)|
|[65,535](https://en.wikipedia.org/wiki/65,535 "65,535")|FFFF|The maximum unsigned 16 bit value (216 − 1)|
|32,767|7FFF|The maximum signed 16 bit value (215 − 1)|
|[255](https://en.wikipedia.org/wiki/255_(number) "255 (number)")|FF|The maximum unsigned 8 bit value (28 − 1)|
|127|7F|The maximum signed 8 bit value (27 − 1)|
|−128|80|Minimum signed 8 bit value|
|−32,768|8000|Minimum signed 16 bit value|
|−2,147,483,648|8000 0000|Minimum signed 32 bit value|
|−9,223,372,036,854,775,808|8000 0000 0000 0000|Minimum signed 64 bit value|

## Debug value
是在分配或释放期间写入内存的特定值, 一边以后可以判断它们是否损坏, 在读取未初始化的内存中的值极为明显. 通常以十六进制形式显示, 以奇数值为首选, 这样没有字节寻址的处理器在视图将它们用作指针时就会出错(指针必须为偶数地址), 且应该选择远离程序代码, 静态数据, 堆数据或堆栈的值. 类似的, 可以选择在指定体系结构的指令集中无效的代码
- `0x5f375a86` 快速求平方根倒数
```c
/*
* magic number - 0x5f375a86
* 输入一个单精度浮点数 a
* 返回结果为 1 / sqrt(a)
* 比如输入 4.0 返回 0.499154 (准确值应是 0.5)
*
* 注：这样使用 union 是不符合标准的，但是在大多数编译器上都可以通过编译并正确运行
*/
float r_sqrt(float a) {
    union {
        int ii;
        float i;
    };
    i = a;
    float ihalf = 0.5f * i;
    ii = 0x5f375a86 - (ii >> 1);

    i = i * (1.5f - ihalf * i * i);
    //i = i * (1.5f - ihalf * i * i);
    //i = i * (1.5f - ihalf * i * i);
    return i;
}
```
- 位元反序
```c
/*
* magic number - 0x00082082、0x01122408、255
* 输入一个 6 位二进制数
* 返回 6 位二进制数，其位顺序和输入相反
* 比如输入 012345
* 返回    543210
* 此处的字母和数字代表特定 {0, 1}
* unsigned char 高 2 位无意义
*/
unsigned char revert(unsigned char i) {
    return ((i * 0x00082082) & 0x01122408) % 255;
}
```
- 除数为3的无符号除法
```c
/*
* magic number - 2863311531
* 除数为 3 的无符号除法
*
* 编译器版本 和 目标平台
* Apple LLVM version 9.0.0 (clang-900.0.38)
* Target: x86_64-apple-darwin17.2.0
*/
unsigned int div(unsigned int i) {
    ...
    /*
    * 在上述编译器和平台上
    * -O0 生成汇编 
    * movl    $3, %ecx
    * movl    -4(%rbp), %eax
    * xorl    %esi, %esi
    * movl    %esi, %edx
    * divl    %ecx
    *
    * -O2 生成汇编
    * movl    $2863311531, %edx
    * imulq   %rcx, %rdx
    * shrq    $33, %rdx
    */
    unsigned int z = i / 3;
    ...
}
```

# References
1. [Magic number (programming) - Wikipedia](https://en.wikipedia.org/wiki/Magic_number_(programming))
2. [一些 Magic number 的由来、解释和推导 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/33543750?from_voters_page=true)
3. [文件格式的幻数File Format and Magic Number_文件幻数_BloodyEve的博客-CSDN博客](https://blog.csdn.net/qq_35980805/article/details/106725455)