# ssh
- [ssh用法及命令](https://blog.csdn.net/pipisorry/article/details/52269785)
- [SSH 基本用法](https://zhuanlan.zhihu.com/p/21999778)
______________________________________________
### 什么是ssh
- SSH是一种网络协议，用于计算机之间的加密登录
- 如果一个用户从本地计算机，使用SSH协议登录另一台远程计算机，我们就可以认为，这种登录是安全的，即使被中途截获，密码也不会泄露。最早的时候，互联网通信都是明文通信，一旦被截获，内容就暴露无疑。1995年，芬兰学者Tatu Ylonen设计了SSH协议，将登录信息全部加密，成为互联网安全的一个基本解决方案，迅速在全世界获得推广，目前已经成为Linux系统的标准配置。
- SSH只是一种协议，存在多种实现，既有商业实现，也有开源实现。本文针对的实现是OpenSSH，它是自由软件，应用非常广泛。这里只讨论SSH在Linux Shell中的用法。如果要在Windows系统中使用SSH，会用到另一种软件PuTTY

- SSH之所以能够保证安全，原因在于它采用了公钥加密。
- 整个过程是这样的：
  （1）远程主机收到用户的登录请求，把自己的公钥发给用户
  （2）用户使用这个公钥，将登录密码加密后，发送回来
  （3）远程主机用自己的私钥，解密登录密码，如果密码正确，就同意用户登录
- 这个过程本身是安全的，但是实施的时候存在一个风险：
  - 如果有人截获了登录请求，然后冒充远程主机，将伪造的公钥发给用户，那么用户很难辨别真伪
  - 因为不像https协议，SSH协议的公钥是没有证书中心（CA）公证的，也就是说，都是自己签发的。
  - 可以设想，如果攻击者插在用户与远程主机之间（比如在公共的wifi区域），用伪造的公钥，获取用户的登录密码。再用这个密码登录远程主机，那么SSH的安全机制就荡然无存了。这种风险就是著名的"中间人攻击"（Man-in-the-middle attack）

### ssh安装
- SSH分客户端openssh-client和openssh-server
- 如果你只是想登陆别的机器的SSH只需要安装openssh-client
（ubuntu有默认安装，如果没有则sudo apt-get install openssh-client），如果要使本机开放SSH服务就需要安装openssh-server
- Ubuntu缺省已经安装了ssh client
- ssh-agent表示ssh-client启动，sshd表示ssh-server启动了


### 配置ssh
```shell
echo -e "\033[31;1m ******************************* \033[0m"
echo -e "\033[31;1m ************安装和配置ssh************ \033[0m"
sudo apt-get install -y openssh-server 1> /dev/null
sudo sed -i 's/UsePAM no/UsePAM yes/g' /etc/ssh/sshd_config
sudo sed -i '8a /etc/init.d/ssh start' /etc/profile
sudo /etc/init.d/ssh start
ps -e | grep ssh

echo -e "\033[31;1m ssh授权 \033[0m"
cd ~/.ssh/
ssh-keygen -t rsa
cat ./id_rsa.pub >> ./authorized_keys

$ ps -e|grep ssh
 2151 ?        00:00:00 ssh-agent

 5313 ?        00:00:00 sshd
```
- 如果缺少sshd，说明ssh服务没有启动或者没有安装

