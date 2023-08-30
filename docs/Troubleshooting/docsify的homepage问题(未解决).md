## Sitation
- 使用docsify的homepage功能时, 如果将该值设置为README.md以外的值(\_sidebar.md), 再使用按钮等链接方式指向README文件, 则文件不可达
- 本地serve的docsify并无此问题

## Reason (猜测)
- 因为本地和Github部署的文件的编码不同
- Docsify会将`_sidebar.md`文件渲染为`/#/README.md`路径, 此时README.md文件将不与任何路径关联, 故访问不可达

