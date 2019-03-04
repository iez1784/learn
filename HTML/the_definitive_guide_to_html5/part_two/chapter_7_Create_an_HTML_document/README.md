### Chapter 7 -- 创建HTML文档 (P98~P125)
____________________________________________
- 本章介绍最基础的HTML5元素: 文档元素和元数据元素
- 它们是用来创建HTML文档和说明其内容的元素

##### 表 7-1 本章内容摘要

问题 | 解决方案 | 代码清单
:------ | :------ | :------
表示文档包含的是HTML5内容 | 使用DOCTYPE元素 | 7-1
表示文档中HTML标记的开始 | 使用html元素 | 7-2
表示HTML文档中元数据部分的开始 | 使用head元素 | 7-3
表示HTML文档中内容部分的开始 | 使用body元素 | 7-4
设置HTML文档的标题 | 使用title元素 | 7-5
设置用做HTML文档中的相对URL解析基础的URL | 使用base元素 | 7-6
添加对于HTML文档所包含数据的说明 | 使用meta元素 | 7-7
声明HTML文档的字符编码 | 使用带charset属性的meta元素 | 7-8
设置HTML文档的默认样式表或周期性地刷新页面内容 | 使用带http-equiv属性的meta元素是| 7-9
定义问答内嵌样式 | 使用style元素 | 7-10 ~ 7-12
载入包括样式表和网站标志在内的外部资源 | 使用link元素 | 7-13 ~ 7-15
预先载入预计马上就会用到的资源 | 使用link元素，并将其rel属性值设置为prefetch | 7-16
定义文档内嵌脚本| 使用script元素 | 7-17
载入外部脚本文件 | 使用带src属性的script元素 | 7-18、 7-19
控制脚本的执行时机和执行方式 | 使用带async或defer属性的script元素 | 7-20 ~ 7-24
显示为浏览器不支持或禁用了JavaScript的情况准备的内容 |  使用noscript元素 | 7-25 ~ 7-26

### 7.1 构筑基本的文档结构
- 先从文档元素说起
- 这些基础成分确定了HTML文档的轮廓以及浏览器的初始环境
- 文档元素只有4个，但是任何HTML文档都需要所有这些元素

#### 7.1.1 DOCTYPE元素
- DOCTYPE元素独一无二，而且自成一类
- 每一个HTML文档都必须以DOCTYPE元素开头
- 浏览器据此得知自己将要处理的是HTML内容
- 即使省略DOCTYPE元素，大多数浏览器仍能正确显示文档内容，只不过依赖浏览器的这种表现不是好习惯

##### 表7-2 DOCTYPE元素
类型 | 说明
:------ | :------ 
元素 | DOCTYPE
元素类型 | 无
允许具有的父元素 | 无
局部属性 | 无
内容 | 无
标签用法 | 单个开始标签
是否为HTML5新增 | 否
在HTML5中的变化 | HTMl4中要求要有的DTD已不再使用
习惯样式 | 无

- 在HTML5中DOCTYPE元素之一一种用法，如代码清单 7-1 所示

##### 代码清单7-1 使用DOCTYPE元素
```html
<!DOCTYPE HTML>
```
- 这个元素告诉浏览器两件事情:
  1. 它处理的是HTML文档
  2. 用来标记文档内容的HTML所属的版本
  3. 版本号不用写
  4. 浏览器能自动探测出这里所用的是HTML5
  5. 该元素没有结束标签
  6. 只消在文档开头放上它唯一的标签就行

#### 7.1.2 html元素
- html元素更恰当的名称是根元素
- 它表示文档中HTML部分的开始

##### 表7-3 html元素
类型 | 说明
:------ | :------ 
元素 | html
元素类型 | 无
允许具有的父元素 | 无
局部属性 | manifest (详见第40章)
内容 | head元素和body元素各一
标签用法 | 开始标签和结束标签，内含其他元素
是否为HTML5新增 | 否
在HTML5中的变化 | manifest属性是HTML5中新增的。HTML4版本中的属性已不再使用
习惯样式 | html {display : block;}
 | html: focus {outline: none;}

 ##### 代码清单7-2 使用html元素
 ```html
<!DOCTYPE HTML>
<html>
......此处省略内容和元素......
</html>
 ```

 #### 7.1.3 head元素
 - head元素包含着文档的元数据
 - HTML中，元数据向浏览器提供了有关文档内容和标记的信息，此处还可以包含脚本和对外部资源(比如CSS样式表)的引用

 ##### 表7-4 head元素
 类型 | 说明
