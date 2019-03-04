## Chapter 4 -- CSS初探 (P33-P59)
______________________________________
### CSS(层叠样式表) 用来规定HTML文档的呈现形式(外观和格式编排)
______________________________________
#### 表 4-1 本章内容概要

问题 | 解决方案 | 代码清单
:------ | :------ | :------
定义样式 |  使用属性/值声明 | 4-1
将样式直接应用于元素 | 用style属性创建元素内嵌样式 | 4-2
创建可用于多个元素的样式 | 使用style元素，编写一个选择器和一组样式声明 | 4-3、4-4 
创建可用于多个HTML文档的样式 | 创建一个外部样式表文件，并用link元素引用它 | 4-5 ~ 4-9 
确定元素将使用什么样式属性 | 对样式来源适用层叠规则，同级样式发生冲突时计算并比较样式的具体程度 | 4-10 ~ 4-12 、4-14 ~ 4-16 
改变正常的样式层叠次序 | 使用重要样式 | 4-13 
使用父元素的样式属性 | 使用属性继承 | 4-17、4-18 
根据一条属性确定另一条属性的值 | 使用相对度量单位 | 4-19 ~ 4-23 
动态计算属性值 | 使用calc函数 | 4-24

______________________________________
### 4.1 定义和应用样式
- CSS样式由一条或多条以分号隔开的样式声明组成
- 每条声明包含着一个CSS属性和该属性的值，二者以冒号分隔
- 代码清单 4-1

#### 代码清单 4-1 一条简单的CSS样式
```css
background-color: grey; color: white
```
- background-color:grey; -->声明
  - background-color --> 属性
  - grey --> 值
- color：white --> 声明
  - color --> 属性
  - white --> 值
- 这个例子中的样式含有两条样式声明。第一条将background-color属性的值设置为grey，第二条将color属性的值设置为white
_____________________________________
#### 4.1.1 了解本章所用的CSS属性

#### 表 4-2 CSS属性摘要

属性 | 说明 | 所在章
:------ | :------ | :------
background-color |  设置元素的背景颜色 | 19
border | 设定围绕元素的边框 | 19
color | 设置元素的前景颜色 | 24
font-size | 设置元素文字的字号 | 22
height | 设置元素高度 | 20
padding | 设定元素内容与边框之间的间距 | 20
text-decoration | 设置元素文字的装饰效果，如本章用到的下划线 | 22
width | 设置元素宽度 | 20
_____________________________________
#### 4.1.2 使用元素内嵌样式
- 样式不是定义了就了事，它还需要被应用，也即告诉浏览器它要影响哪些元素。
- 把样式应用到元素身上的各种方式中，最直接的是使用全局属性style
- 代码清单4-2

#### 代码清单4-2 用全局属性style定义样式
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 4-2 用全局属性style定义样式</title>
    </head>
    <body>
    	<a href="http://apress.com" style="background-color:grey; color:white">
    	Visit the Apress Website
        </a>
        <p>I like <span>apples</span> and oranges. </p>
        <a href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 这个HTML文档中有4个内容元素: 两个超链接(用a元素生产)， 一个p元素以及包含在其中的一个span元素
- 例中用全局属性style将样式应用到第一个a元素(链接到Apress网站)。style属性只影响它所属的元素
- background-color属性和color属性分别设置元素的背景和前景颜色
_________________________________
#### 4.1.3 使用文档内嵌样式
- 用style元素(而不是style属性)定义文档内嵌样式，通过CSS选择器指示浏览器应用样式
- 代码清单4-3

#### 代码清单4-3 使用style元素
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 4-3 使用style元素</title>
    	<style type="text/css">
    	a {
    		background-color:grey;
    		color:white;
    	}
    	</style>
    </head>
    <body>
    	<a href="http://apress.com">Visit the Apress websie</a>
    	<p>I Like <span>apples</span>and oranges.</p>
    	<a href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 它们被包在一对花括号之间，并且跟在一个选择器之后
```html
<style type="text/css">
    	a {
    		background-color:grey;
    		color:white;
    	}
    	</style>
```
- a --> 选择器
- background-color:grey; color:white; --> 声明
- 本例中的选择器为a，它指示浏览器将样式应用到文档中的每一个a元素

- 一个style元素中可以定义多条样式，为此只消不断重复定义一个选择器和一套样式声明的过程即可 
- 代码清单4-4

