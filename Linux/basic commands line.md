# Linux 基本命令
____________________________
#### 基本命令
在Linux中，所有设备都是用文件名来表示的，就像我们在分区时所了解的那样，这与我们所熟悉的Windows系统有很大不同，Linux中并没有所谓C盘、D盘之类的说法，并且在Linux中只有文件和目录（相当于Windows中的文件夹），所有文件和目录都以倒树状结构挂载在“/”（读做根目录）目录下，也正是因此Linux系统的管理员称为root（树根）

##### 1. 基本命令
命令行的环境所代表的含义，如下所示：

```shell
[root@localhost]$ /etc #
```

root| localhost | etc
:------ | :------ | :------       
用户名 | 主机名 | 当前目录

对于普通用户来说，提示符“#”显示为“$”。在Linux中如果要执行一个命令则可以通过如下方式：

```shell
# 命令名  [-选项]  参数
```
- 命令名、选项或者参数之间都是至少要有一个空格，多个空格没有关系，选项不是必需的
- 当有多个选项时，可以写在一起。因为Linux基本是由C语言编写的，所以无论命令名或选项，Linux都是严格区分大小写的 

###### 1.1  列出文件清单命令：ls

ls命令能够列出当前目录下的所有内容。ls 命令的执行方式为：

```shell
 # ls [-选项] [文件名或者目录名]
```
知道当前所处的位置有哪些内容，这些信息就可以使用ls命令来获得。它有很多的命令选项，并且选项之间可以互相组合使用

ls选项列表 | 命令选项说明
:------ | :------
-l | 列出所要查看的内容详细信息，不但包括文件夹名，还包括文件大小、访问权限和所有者等信息
-a | 列出所有文件，包括隐藏文件也显示出来
-R | 列出当前目录下的所有内容，并且将子目录的内容也一起列出来
-d | 仅列出目录本身，而不显示当前目录下的内容

在Linux中，ls命令是最常使用的命令之一，因为在命令行下要随时查看目录内容。如果不加任何选项的话，ls命令仅列出当前目录下的文件和目录名，例如，想要查看/etc目录下的内容，可以使用下列命令：

```shell
# ls /etc
```

如果想要列出当前目录下所有文件，则可以使用下列命令：

```shell
# ls -a 
```
- ls -a命令执行结果
  - 可能会发现里面有很多以“.”为开头的文件或者目录，在Linux中，如果一个文件名（目录名）以“.”开头则表示它是隐藏文件（目录）
  - 并且在默认情况下，蓝色代表一个目录，白色代表一个普通文件

- 在默认情况下蓝色代表目录，白色代表普通文件，红色代表压缩文件或者软件包，绿色代表可执行文件，浅蓝色代表链接文件，黄色代表设备文件等
- 但是这并不是在所有情况下都是有效的，之所以能以颜色区分，是因为在执行命令“ls -l”时，实际上是执行了“ls --color=auto”命令，可以使用alias命令进行查看
- 如果要想确切地知道到底是文件还是目录，可以通过ls –l命令，首行字母为“d”则为目录，首行字母为“-”的即为文件，首行字母为“l”的为软链接文件

###### 1.2  改变当前路径命令：cd
cd命令能够改变当前用户所处的位置。cd命令比较简单，其命令执行的方式为：
```shell
# cd 路径
```
路径和相对路径的概念:
- Ubuntu中所有文件或者目录都挂载在“/”目录下，所以如果一个文件或者目录的详细位置是从“/”开始的话，这样的路径称为绝对路径
如/etc/init.d/lvm。
- 如果路径不是从根写起，则称之为相对路径，例如，现在所处的位置为/etc目录中，如果现在要进入init.d目录中，则可以执行如下命令：

```shell
# cd init.d
```
这种不是从根目录写起的路径称为相对路径

其实这两种路径的写法都能达到同样的效果，相对路径的写法有时候更加快速、方便一些，例如，进入很深的一个目录结构中时，而绝对路径能够确保路径一定正确。

例如，现在想从/root目录中进入到/etc目录中，可以下达命令：
```shell
# cd /etc
```

#######特殊目录的表示方法及含义

特殊目录的表示方法 | 含 义
:------| :------
. | 代表当前目录
.. | 代表上层目录
~ | 代表当然登录用户的宿主目录
~用户名 | 代表进入~后用户的宿主目录
- | 代表前一目录，即进入当前目录之前操作的目录

