## Chapter 3 -- 初探HTML (P11-P32)
______________________________________
### 表3-1 本章内容概要

问题 | 解决方案 | 代码清单
:------|:------|:------
标记文档内容 | 使用HTML元素 | 3-1 ~ 3-5
细调浏览器处理HTML元素的方式 | 把一个或多个属性应用到元素上 | 3-6 ~ 3-10
声明文档包含的是HTML内容 | 使用DOCTYPE和html元素 | 3-11
描述文档 | 使用head元素，其中包含一个或多个元数据元素(第七章) | 3-12
在HTML文档中添加内容 | 使用body元素, 其中包含文本内容和其他HTML元素 | 3-13
定义用于选择某个元素的快捷键 | 使用全局属性accesskey | 3-14
对元素进行分类，以便统一其样式或用程序查找该元素 | 使用全局属性class | 3-15 ~ 3-17
使元素的内容可被编辑 | 使用全局属性contenteditable | 3-18
为元素添加快捷菜单 | 使用全局属性contextmenu (目前尚无支持这个属性的浏览器)| --
指定元素内容的布局方向 | 使用全局属性dir | 3-19
声明元素可拖动 | 使用全局属性draggable (第37章) | --
声明可将其他元素拖放道某个元素上 | 使用全局属性dropzone (第37章) | --
表示某个元素及其内容毋需关注 | 使用全局属性hidden | 3-20
为元素分配一个独一无二的标识符，以便对其应用样式或用程序选择该元素 | 使用全局属性id | 3-21
声明元素内容所用语言 | 使用全局属性lang | 3-22
声明是否应检查元素内容的拼写错误 | 使用全局属性spellcheck | 3-23
直接定义元素的样式 | 使用全局属性style | 3-24
指定HTML文档中元素的Tab键次序 | 使用全局属性tabindex | 3-25
为元素提供额外信息(通常显示为工具提示) | 使用全局属性title | 3-26

_______________________________________
### 3.1 使用元素
#### 代码清单3-1 HTML元素示例
```html
I Like `<code>` apples `</code>` and oranges.
```
- 该元素分为三部分
- 其中有两部分称为标签(tag): 开始标签`<code>`和结束标签`</code>`
- 夹在两个标签之间的是元素的内容 (本例中为单词apples)。两个标签连同它们之间的内容构成code元素
元素是一种用来向浏览器说明文档内容的工具。其效果体现在内容之上。不同的元素有不同的确切含义。

提示: 元素名不区分大小写。今年来更常见得风格是全部使用小写。
注意: 浏览器不会显示元素的标签，它的任务是解读HTML文档，然后向用户呈现一个体现了HTML元素作用的视图。

#### 将内容与呈现分开
- 有些HTML元素会对呈现形式产生影响。浏览器遇到这种元素时，会改变向用户呈现文档内容的方式。code元素就是一例。
- 用HTML元素控制内容呈现形式的做法如今受到强烈反对。现在的观点是应该用HTML元素说明文档内容的结构和含义，用CSS控制内容呈现给用户的形式
- 会影响呈现形式的那些元素通常产生于HTML的早期版本。这些元素在浏览器中呈现时有默认的呈现样式，可以用CSS改变默认样式
_________________________________________
### 3.1.1 了解本章用到的元素
### 表3-2 元素摘要

元素 | 说明 | 所在章
:------|:------|:------
a | 生成超链接 | 8
body | 表示HTML文档的内容 | 7
button | 生成用以提交表单的按钮 | 12 
code | 表示计算机代码片段 | 8 
DOCTYPE | 表示HTML文档的开始 | 7 
head | 表示HTML文档的头部区域 | 7 
hr | 表示主题的改变 | 9 
html | 表示文档的HTML部分 | 7
input | 表示用户输入的数据 | 8 
label | 生成另一元素的说明标签 | 12
p | 表示段落 | 9 
style | 定义CSS样式 | 7
table | 表示用表格组织的数据 | 11 
td | 表示表格单元格 | 11
textarea | 生成用于获取用户输入数据的多行文本框 | 14 
th | 生成表头单元格 | 11 
title | 表示HTML文档的标题 | 7 
tr | 表示表格行 | 11