#### 代码清单4-4 在一个style元素内定义多条样式
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 4-4 在一个style元素内定义多条样式</title>
    	<style type="text/css">
          a {
          	background-color: grey;
          	color:white
          }
          span {
          	border: thin black solid;
          	padding: 10px;
          }
      </style>
  </head>
  <body>
  	<a href="http://apress.com">Visit the Apress website</a>
  	<p>I Like <span>apples</span> and oranges.</p>
  	<a href="http://w3c.org">Visit the W3C website</a>
  </body>
</html>
```
- 本例新增样式的选择器为span(表示浏览器将把样式应用到文档中所有span元素上，实现border和padding属性所规定的效果)
- border属性设置的是围绕目标元素的边框
- padding属性控制的是目标元素与边框之间的间距
__________________________________________________
#### 4.1.4 使用外部样式表
- 如果调样式要用于多个HTML文档，那么与其在每一个文档中重复定义相同的样式，不如另外创建一个独立额样式表
- 这种文件按惯例以.css为文件扩展名，其中包含着用户的样式定义
- 代码清单 4-5

#### 代码清单 4-5 文件styles.css
```css
a {
	background-color:grey;
	color: white
}
span {
	border: thin black solid;
	padding: 10px;
}
```
- HTML文档就可以用link元素将这些样式导入其中

#### 代码清单 4-6 导入外部样式表
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 4-6 导入外部样式表</title>
    	<link rel="stylesheet" type="text/css" href="styles.css"></link>
    </head>
    <body>
    	<a href="http://apress.com">Visit the Apress website</a>
    	<p>I like <span>apples</span> and oranges.</p>
    	<a href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 文档想要链接多少样式表都行，为每一个样式表使用一个link元素即可
- 如果不同样式表中的样式使用了相同的选择器，那么这些样式表的导入顺序很重要，在此情况下得以应用的是后导入的样式

1. 从其他样式表中导入样式
- 可以用@import语句将样式从一个样式表导入另一个样式表。
- 代码清单4-7

#### 代码清单4-7 文件combined.css
```css
@import "css/styles.css";
span {
	border: medium black dashed;
	padding: 10px;
}
```
- 一个样式表中想要导入多少别的样式表都行，为每一个样式表使用一条@import语句即可
- @import语句必须位于样式表顶端，样式表自己的样式定义不能出现在它之前
- 在combined.css这个样式表中，先导入了styles.css，然后再定义了一条针对span元素的新样式。
- 代码清单 4-8

#### 代码清单 4-8 链接到一个包含有导入语句的样式表
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title># 4-8 链接到一个包含有导入语句的样式表</title>
    	<link rel="stylesheet" type="text/css" href="css/combined.css"/>
    </head>
    <body>
    	<a href="http://apress.com">Visit the Apress website</a>
    	<p>I like <span>apples</span> and oranges.</p>
    	<a href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- combined.css中的@import语句导入了styles.css中定义的两条样式，其中应用于span元素的那条样式又被combined.css中定义的具有相同选择器的样式盖过
- @import语句用得并不广泛，不少人并不知道有这个东西
- 浏览器处理@import语句的效率往往不如处理多个link元素并靠样式层叠解决问题

2. 声明样式表的字符编码
- 在CSS样式表中可以出现在@import语句之前的只有@charset语句
- @charset用于声明样式表使用的字符编码

#### 代码清单4-9 声明样式表使用的字符编码类型
```css
@charset "UTF-8";
@import "styles.css"
span {
	border: medium black dashed;
	padding: 10px;
}
- 如果样式表中未声明所使用的字符编码，那么浏览器将使用载入该样式表的HTML文档声明的编码。
- 要是HTML文档中也没有声明其编码，那么默认情况下使用的是UTF-8
```
_________________________________________________
### 4.2 样式的层叠和继承
- 要想掌握样式表，弄清样式层叠和继承这两个概念是关键
- 浏览器根据层叠和继承规则确定显示一个元素时各种样式属性采用的值
- 每个元素都有一套浏览器呈现页面时要用到的CSS属性
- 对于每一个这种属性，浏览器都需要查看一下其所有的样式来源。
- 三中定义样式的方式: 元素内嵌、文档内嵌、外部样式表
- 样式还有另外两个来源: 浏览器样式、用户样式
_________________________________________________
#### 4.2.1 浏览器样式
- 浏览器样式(更恰当的名称是用户代理样式)是元素尚未设置样式是浏览器应用在它身上的默认样式
- 这些样式因浏览器而略有差异，不过大体一致

#### 代码清单 4-10 不含样式的HTML文档
```html
<!DOCTYPE HTML>
<html>
    <head>
    	<title>#4-10 不含样式的HTML文档</title>
    </head>
    <body>
    	<a href="http://apress.com">Visit the Apress website</a>
    	<p>I like <span>apples</span> and oranges.</p>
    	<a href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 去掉了所有样式