###### 宿主目录:
  - 根目录，相当于windows系统分区的c:\ 
  - 宿主目录是用户自己的目录，相当于windows里面的C:\Users\someuser
  - 所谓宿主目录，就是操作系统为当前用户所设计的用来存放文件、工作的默认目录。如windows中的“我的文档”，就是windows为我们设计的宿主目录
  - linux中每个用户都有自己的宿主目录，这个目录对于普通用户来说，在home/username，而对于root用户来说，在/root。所以当用户为root时，~与/root等价

例子:
ms@ubuntums:/$ ls
bin dev initrd.img lost+found opt run srv usr
boot etc initrd.img.old media proc sbin sys var
cdrom home lib mnt root selinux tmp vmlinuz

可以看到根目录下有root文件家和home文件家。

/home下则有ms和ms2用户的文件夹：

ms@ubuntums:/home$ tree
.
├── lost+found [error opening dir]
├── ms
│   ├── examples.desktop
│   ├── 公共的
│   ├── 模板
│   ├── 视频
│   ├── 图片
│   ├── 文档
│   ├── 下载
│   │   ├── 836e903a5bb5c9ea9840b75bd539b60038f3b3ca.jpg.png
│   │   ├── e1bb0159d109b3de400b50d0ccbf6c81820a4ccd.jpg.png
│   │   └── google-chrome-stable_current_i386.deb
│   ├── 音乐
│   └── 桌面
└── ms2
├── examples.desktop
├── 公共的
├── 模板
├── 视频
├── 图片
├── 文档
├── 下载
├── 音乐
└── 桌面

- 超级用户root，其宿主目录缺省情况下是:/root 
- 用户ms的宿主默认目录是/home/ms.  shell ms@ubuntums:~$  中短～表示我们处在宿主目录
- ubuntu主文件夹窗口，里面包含几个默认的文件夹，桌面、文档、音乐、图片和视频等。主文件夹就是/home/用户目录
提示：
 - 直接在命令行中输入cd命令而不加任何参数，可以马上回到用户的主目录（home），这一点与DOS中cd命令显示当前路径不同，请一定注意
 - 在Linux中，很多与用户自身相关的配置文件、属于自己的文档、程序、脚本和安装包等都存放在用户自己的home目录中，这个目录就相当于Microsoft Windows中的“我的文档”。所以能用cd命令直接“回家”

###### 1.3  查看当前路径命令：pwd

pwd命令能够显示当前所处的路径。
这个命令比较简单，如果有时在操作过程中忘记了当前的路径，则可以通过此命令来查看路径，其执行方式为：
```shell
# pwd 
/home/samlee
```
命令简介
- 该命令用来显示目前所在的工作目录。指令英文原义：print work directory
- 执行权限    ：All User
- 指令所在路径：/usr/bin/pwd 或 /bin/pwd

命令语法
- pwd [OPTION]...

命令参数

参数 | 长参数 | 描叙
-L | --logical（无效）| 当目录为连接路径时，显示连接路径
-P | --physical（无效）| 显示实际物理路径，而非使用连接（link）路径
 | --help | 显示命令在线帮助（该参数无法使用）
 | --version | 显示命令版本信息（该参数无法使用）

####### 使用示例
1：查看pwd命令的帮助信息
```shell
   1: root@DB-Server init.d]# man pwd 
   2: PWD(1)                           User Commands                          PWD(1)
   3:  
   4: NAME 
   5:        pwd - print name of current/working directory
   6:  
   7: SYNOPSIS 
   8:        pwd [OPTION]...
   9:  
  10: DESCRIPTION 
  11:        Print the full filename of the current working directory.
  12:  
  13:        -L, --logical 
  14:               use PWD from environment, even if it contains symlinks
  15:  
  16:        -P, --physical 
  17:               avoid all symlinks
  18:  
  19:        --help display this help and exit
  20:  
  21:        --version 
  22:               output version information and exit
  23:  
  24:        NOTE:  your  shell  may  have  its  own version of pwd, which usually supersedes the version described here.  Please refer to your shell鈥檚 documentation for details about the 
  25:        options it supports.
  26:  
  27: AUTHOR 
  28:        Written by Jim Meyering.
  29:  
  30: REPORTING BUGS 
  31:        Report bugs to <bug-coreutils@gnu.org>.
  32:  
  33: COPYRIGHT 
  34:        Copyright 漏 2006 Free Software Foundation, Inc. 
  35:        This is free software.  You may redistribute copies of it under the terms of the GNU General Public License <http://www.gnu.org/licenses/gpl.html>.  There is NO WARRANTY,  to 
  36:        the extent permitted by law.
  37:  
  38: SEE ALSO 
  39:        The full documentation for pwd is maintained as a Texinfo manual.  If the info and pwd programs are properly installed at your site, the command
  40:  
  41:               info pwd
  42:  
  43:        should give you access to the complete manual.
  44:  
  45: pwd 5.97                           May 2011                             PWD(1) 
  46: (END) 
  47:  
```
2：显示当前目录所在路径 pwd
```shell
   1: [root@DB-Server networking]# pwd 
   2: /etc/sysconfig/networking
```
3：显示当前目录的物理路径 pwd –P
```shell
   1: [root@DB-Server init.d]# cd /etc/init.d 
   2: [root@DB-Server init.d]# pwd -P 
   3: /etc/rc.d/init.d
```
4: 显示当前目录的连接路径：pwd -L
```shell
   1: [root@DB-Server networking]# cd /etc/init.d 
   2: [root@DB-Server init.d]# pwd -L 
   3: /etc/init.d 
   4: [root@DB-Server init.d]# pwd 
   5: /etc/init.d
 ```

