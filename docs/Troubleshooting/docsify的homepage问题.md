## Sitation
- 使用*Docsify*的`homepage`功能时, 如果将该值设置为README.md以外的值(\_sidebar.md), 再使用按钮等链接方式指向README文件, 则文件不可达
- 本地serve的docsify并无此问题

## Reason
- 依据TTL判断, 本地和Github的操作系统类型不同, Github使用Linux服务器, 大小写敏感, docsify优化导致
- Docsify会将`_sidebar.md`文件渲染为`/#/README.md`路径, 此时README.md文件将不与任何路径关联, 故访问不可达

## Solution
- 将homepage属性设为`README.md`文件(默认值), **不使用其它文件作为homepage**
