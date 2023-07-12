Firstly, I following the guide [Git Environment Building](https://blog.csdn.net/alice_tl/article/details/78388076), when running `ssh -T git@github.com` to confirm the connection status, an error occoured: **"Permission denied(publickey)"**.

To think about the situation that ssh service may not enabled, use `ssh-agent -s` to start the service and `ssh-add ~/.ssh/mykey` to reconnect the ssh, the error still existed: **"Could not open a connection to your authentication agent"**

After searching on the internet, I discovered that the *"OpenSSH Authentication Agent"* service meight disabled by updated 1803 edition, so go check and enabled it. Then resrarted the machine, the ssh still not working.

Then I redone the process in the guide: creating rsa private and public keys, transmitting the public key to github and complete all the acting that may help to solve the problem. Indeed a pare of new keys generated, but the error encounted as usual.

According to [Could not open a connection to your authentication](https://blog.csdn.net/argleary/article/details/100638560), the command `ssh-agent bash` could run ssh as the parent of the bash shell. Implement it then retry `ssh -T git@github.com`......

It finally worked!
![[Pasted image 20220816210429.png]]

However, when I closed the Git bash and reopen, the permission denied occoured again, follow this article to solve the problem permanently: [git ssh Permission denied](https://blog.csdn.net/alexander_phper/article/details/52871191)

##### Reference(zh-cn): 
[Git enfieonment building](https://blog.csdn.net/alice_tl/article/details/78388076)
[Git occours git@github.com: Permission denied (publickey).](https://blog.csdn.net/qq_43768946/article/details/90411154)
[Solution of win10 unable to start ssh-agent service, error :1058](https://blog.csdn.net/qq_19926599/article/details/86380544)
[Could not open a connection to your authentication agent](https://blog.csdn.net/argleary/article/details/100638560)
[git ssh Permission denied](https://blog.csdn.net/alexander_phper/article/details/52871191)


Last Edited by: nihzh - 220816