——————————————————————————————————————————————
### 3.1.2 使用空元素
- 没有内容的元素称为空元素， 代码清单3-2所示就是一例
#### 代码清单 3-2  空HTML元素
```html
I like <code></code> apples and oranges.
```
- 有些元素为空时没有意义(code就是其中之一)， 即便如此，它也是有效的HTML代码

______________________________________________
### 3.1.3 使用自闭合标签
- 空元素可以更简洁地只用一个标签标示
#### 代码清单 3-3 只用一个标签标示空元素  
```html
I like </code> apples and oranges.
```
- 将开始标签与结束标签合二为一。通常用来表示结束标签开始的斜杠符号(/)在此被放到标签的末尾
- 代码清单3-2与代码清单3-3中的元素等价，但只用一个标签的表示法更为简洁
______________________________________________
### 3.1.4 使用虚元素
- 有些元素只能用一个标签表示，在其中放置任何内容都不符合HTML规范。这类元素称为虚元素(void element)
- hr就是这样一个元素。它是一种组织性元素(第9章将介绍一些其他的这类元素)，用来表示内容中段落级别的终止。
- 虚元素有两种表示法。第一种只使用开始标签，如代码清单3-4；第二种表示法在此基础上加了一个斜杠符号，其形式与空元素一致，如代码清单3-5

#### 代码清单 3-4 用单个开始标签标示虚元素  
```html
I like apples and oranges.
<hr>
Today was warm and sunny.
```

#### 代码清单 3-5 用空元素结构表示虚元素  
```html
I like apples and oranges.
<hr />
Today was warm and sunny.
```
- 作者更喜欢第二中表示法
- hr元素也是一个具有呈现形式含义的元素，它会显示为一条横线(这也是其名称的由来)

#### 用不用非强制使用的开始和结束标签
- 许多HTML5元素在某些条件下可以省略其中一个标签。 例如: html元素的结束标签在此情况下就可以省略: "该元素后面没有紧跟着一条注释， 且该元素包含着一个非空或者其开始标签未曽省略的body元素"。(来自HTML5规范文档，w3c.org)

_______________________________________________
### 3.2 使用元素属性
- 元素可以用属性(attribute)进行配置

代码清单3-6所示为应用到a元素上的一个属性。这个属性元素用来生成超链接。点击超链接就会加载另一个HTML文档
#### 代码清单 3-6 使用元素属性
```html
I like <a href="/apples.html">apples</a> and oranges.
```
- 属性只能用在开始标签或单个标签上，不能用于结束标签。
- 属性具有名称和值两部分。
- href: 属性名； apples.html: 属性值
- 有一些全局属性可用于所有HTML元素。除了这些全局属性，元素还有用来提供特有配置信息的专有属性。
- href属性就限于a元素,它配置的是超链接的目的URL。a元素定义了一批专有属性。(第8章)
** 提示: ** 示例中使用双引号界定属性值(形如"属性值")，不过也可以用单引号(形如'属性值')。如果属性值本身含有引号，那么两种引号都要用到(形如"'含引号的'属性值"，或'"含引号的"属性值')

__________________________________________________
### 3.2.1 一个元素应用多个属性
- 一个元素可以应用多个属性，这些属性间以一个或几个空格分隔即可。见代码清单3-7

#### 代码清单 3-7 为一个元素设置多个属性
```html
I like <a class="link" href="/apples.html" id="firstlink">apples</a> and oranges.
```
- 这些属性的顺序未作要求， 全局属性和元素专有属性可随意交错。
- 其中class和id都是全局属性

__________________________________________________
### 3.2.2 使用布尔属性
- 有些属性属于布尔属性，这种属性不需要设定一个值，只消将属性名添加到元素中即可。 如代码清单3-8

#### 代码清单 3-8 布尔属性  
```html
Enter your name: <input disabled>
```

