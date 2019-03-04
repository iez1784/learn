# HTML 表格

# 可以使用 HTML 创建表格

________________________________________

## 实例

[表格](http://www.w3school.com.cn/tiy/t.asp?f=html_tables)
这个例子演示如何在 HTML 文档中创建表格

[表格边框](http://www.w3school.com.cn/tiy/t.asp?f=html_table_borders)
演示各种类型的表格边框

________________________________________

# 表格
表格由 `<table>`标签来定义。每个表格均有若干行(由`<tr>`标签定义)， 每行被分割若干单元格(由`<td>`标签定义)。字母td每日表格数据(table data)， 即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等

```html
<table border="1">
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```
在浏览器显示如下：

row 1, cell 1   row 1, cell 2
row 2, cell 1   row 2, cell 2

_________________________________________

# 表格和边框属性
如果不定义边框属性, 表格将不显示边框。有时这很有用， 但是大多数时候， 我们希望显示边框
使用边框属性来显示一个带有边框的表格:

```html
<table border="1">
<tr>
<td>Row 1, cell 1</td>
<td>Row 1, cell 2</td>
</tr>
</table>
```

—————————————————————————————————————————

# 表格的表头
表格的表头使用`<th>`标签进行定义
大多数浏览器会把表头显示为粗体居中的文本:
```html
<table border="1">
<tr>
<th>Heading</th>
<th>Another Heading</th>
</tr>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>
```

在浏览器显示如下:
**Heading** **Another** **Heading**
row 1, cell 1   row 1, cell 2
row 2, cell 1   row 2, cell 2

___________________________________________

# 表格中的空单元格
在一些浏览器中, 没有内容的表格单元显示得不太好。 如果某个单元格是空的 (没有内容) , 浏览器可能无法显示出这个单元格的边框。

```html
<table border="1">
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td></td>
    <td>row 2, cell 2</td>
    </tr>
</table>
```

浏览器可能会这样显示:
![](/table_td_empty.gif)

**注意:** 这个空的单元格的边框没有被显示出来。为了避免这种情况，在空单元格中添加一个空格占位符， 就可以将边框显示出来。
```html
<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>row 2, cell 2</td>
</tr>
</table>
```

在浏览器中显示如下：

row 1, cell 1   row 1, cell 2
                row 2, cell 2

——————————————————————————————————————————————————————————————————————
# 更多实例
[没有边框的表格](http://www.w3school.com.cn/tiy/t.asp?f=html_tables2)
一个没有边框的表格。

[表格中的表头(Heading)](http://www.w3school.com.cn/tiy/t.asp?f=html_table_headers)
如何显示表格表头。

[空单元格](http://www.w3school.com.cn/tiy/t.asp?f=html_table_nbsp)
如何使用 "&nbsp;" 处理没有内容的单元格。

[带有标题的表格](http://www.w3school.com.cn/tiy/t.asp?f=html_tables3)
一个带标题 (caption) 的表格

[跨行或跨列的表格单元格](http://www.w3school.com.cn/tiy/t.asp?f=html_table_span)
如何定义跨行或跨列的表格单元格。

[表格内的标签](http://www.w3school.com.cn/tiy/t.asp?f=html_table_elements)
如何显示在不同的元素内显示元素。

[单元格边距(Cell padding)](http://www.w3school.com.cn/tiy/t.asp?f=html_table_cellpadding)
如何使用 Cell padding 来创建单元格内容与其边框之间的空白。

[单元格间距(Cell spacing)](http://www.w3school.com.cn/tiy/t.asp?f=html_table_cellspacing)
如何使用 Cell spacing 增加单元格之间的距离。

[向表格添加背景颜色或背景图像](http://www.w3school.com.cn/tiy/t.asp?f=html_table_background)
如何向表格添加背景。

[向表格单元添加背景颜色或者背景图像](http://www.w3school.com.cn/tiy/t.asp?f=html_table_cellbackground)
如何向一个或者更多表格单元添加背景。

[在表格单元中排列内容](http://www.w3school.com.cn/tiy/t.asp?f=html_table_align)
如何使用 "align" 属性排列单元格内容,以便创建一个美观的表格。

[框架(frame)属性](http://www.w3school.com.cn/tiy/t.asp?f=html_table_frame)
如何使用 "frame" 属性来控制围绕表格的边框。

[带有 thead、tbody 以及 tfoot 元素的 HTML 表格](http://www.w3school.com.cn/tags/tag_thead.asp)

__________________________________________________

# 表格标签

表格| 描述
:------|:------
`<table>`|定义表格
`<caption>`|定义表格标题
`<th>`|定义表格的表头
`<tr>`|定义表格的行
`<td>`|定义表格单元
`<thead>`|定义表格的页眉
`<tbody>`|定义表格的主体
`<tfoot>`|定义表格的页脚
`<col>`|定义用于表格列的属性
`<colgroup>`|定义表格列的组
________________________________________________

# `colgroup`

## 浏览器支持
所有主流浏览器支持 `<colgroup` 标签
Firefox、Chrome以衣Safari仅支持colgroup 元素的span和width属性

## 定义和用法
`<colgroup>` 标签用于对表格中的列进行组合, 以便对其进行格式化。
如需对全部列应用样式, `<colgroup`标签很有用, 这样就不需要对各个单元和各行重复应用样式了.
`<colgroup>` 标签只能在table元素中使用

_______________________________________________

## HTML与XHTML之间的差异
NONE
_______________________________________________

## 提示和注释:
**提示:** 请为`<colgroup`标签添加class属性。这样就可以使用CSS来负责对齐方式、宽度和颜色等等
**注释:** col 元素是仅包含属性的空元素。如需创建列，您就必须在tr元素内部规定td元素

参见: [`<col`标签](http://www.w3school.com.cn/tags/tag_col.asp)

## 可选的属性
属性|值|描述
:------|:------|:------
`<align>`|right</br>left</br>center</br>justify</br>char</br>|定义在列组合中内容的水平对齐方式
`<char>` |character| 规定根据哪个字符来对齐列组中的内容
`<charoff>`|number|规定第一个对齐字符的偏移量
`<span>`|number|规定列组应该横跨的列数
`<valign>`|top</br>middle</br>bottom</br>baseline|定义在列组合中内容的垂直对齐方式
`<width>`|pixels</br>%</br>relative_length|规定列组合的宽度

## 全局属性
`<colgroup>` 标签支持 [HTML中的全局属性](http://www.w3school.com.cn/tags/html_ref_standardattributes.asp)

## 事件属性 
`<clogroup>` 标签支持 [HTML中的事件属性](http://www.w3school.com.cn/tags/html_ref_eventattributes.asp)

## 相关页面
HTMl DOM 参考手册: [Column对象](http://www.w3school.com.cn/jsref/dom_obj_col.asp)