- 链接的文字内容被显示为蓝色，而且带有下划线
- 依次推测，浏览器相当于应用了类似代码清单 4-11

#### 代码清单 4-11 推测出来的a元素的默认浏览器样式
```css
a {
	color: blue;
	text-decoration: underline;
}
```
- 不是每一个HTML元素都有默认的浏览器样式，但是大多数元素都有

___________________________________________________
#### 4.2.2 用户样式
- 大多数浏览器都允许用户定义自己的样式表。这类样式表中包含的样式称为用户样式。
- 这个功能用的人不多
- 那些要定义自己的样式表的人往往比较看重这一点，一个特别的原因是这可以让有生理不便的人更容易使用网页
- 各种浏览器都有自己管理用户样式的方式
- Chrome: 用户的个人配置信息目录中生成一个名为Default\User StyleSheets\Customer.css的文件，添加到这个文件中的任何样式都会被用于用户访问的所有网站，只不过要依下节所讲的层叠规则行事

____________________________________________________
#### 4.2.3 样式如何层叠
- 浏览器要显示元素时求索一个CSS属性值的次序
  1. 元素内嵌样式(用元素的全局属性style定义的样式)
  2. 文档内嵌样式(定义在style元素中的样式)
  3. 外部样式(用link元素导入的样式)
  4. 用户样式(用户定义的样式)
  5. 浏览器样式(浏览器应用到的默认样式)
- 三个属性来源: 元素内嵌样式、文档内嵌样式、外部样式表合称作者样式
- 定义在用户样式表中的样式表称为用户样式
- 由浏览器定义的样式则称为浏览器样式

____________________________________________________
#### 4.2.4 用重要样式调整层叠次序
- 把样式属性值标记为重要(important)，可以改变正常的层叠次序

##### 代码清单 4-13 将样式属性标记为重要
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title># 4-13 将样式属性标记为重要</title>
      <style type="text/css">
          a {
            color: black !important;
            }
      </style>
    </head>
    <body>
      <a style="color:red" href="http://apress.com">Visit the Apress website</a>
      <p>I like <span>apples</span>and oranges.</p>
      <a href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 在样式声明后附上!important即可将对应属性值标记为重要
- 不管这种样式属性定义在什么地方，浏览器都会给予优先考虑
- 提示: 能凌驾于作者定义的重要属性值之上的只有用户样式表中定义的重要属性值。对于普通属性，作者样式中的值优先于用户样式中的值，而对于重要属性情况正好相反

_________________________________________________
#### 4.2.5 根据具体程度和定义次序解决同级样式冲突
- 如果有两条定义同一层次的样式都能应用于同一个元素，而且它们都包含着浏览器要查看的CSS属性值，这时就需要判断了。浏览器会评估两条样式的具体程度，然后选中较为特殊的那条
- 通过统计三类特征得出:
  1. 样式的选择器看id值的数目
  2. 选择器中其他属性和伪类的数目
  3. 选择器中元素名和伪元素的数目
- 代码清单 4-14

#### 代码清单 4-14 样式的具体程度
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title># 4-14 样式的具体程度</title>
      <style type="text/css">
        a {
          color: black;
        }
        a.myclass {
          color: white;
          background: grey;
        }
      </style>
    </head>
    <body>
      <a href="http://apress.com">Visit the Apress website</a>
      <p> I like <span>apples</span> and oranges.</p>
      <a class="myclass" href= "http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 评定具体程度时要按a-b-c的形式(其中每一个字母依次代表上述三类特征的统计结果)生产一个数字。它不死一个三位数。如果对某个样式算出的a值最大，那么它就是具体程度高的那个
