## Situations
- 在Linux系统的Docker中安装
- 跟随官方指导[Docker 环境安装 ARL · TophantTechnology/ARL Wiki (github.com)](https://github.com/TophantTechnology/ARL/wiki/Docker-%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85-ARL)安装
- 采用git clone方式拉取
- 采用docker-compose启动
- 安装成功完成后, 访问`https://localhost:5003`后, 越过登录界面直接显示灯塔主页
- 进行任何操作没有响应, 弹出报错`timeout of 12000ms exceeded`

## Reasons
>作者写了一个BUG  
在config.py里对”RISKIQ“的引用如下两句：  
Config.RISKIQ_EMAIL = y["RISKIQ"]["EMAIL"]  
Config.RISKIO KEY = y["RISKIQ"]["KEY"]  
但是在config.yaml中并未声明这个
-- Ye0kr1n on Github

## Fixing
`docker-compose down` 关停并销毁容器
在`ARL/docker/config-docker.yaml`中添加
```
#演示帐号有查询额度限制，请前往 https://community.riskiq.com/ 注册自己的key并替换
RISKIQ:
  EMAIL: "n1un1u2019@qq.com"
  KEY: "03da3c29cce5152a536bae332f7b03a288154b37a13b93921225d3ade49c9b4c"
```
`docker-compose up -d` 重新创建并启动容器
*可惜的是RISKIQ网站现在无法注册了, 先用这个顶一下*

## References
1. [timeout of 12000ms exceeded · Issue #476 · TophantTechnology/ARL (github.com)](https://github.com/TophantTechnology/ARL/issues/476)
2. [ARL/docker/config-docker.yaml at 8dd790df6afa22b57591ba20f11a4b3b5570130d · TophantTechnology/ARL (github.com)](https://github.com/TophantTechnology/ARL/blob/8dd790df6afa22b57591ba20f11a4b3b5570130d/docker/config-docker.yaml#LL11-L11C8)