:------ | :------ 
元素 | head
元素类型 | 无
允许具有的父元素 | html
局部属性 | 无
内容 | 必须有一个title元素，其他元数据元素可有可无
标签用法 | 开始标签和结束标签，内含其他元素
是否为HTML5新增 | 否
在HTML5中的变化 | 无
习惯样式 | 无

- 每个HTML文档都应该包含一个head元素，而后者(head)必须包含一个title元素

##### 代码清单 7-3 使用head元素
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>title</title>
    </head>
</html>
```

#### 7.1.4 body元素
- HTML文档的元数据和文档信息包装在head元素中，文档的内容则包装在body元素中
- body元素总是紧跟在head元素之后，它是html元素的第二个子元素

##### 表7-5 body元素
类型 | 说明
:------ | :------ 
元素 | body
元素类型 | 无
允许具有的父元素 | html
局部属性 | 无
内容 | 所有短语元素和流元素
标签用法 | 开始标签和结束标签
是否为HTML5新增 | 否
在HTML5中的变化 | alink、background、bgcolor、link、margintop、marginbottom、marginleft、marginright、marginwidth、text和vlink属性不再使用。这些属性的效果可用CSS实现
习惯样式 | body {display:block; margin: 8px;}
        | body: focus {outline: none;}

##### 代码清单7-4 使用body元素
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>使用body元素</title>
    </head>
    <body>
        <p>
            I like <code id = "applecode"> apples</code> and oragnes.
        </p>
        <a href="http://apress.com">Visit Apress.com </a>
    </body>
</html>    
```

### 7.2 用元数据元素说明文档
- 元数据元素可以用来提供关于HTML文档的信息
- 它们本身不是文档内容，但提供了关于后面的文档内容的信息
- 元数据元素应放在head元素中

#### 7.2.1 设置文档标题
- title元素的作用是设置文档的标题或名称
- 浏览器通常将该元素的内容显示在其窗口顶部或标签页的标签上

###### 表7-6 title元素
类型 | 说明
:------ | :------ 
元素 | title
元素类型 | 元数据
允许具有的父元素 | head
局部属性 | 无
内容 | 文档标题或对文档内容言简意赅的说明
标签用法 | 开始标签和结束标签。内含文字
是否为HTML5新增 | 否
在HTML5中的变化 | 无
习惯样式 | title {display: none;}

- 每个HTML文档都应该有且只有一个title元素，其开始标签和结束标签之间的文字在用户眼里应用实践意义
- 至少用户应能根据此区分各个浏览器窗口或浏览器的各个标签页，并且知道哪个显示的才是你的Web应用系统

##### 代码清单7-5 使用title元素
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>使用title元素</title>
    </head>
    <body>
        <p>
            I like <code id = "applecode"> apples</code> and oragnes.
        </p>
        <a href="http://apress.com">Visit Apress.com </a>
    </body>
</html>    
```

#### 7.2.2设置相对URL的解析基准
- base元素可用来设置一个基准URL，让HTML文档中的相对链接在此基础上进行解析
- 相对链接省略了URL中的协议、主机和端口部分，需要根据别的URL(要么是base元素中指定的URL，要么是用以加载当前文档的URL)得出其完整形式
- base元素还能设定链接在用户点击时的打开方式，以及提交表单时浏览器如何反应

##### 表7-7 base元素
类型 | 说明
:------ | :------ 
元素 | base
元素类型 | 元数据
允许具有的父元素 | head
局部属性 | href、target
内容 | 无
标签用法 | 虚元素形式
是否为HTML5新增 | 否
在HTML5中的变化 | 无
习惯样式 | 无

- HTML文档至少应该包含一个base元素
- 它通常是head元素中位置最靠前的子元素之一，以便随后的元数据元素中的相对URL可以用上其设置的基准URL

1. 使用href属性
- herf属性指定了解析文档此后部分中的相对URL要用到的基准URL

##### 代码清单 7-6 使用base元素中的href属性
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title> 使用base元素中的href属性</title>
        <base href="http://titan/listings/"/>
    </head>
    <body>
        <p>
            I Like <code id = "apples">apples </code> and oranges.
        </p>
        <a href="http://apress.com">Visit Apress.com</a>
        <a href="page2.html">Page 2</a>
    </body>
</html>
```

