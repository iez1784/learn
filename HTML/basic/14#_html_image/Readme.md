# HTML 图像

# 通过使用 HTML, 可以在文档中显示图像
_________________________________________________

## 实例
[插入图像](http://www.w3school.com.cn/tiy/t.asp?f=html_image)
如何在网页中显示图像

[从不同的位置插入图片](http://www.w3school.com.cn/tiy/t.asp?f=html_image2)
如何将其他文件夹或服务器的图片显示到网页中

_________________________________________________

# 图像标签 ( <img> ) 和源属性 ( Src )
在 HTML 中, 图像由 <img> 标签定义。
<img> 是空标签, 意思是说, 它只包含属性, 并且没有闭合标签
要在页面上显示图像, 你需要使用源属性 ( src ). src 指 "source"。 源属性的值是图像的 URL 地址。

定义图像的语法是:

```html
<img src="url" />
```

URL 指存储图像的位置。 如果名为"boat.gif"的图像位于 www.w3school.com.cn的images目录中, 那么其 URL 为 http://www.w3school.com.cn/images/boat.gif

浏览器将图像显示在文档中图像标签出现的地方。 如果你将图像标签置于两个段落之间，那么浏览器会首先显示第一个段落， 然后显示图片， 最后显示第二段

————————————————————————————————————————————————————

替换文本属性 ( Alt )
alt 属性用来为图像定义一串预备的可替换的文本。 替换文本属性的值是用户定义的。

```html
<img src="boat.gif" alt="Big Boat">
```
在浏览器无法载入图像时， 替换文本属性告诉读者她们失去的信息。 此时，浏览器将显示这个替代性的文本而不是图像。 为页面上的图像都加上替换文本属性是个好习惯， 这样有助于更好的显示信息， 并且对于那些使用纯文本浏览器的人来说是非常有用的。

_____________________________________________________

# 基本的注意事项 - 有用的提示:

假如某个 HTML 文件包含十个图像， 那么为了正确显示这个页面， 需要加载11个文件。 加载图片是需要时间的， 所以我们的建议是: 慎用图片

_____________________________________________________

# 更多实例

[背景图片](http://www.w3school.com.cn/tiy/t.asp?f=html_backgroundimage)
如何向 HTML 页面添加背景图片

[排列图片](http://www.w3school.com.cn/tiy/t.asp?f=html_image_align)
如何在文字中排列图像

[浮动图像](http://www.w3school.com.cn/tiy/t.asp?f=html_image_float)
如何使图片浮动至段落的左边或右边

[调整图像尺寸](http://www.w3school.com.cn/tiy/t.asp?f=html_image_size)
如何将图片调整到不同的尺寸

[为图片显示替换文本](http://www.w3school.com.cn/tiy/t.asp?f=html_image_alt)
如何为图片显示替换文本。在浏览器无法载入图像时，替换文本属性告诉读者们失去的信息。为页面上的图像都加上替换文本属性是个好习惯

[制作图像链接](http://www.w3school.com.cn/tiy/t.asp?f=html_image_link)
如何将图像作为一个链接使用

[创建图像映射](http://www.w3school.com.cn/tiy/t.asp?f=html_areamap)
如何创建带有可供点击区域的图像地图。其中的每个区域都是一个超级链接

[把图像转换为图像映射](http://www.w3school.com.cn/tiy/t.asp?f=html_ismap)
如何把一幅普通的图像设置为图像映射

——————————————————————————————————————————————————————————

# 图像标签
标签 | 描述
`<img>` | 定义图像
`<map` | 定义图像地图
`<area>` | 定义图像地图中的可点击区域