- 此例中布尔属性是disabled，元素中只添加了该属性的名称
- input元素为用户在HTML表单(第12章)中输入数据提供了一种手段。
- 添加disabled属性可以阻止用户输入数据
- 布尔属性有一点小古怪， 它以本来存在而不是用户为其设定的值对元素进行配置。
- 为布尔属性指定一个空字符串("")或属性名称字符串作为其值也有同样的效果  如代码清单3-9

#### 代码清单 3-9 为布尔属性指定空字符串值  
```html
Enter your name: <input disabled="">
Enter your name: <input disabled="disabled">
```

___________________________________________________
### 3.2.3 使用自定义属性
- 用户可自定义属性，这种属性必须以 data- 开头  代码清单3-10

#### 代码清单 3-10  
```html
Enter your name: <input disabled="true" data-creator="adam" data-purpose="collection">
```

- 这种属性的恰当名称是作者自定义属性， 有时也称扩展属性
- 自定义属性是对HTML4中"浏览器应当忽略不认识的属性"这种广泛应用的技巧的正式规定。
- 在这类属性名称之前添加前缀 data- 是为了避免与HTML的未来版本中可能增加的属性名冲突
- 自定义属性与CSS(第四章)和JavaScript(第5章)结合起来很有用

____________________________________________________
### 3.3 创建HTML文档
- 元素和属性不会孤立存在，它们是用来标记HTML文档内容的
- 创建一个HTML文档，最简单的方法是创建一个文本文件，并将其文件扩展名设置成为这类文件规定的.html
- 这个文件可以直接从磁盘载入浏览器，也可以从Web服务器载入
- HTML文档具有特定的结构，最起码要有一些关键性的元素

#### 浏览器和用户代理
- 在本章(及本书大部分章节中)，HTML文档都是针对浏览器创建的。
- 用于处理HTML文档的各种软件有一个共同的名称叫做用户代理(user agent)
- 浏览器是最流行的用户代理，但不是唯一的一种
- HTML内容并不是总是会被显示给用户看

