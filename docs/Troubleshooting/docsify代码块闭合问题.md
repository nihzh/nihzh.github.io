## 问题描述
- 使用docsify部署的GitHub page个人blog页面
- md文件中代码块不能正常闭合, 在其他markdown编辑器中无此情况
	- vscode
	- obsidian

## 原因
- 当代码块紧接(不空行)列表时, 代码块内容如果有空行, 则会从空行处断开
- 这是docsify的程序问题, 暂无时间分析修改
- 列表: 有序列表, 无序列表

## 解决办法
- 将紧接列表的代码块前添加空行 (列表和代码块之间)
- 删除代码块空行
- 提issue
- fork项目修改 (https://docsify.js.org/#/zh-cn/markdown)
原项目地址: https://github.com/docsifyjs/docsify