- 此例将基准URL设置为http://titan/listings/. 其中titan是开发服务器的名称，而listings是服务器上包含本书示例文件的目录
- 在文档的后面部分会有一个用来生成超链接的a元素，它使用了page2.html这个相对URL
- 用户点击这个超链接时，浏览器会把基准URL和相对URL拼接成完整的URL: http://titan/listings/page2.html
- 提示
  - 如果不用base元素，或不用其href属性设置一个基准URL，那么浏览器会将当前文档的URL认定为所有相对URL的解析基准
  - 例如，假设浏览器使用了http://myserver.com/app/mypages.html这个URL载入了一个文档，该文档中有一个超链接使用了myotherpage.html这个URL，那么点击这个超链接时浏览器将尝试从http://myserver.comapp.myotherpage.html这个绝对URL加载第二个文档

 2. 使用target属性
 - target属性的作用是告诉浏览器该如何打开URL
 - 这个属性的值代表着一个浏览上下文(browsing context)

 #### 7.2.3 用元数据说明文档
 - meta元素可以用来定义文档的各种元数据
 - 它有多种不同用法，而且一个HTML文档中可以包含多个meta元素

 ##### 表7-8 meta元素
类型 | 说明
:------ | :------ 
元素 | meta
元素类型 | 元数据
允许具有的父元素 | head
局部属性 | name、content、charset和http-equiv
内容 | 无
标签用法 | 虚元素形式
是否为HTML5新增 | 否
在HTML5中的变化 | charset属性是HTML5中新增的。在HTML4中，http-equiv属性可以有任意多个不同值。而在HTML5中情况有所不同，只有本小节所说的值才能使用。HTML4中的scheme属性在HTML5中已不再使用。此外，现在已不再使用meta元素来制定网页所用的语言
习惯样式 | 无

- 下面介绍几种meta元素的用法
- 每个meta元素只能用于一种用途
- 如果在这些特性中要使用的不止一个，那就应该在head元素中添加多个meta元素

1. 指定名/值元数据对
- meta元素的第一个用途是用名/值对定义元数据，为此需要用到其name和content属性

##### 代码清单 7-7 在meta元素中用名/值对定义元数据
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>7-7 在meta元素中用名/值对定义元数据</title>
        <base href="http://titan/listings/">
        <meta name="author" content="Adam Freeman"/>
        <meta name="description" content="A simple example"/>
    </head>
    <body>
        <p>
            I like <code id="applecode">apples</code> and oranges.
        </p>
        <a href="http://apress.com">Visit Apress.com</a>
        <a href="page2.html">Page 2</a>
    </body>
</html>
```
- 此处name属性用来表示数据的类型，而content属性用来提供值
- 表 7-9 列出了meta元素可以使用的几种预定义元数据类型
- 除了表中5个预定义的元数据名称，还可以使用元数据扩展
- [MetaExtensions](http://wiki.whatwg.org/wiki/MetaExtensions)有这些扩展的一份时常更新的清单

##### 表 7-9 供meta元素使用的预定义元数据类型
元数据名称 | 说明
:------ | :------
application name | 当前页所属Web应用系统的名称
author | 当前页的作者名
description | 当前页的说明
generator | 用来生成HTML的软件名称(通常用于Ruby on Rails、ASP.NET等服务器端框架生成HTML页的情况下)
keywords | 一批以逗号分开的字符串，用来描述页面的内容

- 这个元数据类型有三个大多数搜索引擎都认识的值: noindex(表示不要索引本页)、noarchive(表示不要将本页存档或缓存)和nofollow(表示不要顺着本页中的链接继续搜索下去)
- 提示: 
    - 要告诉搜索引擎如何对内容分类和分等级，过去最主要的手段就是使用keywords元数据
    - 现在的搜索引擎对keywords元数据的重视程度远不如前，这是因为它可以被滥用来制造页面内容和相关性的假象
    - 要想让内容在搜索引擎眼里有所改观，最好的办法是采纳它们自己提供的建议
    - 大多数搜索引擎都提供了优化网页或整个网站的指南
    - [谷歌的指南](http://google.com/support/webmasters/bin/topic.py?topic=15260)

2. 声明字符编码
- meta元素的另一种用途是声明HTML文档内容所用的字符编码

##### 代码清单 7-8 用meta元素声明字符编码
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>7-8 用meta元素声明字符编码</title>
        <base href="http://titan/listings/" />
        <meta name="author" content="Adam Freeman" />
        <meta namej="description" content="A simple example" />
        <meta charset="utf-8" />
    </head>
    <body>
        <p>
            I like <code id="applecode">apples</code> and oranges.
        </p>
        <a href="http://apress.com">Visit Apress.com </a>
        <a href="page2.html">Page2</a>
        </body>
</html>
```
- 声明了这个页面采用UTF-8编码
- UTF-8编码能以最少的字节数表示所有Unicode字符，所以用得非常普遍