- 只有a值相等，才会比较b值。b值相等，才会比较c值
- 1-0-0比0-5-5这个得分代表的具体程度更高
- 本例中 a.myclass这个选择器含有一个class属性，于是该样式的值为0-1-0(0个id值+1个其他属性+0个元素名)
- 另一条样式的具体程度值为0-0-0(因为它不包含id值、其他属性或元素名)。因此浏览器在呈现被归入myclass类的a元素时将使用a.myclass样式中设定的color属性值
- 对于所有其他a元素，使用的则是另一条样式中设定的值
- 如果同一个样式属性出现在具体程度相当的几条样式中，那么浏览器无法根据其位置的先后选择所用的值，规则是后来者居上 代码清单 4-15

#### 代码清单 4-15 具体程度相同的样式
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>4-15 具体程度相同的样式</title>
      <style type="text/css">
          a.myclass1 {
              color: black;
            }
          a.myclass2 {
            color: white;
            background: grey;
            }
      </style>
    </head>
    <body>
      <a href="http://apress.com">Visit the Apress website</a>
      <p>I like <span>apples</span> and oranges.</p>
      <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 此例style元素中定义的两条样式在具体程度上得分相同
- 浏览器在呈现页面上的第二个a元素时，为样式属性color选用的值时white,这是因为该值来自靠后的那条样式
- 代码清单 4-16 颠倒了两条样式的位置

#### 代码清单 4-16 颠倒样式定义的次序
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>4-16 颠倒样式定义的次序</title>
      <style type="text/css">
      a.myclass2 {
        color: white;
        background:grey;
      }
      a.myclass1 {
        color:black;
      }
    </style>
  </head>
  <body>
    <a href="http://apress.com">Visit the Apress website</a>
    <p>I like <span>apples</span> and oranges.</p>
    <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a>
  </body>
</html>
```
- 现在浏览器为color属性选择的是black这个值
- 根据样式的具体程度和定义次序确定选用的样式属性值，应该把各个属性分开考虑
- 这几个例子当中还定义了背景颜色属性的值。因为该值并非两个样式中都有，所有不会发生冲突，也就没有必要查找其他值

___________________________________________
#### 4.2.6 继承
- 如果浏览器在直接相关的样式中找不到某个属性的值，就会求助于继承机制，使用父元素的这个样式属性值

#### 代码清单 4-17 CSS属性继承
```html
<!DOCTYPE HTML>
<html>
    <head><title>4-17 CSS属性继承</title>
      <style type="text/css">
      p {
        color: white;
        background:grey;
        border: medium solid black;
      }
      </style>
    </head>
    <body>
      <a href="http://apress.com">Visit the Apress website</a>
      <p>I like <span>apples</span> and oranges. </p>
      <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 浏览器应用于span元素(其父元素为p)的样式
- 这个文档并没有在针对span元素的样式中设定color属性值，但是浏览器显示该元素的文字内容时却使用了前景色white。这个值系由父元素p继承而来
- 并非所有CSS属性均可继承。这方面的经验: 与元素外观(文字颜色、字体等)相关的样式会被继承；与元素在页面上的布局相关的样式不会被继承。在样式中使用inherit这个特别设立的值可以强行实施继承，明确指示浏览器在该属性上使用父元素样式中的值
- 代码清单 4-18

#### 代码清单 4-18 使用inherit
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>4-18 使用inherit</title>
      <style type="text/css">
      p {
        color:white;
        background:grey;
        border: medium solid black;
      }
      span {
        border: inherit;
      }
    </style>
  </head>
  <body>
    <a href="http://apress.com">Vistit the Apress website</a>
    <p>I like <span>apples</span> and oranges.</p>
    <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a>
  </body>
