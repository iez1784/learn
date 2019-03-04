# HTML 引用

# 引用 (Quotation)

这是摘自 WWF 网站的引文：

五十年来，WWF 一直致力于保护自然界的未来。 世界领先的环保组织，WWF 工作于 100 个国家，并得到美国一百二十万会员及全球近五百万会员的支持。

______________________________________________________________

# HTMl <q> 用于短的引用
HTML <q> 元素定义短的引用

浏览器通常会为<q>元素包围引号

## 实例

```html
<p>WWWF 的目标是 : <q>构建人与自然和谐共存的世界。</q></p>
```

______________________________________________________________

# 用于长引用的 HTML <blockquote>
HTML <blockquote> 元素定义被引用的节

浏览器通常会对 <blockquote> 元素进行缩进处理


## 实例

```html
<p>以下内容引用自 WWWF 的网站: </p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
五十年来, WWWF 一直致力于保护自然界的未来。
世界领先的环保组织, WWWF 工作于 100 个国家,
并得到美国一百十十万会员及全球近五百万会员的支持。
</blockquote>
```
cite 属性用于设置或者返回一个引用的cite属性值 。

cite 属性描述了引用的URL源地址。

** 注意： cite 属性在普通的 Web 浏览器中没有视觉效果，但可以通过屏幕阅读器使用。 **
______________________________________________________________

# 用于缩略词的 HTML <abbr>
HTML <abbr> 元素定义缩写或首字母缩略语
对缩写进行标记能够为浏览器、翻译系统以及搜索引擎提供有用的信息

## 实例

```html
<p><abbr title="World Health Organization">WHO</abbr> 成立于 1948 年。</p>
```

通过对缩写进行标记，您能够为浏览器、拼写检查和搜索引擎提供有用的信息。

<abbr> 标签最初是在 HTML 4.0 中引入的，表示它所包含的文本是一个更长的单词或短语的缩写形式。

## 提示和注释
** 提示：可以在 <abbr> 标签中使用全局的 title 属性，这样就能够在鼠标指针移动到 <abbr> 元素上时显示出简称/缩写的完整版本。 **

### 全局属性
<abbr> 标签支持 HTML 中的全局属性。

### 事件属性
<abbr> 标签支持 HTML 中的事件属性。   
_______________________________________________________________

# 用于定义的 HTML <dfn>
HTML <dfn> 元素定义项目或缩写的定义
<dfn>的用法， 按照HTML5标准中的描述，有点复杂:

1. 如果设置了 <dfn> 元素的title属性，则定义项目:

## 实例
```html
<p><dfn title="World Health Organization">WHO</dfn> 成立于 1948年。</p>
```

2. 如果<dfn>元素包含具有标题的<abbr>元素，则title定义项目:

## 实例
```html
<p><dfn><abbr title="World Health Organization">WHO</abbr></dfn>成立于 1948 年. </p>
```

3. 否则, <dfn> 文本内容即是项目, 并且对父元素包含定义

## 实例
```html
<p><dfn>WHO</dfn> World Health Organization 成立于 1948 年。 </p>
```

** 注释：如果您希望简而化之，请使用第一条，或使用 <abbr> 代替。 **
_______________________________________________________________

# 用于联系信息的 HTML <address>
HTML <address> 元素定义文档或文章的联系信息 (作者/拥有者)
此元素通常以斜体显示。大多数浏览器会在此元素前后添加折行。

## 实例
```html
<address>
Written by Donald duck. <br>
Visit us at:<br>
Example.com<br>
Box 564, Disneland<br>
</address>
```


_______________________________________________________________

# 用于著作标题的 HTML <cite>
HTML <cite> 元素定义著作的标题
浏览器通常会以斜体显示 <cite> 元素

## 实例
```html
<p><cite>The Scream</cite> by Edward Munch. Painted in 1893.</p>
```

** 浏览器通常会以斜体显示 cite 元素 **

———————————————————————————————————————————————————————————————

# 用于双向重写的 HTML <bdo>
HTML <bdo> 元素定义双流向覆盖 (bi-directional override)
<bdo> 元素用于覆盖当前文本方向:

## 实例
```html
<bdo dir="rtl">This text will be wirtten from right to left </bdo>
```

______________________________________________________________

# HTML 引文、引用和定义元素
| 标签 |  描述 |
| :------| :------| 
| <abbr> | 定义缩写或首字母缩略语|
| <address> | 定义文档作者或拥有者的联系信息|
| <bdo> | 定义文本方向| 
| <blockquote> | 定义从其他来源引用的节| 
| <dfn> | 定义项目或缩略词的定义| 
| <q> | 定义短的行内引用| 
| <cite> | 定义著作的标题| 