3. 模拟HTTP标头字段

##### 7-9 用meta元素模拟HTTP标头字段
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>7-9 用meta元素模拟HTTP标头字段</title>
        <base href="http://titan/listings/" />
        <meta name="author" content="Adam Freeman" />
        <meta name="description" content="A simple example" />
        <meta charset = "utf-8"/>
        <meta http-equiv="refresh" content="5"/>
    </head>
    <body>
        <p>
            I like <code id="applecode">apples</code> and oranges.
        </p>
        <a href="http://apress.com">Visit Apress.com </a>
        <a href="page2.html">Page2</a>
        </body>
</html>
```

- http-equiv属性的用途是指定所要模拟的标头字段名称，字段则由content属性指定
- 将标头字段refresh的值设置为"5"，其作用是让浏览器每隔5秒就再次载入页面
- 提示
  - 如果在刷新间隔时间值后加上一个分号再加上一个URL，那么浏览器在指定时间之后将载入指定的URL
- http-equiv属性有三个值可用 表7-10

##### 表 7-10 meta元素的http-equiv属性允许使用的值
属性值 | 说明
refresh | 以秒为单位指定一个时间间隔，在此时间过去之后将从服务器重新载入当前页面。也可以另行指定一个URL让浏览器载入。如`<meta http-equiv = "refresh" content="5"; http://www.apress.com/>`
default-style | 指定页面优先使用的样式表。对应的conent属性值应与同一文档中某个style元素或link元素的title属性值相同
content-type | 这是另一种声明HTML页面所用字符编码的方法。如`<meta http-equiv="content-type" conetent="text/html charset=UTF-8" />`

#### 7.2.4 定义CSS样式
- sytle元素可用来定义HTML文档内嵌的CSS样式(link元素则是用来导入外部样式表中的样式)

##### 表 7-11 style元素

类型 | 说明
:------ | :------ 
元素 | stype
元素类型 | 无
允许具有的父元素 | 任何可包含元数据元素的元素,包括head、div、noscript、 section、article、aside
局部属性 | type、media、 scoped
内容 | CSS样式
标签用法 | 开始标签和结束标签。内含文字
是否为HTML5新增 | 否
在HTML5中的变化 | scoped属性为HTML5中新增
习惯样式 | 无

##### 代码清单 7-10 使用style元素
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>7-10 使用style元素</title>
        <base href="http://titan/listings/" />
        <meta name="author" content="Adam Freeman" />
        <meta name="description" content="A simple example" />
        <meta charset = "utf-8"/>
        <style type="text/css">
        a {
            background-color: grey;
            color: white;
            padding: 0.5em;
            }
            </style>
    </head>
    <body>
        <p>
            I like <code id="applecode">apples</code> and oranges.
        </p>
        <a href="http://apress.com">Visit Apress.com </a>
        <a href="page2.html">Page2</a>
    </body>
</html>
```
- style元素可以出现在HTML文档中的各个部分
- 一个文档可包含多个style元素，因此不必把所有样式定义都塞进head部分
- 在使用模板引擎生成页面的情况下这个特性很有帮助

1. 指定样式类型
- type属性可以用来将所定义的样式类型告诉浏览器
- 但是浏览器支持的样式机制只有CSS一种，所以这个属性的值总是text/css

2. 指定样式作用范围
- 如果style元素中有scoped属性存在，那么其中定义的样式只作用于该元素的父元素及所有兄弟元素
- 要是不用scoped属性的话，在HTML文档中任何地方用style元素定义的样式将都作用于整个文档
- 警告: 在撰写此书时，尚无主流浏览器支持style元素的scoped属性

3. 指定样式适用的媒体
- media属性可用来表明文档在什么情况下应该使用该元素中定义的样式

##### 代码清单 7-11 使用style元素的media属性
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>7-11 使用style元素的media属性</title>
        <base href="http://titan/listings/" />
        <meta name="author" content="Adam Freeman" />
        <meta name="description" content="A simple example" />
        <meta charset = "utf-8"/>
        <style media = "screen" type="text/css">
        a {
            background-color: grey;
            color: white;
            padding: 0.5em;
        }
        </style>
        <style media = "print">
        a {
            color: Red;
            font-weight: bold;
            font-style: italic
            }
        </style>
    </head>
    <body>
        <p>
            I like <code id="applecode">apples</code> and oranges.
        </p>
        <a href="http://apress.com">Visit Apress.com </a>
        <a href="page2.html">Page2</a>
    </body>
```
- 代码中使用了两个style元素，它们有不同的media属性值
- 浏览器在屏幕上显示文档的时候使用的是第一个style元素中的样式，在打印文档的时候用得是第二个中的样式
- 样式的使用条件可以设计得非常细致
- 首先要确定的是所针对的设备类型 表7-12总结了有符合规定的值