</html>
```
- 这个例子定义了一条用于span元素的样式，其border属性值继承自父元素

____________________________________
### 4.3 CSS中的颜色
- 在CSS中设置颜色有好几种方法。
  - 最简单的办法是使用规定的颜色名称，或者设置红、绿、蓝三种颜色成分的值(十进制或十六进制)
  - 设置颜色成分值时，十进制值以逗号分隔，十六进制前面通常要加上一个#符号(比如:#ffffff,它代表白色)
- 表4-3罗列了一些规定的颜色名称及其十进制
- [颜色完整列表](http://www.w3.org/TR/css3-color)
- 表4-4列出了一组可用的灰色派生色

#### 表4-3 CSS颜色选编
颜色名称 | 十六进制表示 | 十进制表示
:------ | :------ | :------
black | #000000 | 0,0,0
silver | #C0C0C0| 192,192,192 
gray | #808080 | 128,128,128
white | #FFFFFF | 255,255,255
maroon | #800000 | 128,0,0
red | #FF0000 | 255,0,0
purple | #800080 | 128,0,128
fushia | #FF00FF | 255,0,255
green | #008000 | 0,128,0
lime | #00FF00 | 0,255,0
olive | #808000 | 128,128,0
yellow | #FFFF00 | 255,255,0
navy | #000080 | 0,0,128
blue | #0000FF | 0,0,255
teal | #008080| 0,128,128
aqua | #00FFFF | 0,255,255

#### 表4-4 CSS颜色选编
 颜色名称 | 十六进制表示 | 十进制表示
:------ | :------ | :------
darkgray | #a9a9a9 | 169,169,169
darkslategray | #2f4f4f | 47,79,79 
dimgray | #696969 | 105,105,105
gray | #808080 | 128,128,128 
lightgray | #d3d3d3 | 211,211,211 
lightslategray | #778899 | 119,136,153
slategray | #708090 | 112,128,144

#### 表示更复杂的颜色
- 颜色名称和简单的十六进制数不甚表示颜色的唯一方式。CSS中还可以用一些函数选择颜色

#### 表4-5 CSS颜色函数
函数 | 说明 | 示例
:------ | :------ | :------
rgb(r,g,b)| 用RGB模型表示颜色| color:rgb(112,128,144)
rgba(r,g,b,a)| 用RGB模型表示颜色，外加一个用于表示透明度的a值(0标识全透明，1代表完全不透明)| color: rgba(112,128,144,0.4)
hsl(h,s,l) | 用HSL颜色模型(色相[hue]、饱和度[saturation]和明度[lightness])表示颜色 | color: hsl(120,100%,22%)
hsla(h,s,l,a) | 与HSL模式类似，只不过增加了一个表示透明度的a值 | color: hsla(120，100%，22%，0.4)

#### 4.4 CSS中的长度
- 许多CSS属性要求为其设置长度值
- width属性和font-size属性就是这方面的例子，width设置元素的宽度，font-size设置元素内容的字号
- 代码清单 4-19

##### 代码清单 4-19 为属性设置长度值
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>4-19 为属性设置长度值</title>
      <style type="text/css">
      p {
        background: grey;
        color:white;
        width: 5cm;
        font-size: 20pt;
        }
      </style>
    </head>
    <body>
      <a href="http://apress.com">Visit the Apress</a>
      <p>I like <span>apples</span> and organes.</p>
      <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
_______________________________________
#### 4.4.1 绝对长度
- 代码清单中使用的cm和pt这两个单位都属于绝对单位
- 这类单位是现实世界的度量单位
- CSS支持五中绝对单位

##### 表 4-6 CSS中的绝对单位
单位标识符 | 说明 
:------ | :------ 
in | 英寸
cm | 厘米
mm | 毫米
pt | 磅(1磅等于1/72英寸)
pc | pica(1pica等于12磅)

- 一条样式中可以混合使用多种单位，包括混合使用绝对单位和相对单位
- 如果能预先知道内容的呈现方式，那么绝对单位很有用处
- 相对单位更灵活、更容易管理

#### 4.4.2 相对长度
- 相对长度的规定和实现都比绝对长度更复杂、需要以严密、精确的语言明确定义
- 相对单位的测量需要依托其他类型的单位

##### 表 4-7 CSS相对单位
单位标识符 | 说明 
:------ | :------ 
em | 与元素字号挂钩 
ex | 与元素字体的"x高度"挂钩
rem | 与根元素的字号挂钩
px | CSS像素(假定显示器的分辨率为96dpi)
% | 另一属性的值得百分比
________________________________________________
- 如何用这些单位表示长度
1. 与字号挂钩的相对单位
- 使用相对单位时所设置的实际上是另一种度量值得倍数
- 代码清单 4-20
##### 代码清单 4-20 使用相对单位

```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>4-20 使用相对单位</title>
      <style type="text/css">
      p {
        background: grey;
        color: white;
        font-size: 15pt;
        height: 2em;
        }
      </style>
    </head>
    <body>
      <a href="http://apress.com">Visit the Apress website</a>
      <p>I like <span>apples</span> and oranges.</p>
      <p style= "front-size:12pt">I also like mangos and cherries.</p>
      <a class= "myclass1 myclass2" href="http://w3c.org">Vistit the W3C website</a>
    </body>