#### HTML与XHTML的对比
- 符合HTML语法的文档不一定符合XML语法，因此用标准的XML解析程序处理HTML文档可能会遇到麻烦
- 为了解决这个问题， 可以使用XHTML， 它是HTML的XML序列化形式(以符合XML规范的方式来表达文档的内容以及HTML元素和属性，以便XML解析程序处理)
- 也可以创建既是有效HTML文档也是有效XML文档的多语文档(polyglot document)，不过这要求使用HTML语法的一个子集
- [XHTML](http://wiki.whatwg.org/wiki/HTML_vs._XHTML)

____________________________________________________
### 3.3.1 外层结构
- HTML文档的外层结构由两个元素确定: DOCTYPE和html   代码清单3-11

#### 代码清单 3-11 HTML文档的外层结构
```html
<!DOCTYPE HTML>
<html>
  <!-- elements go here -->
 </html>
```

- 上例中的DOCTYPE元素让浏览器明白其处理的是HTML文档。这是用布尔属性HTML表达的: <!DOCTYPE HTML>
- 紧跟DOCTYPE元素的是html元素的开始标签，它告诉浏览器:自此直到html结束标签，所以元素内容都应作为HTML处理
- 即使在文档中省略DOCTYPE和html元素，绝大多数浏览器仍会假定自己处理的是HTML文档
- 关于DOCTYPE和html元素详见第7章

______________________________________________________
### 3.3.2 元数据
- HTML文档的元数据部分可以用来向浏览器提供文档的一些信息。
- 元数据包含在head元素内部  代码清单3-12

#### 代码清单 3-12 在HTML文档中添加head元素  
```html
<!DOCTYPE HTML>
<html>
  <head>
    <!-- metadata goes here -->
    <title>Example</title>
  </head>
</html>
```
- 这个清单中的元数据只有title元素一项
- 按说HTML文档中都应该包含title元素，但是没有的话浏览器通常也不会在意
- 大多数浏览器把title元素的内容显示在其窗口的标题栏上或用来显示文档的标签页的标签位置上
- 第7章会详细说明head元素和title元，以及可以放在head元素中的所有其他元数据元素
- HTML文档中的注释的写法: 注释以标签`<!--开头, 以-->`结尾，浏览器会忽略这两个标签之间的一切内容
- 除了可包含用于说明HTML文档的元素，head元素还能用来规定文档与外部资源(如CSS样式表)的关系，定义内嵌CSS样式，放置和载入脚本程序 (第7章)

______________________________________________________
### 3.3.3 内容
- 文档的第三部分是文档内容，这也是最后一个部分，放在body元素之中   代码清单3-13

#### 代码清单 3-13 在HTML文档中添加body元素
```html
<!DOCTYPE HTML>
<html>
  <head>
  	  <!-- metadata goes here -->
  	  <title>Example</title>
  </head>
  <body>
  	  <!-- content and elements go here -->
  	  I like <code>apples</code> and oranges.
  </body>
</html>
```
- body元素告诉浏览器该向用户显示文档的哪个部分

_______________________________________________________
### 3.3.4 父元素、子元素、后代元素和兄弟元素
- HTML文档中元素之间有明确的关系
- 包含另一个元素的元素是被包含元素的父元素 代码清单3-13中body元素示code元素的父元素，这是因为code元素位于body元素的开始标签和结束标签之间。反过来说code元素是body元素的子元素。
- 一个元素可以拥有多个子元素，但只能有一个父元素
- 包含在其他元素中的元素也可以包含别的元素 代码清单3-13中可以看到: html元素包含着body元素， 而后者又包含着code元素。 body元素和code元素都是html元素的后代元素，但是二者中只有body元素才是html元素的子元素。
- 子元素示关系最近的后代元素。
- 具有同一个父元素的几个元素互为兄弟元素 代码清单3-13中: head元素和body元素就是兄弟元素，它们都是html元素的子元素
- 一个元素能以什么样的元素为父元素或子元素示有限制的，这些限制通过元素类型表现出来
- 圈定应用样式的元素的方法之一就要借助元素的父子关系
- 文档对象模型(DOM)也会涉及通过搜索文档树查找文档中某个元素，而文档树正是元素之间关系的一种表述
- 在HTML世界里， 从后代中辨认兄弟是一种重要能力

_______________________________________________________
### 3.3.5 了解元素类型
- HTML5规范将元素分为三大类: 元数据元素(metadata element)、流元素(flow element)和短语元素(phrasing element)
- 元数据元素用来构建HTML文档的基本结构，以及就如何处理文档向浏览器提供信息和指示
- 另外两种元素略有不同，它们的用途是确定一个元素合法的父元素和子元素范围。
- 短语元素示HTML的基本成分
- 流元素示短语元素的超集
- 所有短语元素都是流元素，但并非所有流元素都是短语元素
- 有些元素无法归入上述三种类型，这些元素要么没有什么特别的含义，要么只能用在一些非常有限的情况下
- li元素就是受限元素的一个例子。它表示列表项，只能有三种父元素: ol(表示有序列表)、ul(表示无序列表) 和menu(表示菜单)

________________________________________________________
### 3.4 使用HTML实体
- HTML文档中有些字符具有特殊含义--最明显的是<和>
- 有时需要在文档内容中用到这些字符，但不想让它们被当做HTML处理，为此应该使用HTML实体(entity)
- 实体是浏览器用来替代特殊字符的一种代码

#### 表3-3 常用HTML实体

字符 | 实体名称 | 实体编号
:------|:------|:------
< | &lt; | &#60; 
> | &gt; | &#62; 
& | &amp; | &#30;
 | &euro; | &#8364;
 | &pound; | &#163;
 | &sect; | &#167;
 | &copy; | &#169;
 | &reg; | &#174;
 | &trade; | &#8482;

- 每个特殊字符都有一个实体编号， 可以用来在文档内容中代表该字符。
- 特别常用的特殊字符还有对应的实体名称。 例如，对于浏览器来说， &#30；和&amp;是一回事

_________________________________________________________
### 3.5 HTML5全局属性
- 每种元素都能规定自己的属性，这种属性称为局部属性(local attribute)
- 每一个局部属性都可以用来控制元素独有行为的某个方面
- 属性还有另一种类型: 全局属性 (global attribute). 它们用来配置所有元素共有的行为。
- 全局属性可以用在任何一个元素身上，不过这不一定会带来有意义或有用的行为改变

_________________________________________________________
#### 3.5.1 accesskey属性
- 使用accesskey属性可以设定一个或几个用来选择页面上的元素的快捷键  代码清单3-14

#### 代码清单 3-14 使用accesskey属性
```html
<!DOCTYPE HTML>
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <form>
      Name: <input type="text" name="name" accesskey="n" />
      <p/>
      Password: <input typ="password" name="password" accesskey="p" />
      <p/>
      <input type="submit" value="Log In" accesskey="s" />
    </form>
  </body>
</html>
```
- 此例为三个input元素添加了accesskey属性
- 其目的是让网页或网站的熟客可以使用快捷键访问经常用到的元素。
- Windows系统上是同时按下Alt+n将键盘焦点转移到第一个input元素

_________________________________________________________
#### 3.5.2 class属性
- class属性用来将元素归类。这样做通常是为了能够找出文档中的某一类元素或为某一类元素应用CSS样式  代码清单3-15示范了如何使用class属性

### 代码清单 3-15 使用class属性 
```html
<!DOCTYPE HTML>
<html>
  <head>
    <title># 3-15: class</title>
  </head>
  <body>
  	 <a class="class1 class2" href="http://apress.com">Apress web site</a>
  	 <p/>
  	 <a class="class2 otherclass" href="http://w3c.org">W3C Web site</a>
  </body>
</html>
```
- 一个元素可以被归入多个类别，为此在class属性值中提供多个用空格分隔的类名即可
- 类名可以随便取，不过最好取点具有实际含义的，文档中拥有许多元素类别时尤其如此
- class属性本身没有任何作为
- class属性的一种利用方式是设计CSS样式时以所定义的一个或多个类作为应用目标 代码清单3-16

### 代码清单 3-16 定义依靠类起作用的样式 
```html
<!DOCTYPE HTML>
<html>
  <head>
    <title># 3-16: class_css</title>
    <style type="text/css">
        .class2 {
        	background-color: grey;
        	color: white;
        	padding: 5px;
        	margin: 2px;
        	}
        .class1 {
        	font-size: x-large;
        }
    </style>
  </head>
  <body>
  	  <a class="class1 class2" href="http://apress.com">Apress web site </a>
  	  <p/>
  	  <a class="class2 otherclass" href="http://w3c.org">W3C web site </a>
  </body>
</html>
```
- 用style定义了两条样式，第一条用于属于class2类的元素，第二条用于属于class1类的元素
- 脚本程序也可以利用class属性 代码清单3-17

### 代码清单 3-17 在脚本中使用class属性
```html
<!DOCTYPE HTML>
<html>
  <head>
    <title># 3-17: 在脚本中使用class属性</title>
  </head>
  <body>
  	 <a class="class1 class2" href="http://apress.com">Apress web site</a>
  	 <p/>
  	 <a class="class2 otherclass" href="http://w3c.org">W3C Web site</a>
  	 <script type="text/javascript">
  	     var elems = document.getElementsByClassName("otherclass");
  	     for (i = 0; i < elems.length; i++) {
  	     	var x = elems[i];
  	     	x.style.border = "thin solid black";
  	     	x.style.backgroundColor = "white";
  	     	x.style.color = "black";
  	     }
  	</script>
  </body>
</html>
```
- 此例中的脚本程序找出所有属于otherclass类的元素并对其设置了一些样式

___________________________________________________
#### 3.5.3 contenteditable属性
- contenteditable属性是HTML5中新增加的属性， 其用途是让用户能够修改页面上的内容 代码清单3-18

#### 代码清单 3-18 使用conenteditable属性
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 3-18 conenteditable</title>
    </head>
    <body>
    	<p contenteditable="true">It is raining right now</p>
    </body>
</html>
```
- 此例把contenteditable属性用在一个p元素身上。该属性值设置为true时用户可以编辑元素内容，设置为false时则禁止编辑。
- 如果未设定其值，那么元素会从父元素处继承该属性的值。

__________________________________________________
#### 3.5.4 contextmenu属性
- contextmenu属性是用来为元素设定快捷菜单。这种菜单会在受到触发的时候(例如:Windows用户用鼠标右击时)弹出来（出本书时，尚无支持该属性的浏览器）

___________________________________________________
#### 3.5.5 dir属性
- dir属性用来规定元素中文字的方向
- 其有效值有两个: ltr(用于从左到右的文字)和rtl(用于从右到左的文字)  代码清单3-19

#### 代码清单 3-19 使用dir属性
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title># 3-19 dir属性</title>
    </head>
    <body>
        <p dir="rtl">This is right-to-left</p>
        <p dir="ltr">This is left-to-right</p>
    </body>
</html>
```

___________________________________________________
#### 3.5.6 draggable属性
- draggable属性是HTML5支持拖放操作的方式之一，用来表示元素是否可被拖放。 (第37章)

___________________________________________________
#### 3.5.7 dropzone属性
- dropzone属性是HTML5支持拖放操作的方式之一，与draggable属性搭配使用。 (第37章)

___________________________________________________
#### 3.5.8 hidden属性
- hidden是个布尔属性，表示相关元素当前毋需关注。浏览器对它的处理方式是隐藏相关元素。  代码清单3-20

#### 代码清单 3-20 使用hidden属性
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title># 3-20 使用hidden属性</title>
      <script>
          var toggleHidden = function() {
          	var elem = document.getElementsById("toggle");
          	if (elem.hasAttribute("hidden")) {
          		elem.removeAttribute("hidden");
          	} else {
          		elem.setAttribute("hidden", "hidden");
          	}
          }
     </script>
    </head>
    <body>
     	 <button onclick="toggleHidden()">Toggle</button>
     	 <table>
     	 	<tr>
     	 		<th>Name</th>
     	 		<th>City</th>
     	 	</tr>
     	 	<tr>
     	 		<td>Adam Freeman</td>
     	 		<td>London</td>
     	 	</tr>
     	 	<tr id="toggle" hidden>
     	 		<td>Joe Smith</td>
     	 		<td>New York</td>
     	 	</tr>
     	 	<tr>
     	 		<td>Anne Jones</td>
     	 		<td>Parise</td>
     	 	</tr>
     	 </table>
    </body>
</html>
```
- 文档中有一个table元素，它包含的一个tr元素(代表表格中的一行)设置了hidden属性。
- 文档中还有一个button元素，按下它所代表的按钮将会调用定义在script元素中的JavaScript函数toggleHidden。
- 这段脚本程序的作用是: 如果那个tr元素的hidden属性存在就将其删除，否则就添加该属性。
- 把hidden属性应用到一个元素之后，浏览器干脆不去显示该元素，仿佛HTML文档中没有这个元素。

_____________________________________________________
#### 3.5.9 id属性
- id属性用来给元素分配一个唯一的标识符。
- 这种标识符通常用来将样式应用到元素上或在JavaScript程序中用来选择元素

#### 代码清单 3-21 使用id属性
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 3-21 使用id属性</title>
    </head>
    <style>
        #w3clink {
        	background: grey;
        	color: white;
        	padding: 5px;
        	border: thin solid black;
        }
    </style>
    <body>
    	<a href="http://apress.com">Apress web site</a>
    	<p/>
    	<a id="w3clink" href="http://w3c.org">W3C web site</a>
    </body>
</html>
```
- 为了根据id属性值应用样式，需要在定义样式时使用一个以#号开头后接id属性值得选择器(selector)

** 提示:**
- id属性还可以用来导航到文档中的特定位置。
- 倘若有个名为example.html的文档中包含一个id属性值为myelement的元素，那么使用example.html#myelement这个URL即可直接导航至该元素。该URL的末尾部分(#加上元素id值)称为URL片段标识符(fragment identifier)

______________________________________________________
#### 3.5.10 lang属性
- lang属性用于说明元素内容使用的语言  代码清单3-22

#### 代码清单 3-22 使用lang属性
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 3 - 22 使用lang属性</title>
    </head>
    <body>
    	<p lang="en">Hello - how are you?</p>
    	<p lang="fr">Bonjour -comment etes-vous?</p>
    	<p lang="es">Hola -como estas</p>
    </body>
</html>
```

- lang属性值必需使用有效的ISO语言代码。
- 关于如何声明语言的全面说明可参阅这个网址: http://tools.ietf.org/html/bcp47
- 使用lang属性的目的是让浏览器调整其表达元素内容的方式。比如说: 改变使用的引号，在使用了文字朗读器(或别的残障辅助技术)的情况下正确发音
- lang属性还可以用来选择指定语言的内容，一遍只显示用户所选语言的内容或对其应用样式

______________________________________________________
#### 3.5.11 spellcheck属性
- spellcheck属性用来表明浏览器是否应该对元素的内容进行拼写检查
- 这个属性只有用在用户可以编辑的元素上时才有意义  
- 代码清单3-23

#### 代码清单 3-23 使用spellcheck属性
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 3-23 使用spellcheck属性</title>
    </head>
    <body>
    	<textarea spellcheck="true">This is some mispelled text</textarea>
    </body>
</html>
``` 
- spellcheck属性可以接受的值有两个: true(启用拼写检查)和false(禁用拼写检查)
- 拼写检查的实现方式则因浏览器而异

** 警告 ** 目前大多数浏览器中的拼写检查都会忽略前面介绍过的lang属性。它们的拼写检查基于用户所用操作系统中的语言设置或浏览器的语言设置

________________________________________________________
#### 3.5.12 style属性
- style属性用来直接在元素上定义CSS样式(这是在style元素或外部样式表中定义样式之外的一种选择)
- 代码清单3-24

#### 代码清单 3-24 使用style属性
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 3-24 使用style属性</title>
    </head>
    <body>
    	<a href="http://apress.com" style="background: grey; color: white; padding:10px">Visit the Apress site </a>
    </body>
</html>
```
______________________________________________________
#### 3.5.13 tabindex属性
- HTML页面上的键盘焦点可以通过按Tab键在各元素之间切换。
- 用tabindex属性可以改变默认的转移顺序
- 代码清单3-25

#### 代码清单 3-25 使用tabindex属性
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 3-25 使用tabindex属性</title>
    </head>
    <body>
    	<form>
    		<label>Name: <input type="text" name="name" tabindex="1"/></label>
    		<p/>
    		<label>City: <input type="text" name="city" tabindex="-1"/></label>
    	    <p/>
    	    <label>Country: <input type="text" name="country" tabindex="2"/></label>
    	    <p/>
    	    <input type="submit" tabindex="3"/>
    	</form>
    </body>
</html>
```
- tabindex为1的元素会第一个被选中。用户按一下Tab键后，tabindex值为2的那个元素会被选中，依次类推。
- tabindex设置为-1的元素不会再用户按下Tab键后被选中。

___________________________________________________
#### 3.5.14 title属性
- title属性提供了元素的额外信息
- 浏览器通常用这些东西显示工具提示
- 代码清单3-26

#### 代码清单 3-26 使用title属性
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 3-26 title属性</title>
    </head>
    <body>
    	<a title="Apress Publishing" href="http://apress.com">Visit the Apress site</a>
    </body>
</html>
```

_____________________________________________________
### 3.6 有用的HTML工具
- 一款优秀的HTML编辑软件。应该能够将无效元素和属性突出显示出来
- 大多数浏览器菜单中都有的"查看源代码"

______________________________________________________
### 3.7 小结
- 跑马观花的介绍了HTML文档的结构和特性，示范了如何用HTML元素标记内容以创建一个HTML文档
- 可以了解到如何使用属性配置浏览器处理元素的方式，以及局部和全局属性的差别
- 介绍了所有全局属性，并且简要说明了用以标记HTML文档的基本元素和结构