##### 表7-12 供style元素的media属性用的规定设备值
设备 | 说明
:------ | :------
all | 将样式用于所有设备 (默认值)
aural | 将样式用于语音合成器
braille | 将样式用于盲文设备
handheld | 将样式用于手持设备
projection | 将样式用于投影机
print | 将样式用于计算机显示器屏幕
screen | 将样式用于计算机显示器屏幕
tty | 将样式用于电传打字机之类的等宽设备
tv | 将样式用于电视机

- 浏览器负责解释设备归类
- 核实一下所针对的浏览器对特定设备的解释与自己是否一致非常必要
- media还有一些特性可以用来设计更具体的使用条件

##### 代码清单 7-12 让style元素的对象更加具体

```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>7-12 让style元素的对象更加具体</title>
        <base href="http://titan/listings/" />
        <meta name="author" content="Adam Freeman" />
        <meta name="dexription" content="A simple example" />
        <meta charset="utf-8" />
        <style media="screen AND (max-width: 500px)" type="text/css">
            a {
                background-color: grey;
                color: white;
                padding: 0.5em;
            }
        </style>
        <style media="screen AND (min-width: 500px)" type="text/css" >
            a {
                color: Red;
                font-size: italic
            }
        </style>
        </head>
        <body>
            <p>
                I like <code id="applecode">apples</code> and oranges.
            </p>
            <a href="http://apress.com">Visit Apress.com </a>
            <a href="page2.html">Page 2</a>
        </body>
</html>
```
- 代码中使用media的width特性区分两组样式
- 浏览器窗口宽度小于500像素时使用的是第一组样式
- 窗口宽度大于500像素时使用的是第二组
- 注意此例中使用了AND来组合设备和特殊条件
- 除了AND，还可以使用NOT和表示OR的逗号(，
- 籍此可以为应用样式设计出复杂而又相当具体的条件
- width等特性通常会跟限定词min和max配合使用
- 不使用这些限定词，让样式的使用取决于非常精确的窗口尺寸也行，但是加上限定词会让条件变得更加灵活
- 表7-13罗列并介绍了可用的各种特性，若非特别说明，这些特性都可以用min=或max-修饰，构成阙指而不是精确值

##### 表 7-13 供style元素的media属性使用的特性
特性 | 说明 | 示例
width heigh | 指定浏览器窗口的宽度和高度。单位为px，代表像素 | width: 200px
device-width、device-height | 指定整个设备(而不仅仅是浏览器窗口)的宽度和高度。单位为px，代表像素 | min-device-height: 200px
resolution | 指定设备的像素密度。单位为dpi(点/英寸)或dpcm(点/厘米) | max-resolution: 600dpi
orientation | 指定设备的较长边朝向。支持的值有portrait和landscape。该特性没有设定词 | orientation: portrait
aspec-ratio、device-aspect-ratio | 指定浏览器窗口或整个设备的像素宽高比。其值表示为像素宽度与像素高度的比值 | min-aspect-ratio: 16/9
color monochrome | 指定彩色或黑白设备上每个像素占用的二进制位数 | min-monochrome: 2
color-index | 指定设备所能显示的颜色数目 | max-color-index: 236
scan | 指定电视的扫描模式。支持的值有progressive和interlace。该特性没有限定词 | scan: interlace
grid | 指定设备的类型。网络型设备使用固定的网络显示类容，例如基于字符的终端和单行显示的寻呼机。支持的值有0和1(1代表网络设备)。该特性没有限定词 | grid: 0

- 与指定设备的情况类似，这些特性也是由浏览器负责解释
- 如果要根据这些特性应用样式，请务必进行全面的测试，并且准备好预期特性不可用时改用的备用样式

#### 7.2.5 指定外部资源
- link元素可用来在HTML文档和外部资源(CSS样式表是最典型的情况)之间建立联系

##### 表7-14 link元素

类型 | 说明
:------ | :------ 
元素 | link
元素类型 | 元数据
允许具有的父元素 | head、 noscript
局部属性 | href、rel、hreflang、media、type、sizes
内容 | 无
标签用法 | 虚元素形式
是否为HTML5新增 | 否
在HTML5中的变化 | 新增了sizes属性。原来的charset、rev和target属性在HTML5中已不再使用
习惯样式 | 无

- link元素定义了6个局部属性，说明见表7-15
- 这些属性中最重要的是rel，它说明了HTML页与link元素所关联资源的关系类型

###### 表7-15 link元素的局部属性

属性 | 说明
href | 指定link元素指向的资源的URL
hreflang | 说明所关联资源使用的语言
media | 说明所关联的内容用于哪种设备。该属性使用的设备和特性值与表7-10和表7-11中介绍的相同
rel | 说明文档与所关联资源的关系类型
sizes | 指定图标的大小。本章后面有一个用link元素载入网站标志的例子
type | 指定所关联资源的MIME类型，如text/css、image/x-icon

- 为rel属性设定的值决定了浏览器对待link元素的方式
- 表7-16介绍了rel属性比较常用的一些值
- rel属性值最全面的介绍参见[地址](http://iana.org/assignments/link-relations/link-relations.xml)

##### 表7-16 link元素的rel属性值选编
值 | 说明
alternate | 链接到文档的替代版本，比如另一种语言的译本
author | 链接到文档的作者
help | 链接到当前文档的说明文档
icon | 指定图标资源，参见代码清单7-15示例
license | 链接到当前文档的相关许可证
pingback | 指定一个回探(pingback)服务器。从其他网站链接到博客的时候它能自动得到通知
prefetch | 预先获取一个资源，参见代码清单7-15示例
stylesheet | 载入外部样式表，参见代码清单7-14示例

1. 载入样式表
- styles.css样式表
```css
a {
    background-color: grey;
    color: white;
    padding: 0.5em;
}
```
###### 代码清单 7-14 用link元素载入外部样式表

```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>7-14 用link元素载入外部样式表</title>
        <base href="http://titan/listings/" />
        <meta name="author" conent="Adam Freeman" />
        <meta name="description" content="A simple example" />
        <meta charset = "utf-8" />
        <link rel="stylesheet" type="text/css" href='css/styles.css' />
    </head>
    <body>
        <p>
           I like <code id="applecode">apples</code> and oranges.
       </p>
       <a href="http://apress.com">Visit Apress.com </a>
       <a href="page2.html">Page 2</a>
   </body>
</html>
```
- 可以使用多个link元素载入多个外部资源
- 使用外部样式表的好处在于可让多个文档使用同一套样式而不必将这些样式复制到每一个文档中
- 浏览器会载入和应用其中的样式

2. 为页面定义网站标志
- 除了CSS样式表，link元素最常见的用处要算定义与页面联系在一起的图标
- 各种浏览器处理这种图标的方式有所不同，最常见的做法是将其显示在相应的标签页标签上或收藏夹中相应的项目前(如果用户收藏了这个页面的话)
- 图标是[Apress](www.apress.com)网站上使用的网站标志。32X32像素，格式为.ico，该图像的名叫favicon.ico

##### 代码清单7-15 用link元素添加网站标志
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>7-15 用link元素添加网站标志</title>
        <base href="http://titan/listings/" />
        <meta name="author" conent="Adam Freeman" />
        <meta name="description" content="A simple example" />
        <meta charset = "utf-8" />
        <link rel="stylesheet" type="text/css" href='css/styles.css' />
        <link rel="shortcut icon" href="logo/A.svg" type="image/x-icon" />
    </head>
    <body>
        <p>
           I like <code id="applecode">apples</code> and oranges.
       </p>
       <a href="http://apress.com">Visit Apress.com </a>
       <a href="page2.html">Page 2</a>
   </body>
</html>
```
- 这里要屏蔽`<base href="http://titan/listings/" />`
- 因为这是所有网页基点，css会被解析为: http://titan/listings/css/styles.css 就会解析不到