</html>
```
- 本例将height属性值设置为2em，意思是p元素在屏幕上显示出来的高度应为字号的两倍
- 这个倍数是在显示每个元素的时候计算出来的。
- 本例在style元素中为p元素的font-size设置了默认值15pt，然后又在文档中第二个p元素的内嵌样式例将该属性值设置为12pt

- 相对单位还可以用来表示另一个相对单位的倍数
- 代码清单 4-12
- height属性值使用的单位时em，这个单位时从font-size属性值推算出来的，而font-size属性值在此使用的单位时rem

##### 代码清单 4-12 使用另一相对单位推算出来的相对单位
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>4-21 使用另一相对单位推算出来的相对单位</title>
      <style type="text/css">
      html {
        font-size: 0.2in;
      }
      p {
        background-color: grey;
        color: white;
        font-size: 2rem;
        height: 2em;
      }
    </style>
  </head>
  <body style="font-size: 14pt">
    <a href="http://apress.com">Visit the Apress website</a>
    <p>I like <span>apples</span> and oranges.</p>
    <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a>
  </body>
</html>
```

- rem单位根据html(文档的根元素)的字号而定
- 本例用一条文档内嵌样式(使用直接在html元素的style属性中定义的元素内嵌样式也行)将html元素的字号设置为0.2英寸(这是一个绝对单位)
- 在另一条样式中， font-size属性值被设置为2rem，这表示使用该值得所有元素的字号将是根元素字号的两倍--0.4英寸,这条样式中的height属性被设置为2em，于是p元素在浏览器中将以0.4英寸的字号显示，其高度则是0.8英寸
- 第三个与字体相关的相对单位是ex。这个单位指的是当前字体的x高度，也即字体基线到中线之间的距离，一般与字母x的高度相当，通常1ex大致等于0.5em

2. 像素单位的问题
- 像素这个术语一般是指显示设备上可寻址的最小单元--图像的基本元素
- CSS却是另辟蹊径，其像素定义如下: 参考像素是距读者一臂之遥的像素密度为96dpi的设备上一个像素的视角(visual angel)
- 好在主流浏览器都没有理会CSS定义的像素和显示设备的像素之间的差别，它们将1像素视为1英寸的1/96(这是Windows系统的标准像素密度。有些平台的显示设备具有不同的像素密度，它们的浏览器通常要做些转换工作，让1像素仍然大约等于1英寸的1/96)
- CSS像素的完整定义参见www.w3.org/TR/CSS21/syndata.html#length-units

#### 代码清单 4-22 在样式中使用像素单位
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>4-22 在样式中使用像素单位</title>
      <style type="text/css">
      p {
        background: grey;
        color: white;
        font-size: 20px;
        width: 200px;
      }
    </style>
  </head>
  <body>
    <a href="htp://apress.com">Visit the Apress website</a>
    <p>I like <span>apples</span> and oragnes. </p>
    <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website"</a>
  </body>
</html>
```
- 这个例子中font-size和width属性的值都使用了像素单位
- em单位更加灵活，如果采用em单位，那么需要修改样式设计时只消改一下字号即可，样式的其他部分一切如常
- CSS像素原本是个相对单位，但在实际使用中却变成了绝对单位，因此就没有那么灵活了

3. 百分比单位 
- 可以吧一个度量单位表示为其他属性值得百分比，这正是%单位的用途
#### 代码清单 4-23 以其他属性值得百分比为单位

```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>4-23 以其他属性值的百分比为单位</title>
      <style type="text/css">
      p {
        background: grey;
        color: white;
        font-size: 200%;
        width: 50%;
      }
      </style>
    </head>
    <body>
      <a href="http://apress.com">Visit the Apress website</a>
      <p>I like <span>apples</span> and oranges. </p>
      <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 使用百分比单位会遇到两个麻烦
  1. 并非所有属性都能用这个单位
  2. 对于能用百分比单位的属性，那个百分比挂钩的其他属性各部相同。比如: 对于font-size属性，挂钩的是元素继承到的font-size值；而对于width属性，挂钩的则是元素的包含块的宽度

4. 未获广泛支持的CSS属性