###### 1.4  改变文件创建时间及创建空文件命令：touch
- touch命令能够创建一个空白文件，或者改变文件的创建时间。
- touch命令的执行方式为：
```shell
# touch 文件名
```
- 一般来说，建立一个文件都会使用一个文本编辑器（如第8章要介绍的vi编辑器），但是也可以使用touch命令来创建一个空白的文件。
例如，现在要在/home目录下创建一个名为test的空白文件，可以执行命令：
```shell
# touch /home/test
```
- 对于touch命令来说，其最主要的功能是改变文件的时间
- 那么一个文件拥有哪些时间属性呢？对于一个文件来说，主要有三种时间属性，分别为：
 （1）mtime：这个时间记录的是文件内容被修改的时间
 （2）ctime：这个时间记录的是文件的属性（所有者、所属组、文件名）或者权限被修改的时间
 （3）atime：这个时间记录的是文件的内容被读取的时间
- 例子： 在/home目录下创建了一个文件file，然后分别查看其三个时间
```shell
ubuntu@ubuntu:~$ touch file
ubuntu@ubuntu:~$ ls -l file
ubuntu@ubuntu:~$ ls -l --time=atime file
ubuntu@ubuntu:~$ ls -l --time=ctime file
```
- 在刚开始创建文件时候三种时间是相同的
- 在默认情况下使用ls –l命令查看到的是文件内容修改的时间（即mtime）
- 通过不同时间内的不同操作后，file文件的三种时间分别发生了变化，如果现在我们想让其变成与当前时间相同，则可以使用touch命令

####### touch命令选项

touch命令选项 | 参数说明
-a | 仅修改atime时间
-m | 仅修改mtime时间

###### 1.5  创建目录命令：mkdir
mkdir 命令能够创建一个目录。mkdir 命令的执行方式为：
```shell
# mkdir 目录名
```   
- 其实一个目录就是一个特殊类型的文件，就如同Windows中的文件夹一样，目录里面既可以有文件，也可以有子目录，就是因为有目录的存在，Linux才能够以一种目录树的结构对文件系统进行管理
- 例如现在要建立一个directory目录，则可以执行命令：
```shell
# mkdir directory
```
- 创建完目录后可以使用ls –l命令去查看目录是否建立成功。如果directory所在行的第一个字母为d，则说明建立成功。
- 有时候我们需要一次性地建立多级目录，则可以使用-p参数：
```shell
# mkdir -p /home/dir1/dir2/dir3
```

###### 1.6  删除空目录命令：rmdir
rmdir命令能够删除一个空目录。rmdir命令的执行方式为：

```shell
# rmdir 目录名
```
- 对于目录来说，如果里面为空的时候可以使用rmdir命令来删除，并且此命令只能用来删除空目录，如果是非空目录，则需要使用下面要介绍的rm 命令
- 例如我们要删除/home/directory这个空目录，则可以执行命令：
```shell
# rmdir /home/directory
```
提示：
- rmdir可以删除的是非空目录，被删的目录下不能有文件或子目录
- 如果只是有子目录存在，还可以用-p来删除
- 如果含有文件，那么-p选项也无能为力了。只有使用“rm –rf”大法，才能“连根拔起”