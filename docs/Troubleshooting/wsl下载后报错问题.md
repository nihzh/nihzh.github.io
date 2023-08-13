## Situation
- Windows 10 系统 22H2版本
- 使用Microsoft商店下载的Ubuntu 22和Kali WSL子系统
- 下载后显示以下报错信息
```text
WslRegisterDistribution failed with error: 0x80004002
Error: 0x80004002 ??????
```

## Reason
- Windows的版本太老, 不符合WSL安装的要求
	- 对于 x64 系统：版本 1903 或更高版本，内部版本为 18362.1049 或更高版本。
	- 对于 ARM64 系统：版本 2004 或更高版本，内部版本为 19041 或更高版本。
- 未开启Windows系统中的*WSL可选功能*
- 未启用Windows系统中的*虚拟机平台*功能

## Solution
跟随官方文档, 使用命令开启以上功能, 并下载旧版的WSL系统
```Powershell
# 在PowerShell中
# 1. 启用WSL
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# 2. 启用虚拟机
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
3. 重启计算机, 并下载[WSL2 内核更新包](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi), 双击运行
```Powershell
# 4. 将wsl2设为默认
wsl --set-default-version 2
```
5. 到应用商店, 下载需要的Windows发行版

## References
1. [旧版 WSL 的手动安装步骤 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual)
2. [WSL Ubuntu error 0x80004002 · Issue #2851 · microsoft/WSL (github.com)](https://github.com/Microsoft/WSL/issues/2851)