##### 表4-8 缺乏浏览器支持的CSS相对度量单位
单位标识符 | 说明
:------ | :------
gd | 与网络(grid)挂钩。它依赖于CSS规范中一些定义不太明确的属性，所以未获广泛支持
vw | 与视口(viewport)宽度挂钩。1vw等于文档显示区域(如浏览器窗口)宽度的1%
vh | 与视口高度挂钩。1vh等于文档显示区域高度的1%
vm | 1vm等于最短视口轴长(高度和宽度中较小的那个)的1%
ch | 与用当前字体显示的字符的平均宽度挂钩。它在CSS规范中的定义很潦草，其实现也不一致

- vw、vh、vm这三个单位目前只在IE中得到了实现
- vm这个单位已被重命名为vmin，同时还增加了另一个单位vmax。这两个单位分别等于vw和vh中较小和较大的那个

5. 用算式作值
- 允许将CSS属性值设置为算式式CSS3定义的一个引人关注的特性。这种灵活手段在控制能力和精确程度方面都给样式设计工作提供了帮助

#### 代码清单 4-24 以算式为值
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>4-24 以算式为值</title>
        <style type="text/css">
             p {
              background: grey;
              color: white;
              font-size: 20pt;
              width: calc(80%-20px);
             }
        </style>
    </head>
    <body>
        <a href="http://apress.com">Visit the Apress website</a>
        <p>I like <span>apples</span> and oranges. </p>
        <a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a>
    </body>
</html>
```
- 算式包含在关键字calc之后的括号之中
- 在其中可以混合使用各种单位进行基本的算术运算
- 撰写本书时，只有IE支持calc()这个特性
_____________________________________________
### 4.5 其他CSS单位

#### 4.5.1 使用CSS角度
- 角度的表示方式是一个数字后跟一个单位， 如360deg

##### 表4-9 CSS角度单位
单位标识符 | 说明
deg | 度(取值范围: 0deg ~ 360deg)
grad | 百分度(取值范围: 0grad ~ 400grad)
rad | 弧度(取值范围: 0rad ~ 6.28rad)
turn | 圆周(1turn等于360deg)

#### 4.5.2 使用CSS时间
- 可以用CSS时间单位度量时间间隔。时间的表示方式是一个数字后跟一个时间单位， 如:100ms

##### 表4-10 CSS时间单位
单位标识符 | 说明
s | 秒
ms | 毫秒

### 4.6 测试CSS特性的支持情况
- CSS规范的分散性及其在浏览器中参差不齐的实现
- 推荐几个用来检测对CSS的支持程度的有用工具
  1. http://caniuse.com: 它对各款浏览器的各种版本对HTML5和CSS3的支持情况进行了全面分析，所提供的详细信息覆盖了多种操作系统上为数众多的桌面版和手机版的浏览器。它还提供了根据浏览器的流行程度和市场影响作出决策支持的简单工具。
  2. [Modernizr](www.modernizr.com):可以用来动态测试各个特性。它是一个小小的JavaScript库，可以测试各种关键的HTML5和CSS特性是否到位，以便根据用户所用浏览器对这些特性的支持情况作出相应调整

### 4.7 有用的CSS工具

#### 4.7.1 浏览器报告样式报告
- 所有主流浏览器的开发人员工具都具有样式检查功能。基本路数都是在文档呈现结果或源代码中选择一个元素，然后查看浏览器应用在上面的样式
- 这些样式检查工具能够显示层叠的次序和计算样式(computed style, 指计入所有层叠和继承而来的样式后最终应用到元素上的样式)。用户甚至能用它们修改样式或加入新样式并查看其效果

#### 4.7.2 用SelectorGadget生成选择器
- 有一些工具可以提供一些帮助:
  1. [SelectorGadget](www.selectorgadget.com): 一个JavaScript书签小程序(bookmarklet)

#### 4.7.3 用LESS改进CSS
- LESS的工具可以用来扩展CSS，它使用JavaScript对CSS予以改进
- 这个工具有些不错的特性，包括变量、样式间的继承以及函数等
- JavaScript库，获取地址: http:/lesscss.org

#### 4.7.4 使用CSS框架
- 推荐的CSS框架是[Blueprint](www.blueprint.org)
- 方便又灵活，还有一套用于建立网格布局的出色功能

### 4.8 小结
- 本章介绍了创建和应用样式的方法、样式层叠的机制以及CSS度量单位
- 介绍了一些用来检测浏览器对特定CSS特行支持情况的有用工具
- 推荐了一些对使用CSS很有帮助的资源