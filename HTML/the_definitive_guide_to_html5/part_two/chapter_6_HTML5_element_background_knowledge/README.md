### Chapter 6 -- HTML5元素背景知识 (P90~P97)
__________________________________________

### 6.1 语义与呈现分离
- HTML5中的一大主要变化是基本信念方面的: 将元素的语义与元素对其内容呈现结果的影响分开
- HTML元素负责文档内容的结构和含义，内容的呈现则由应用于元素上的CSS样式控制
- HTML5新增的大多数元素都有具体的含义
- 作者建议: 在语义方面要求严格点不为过，只要有条件，尽量避免用那些具有浓重呈现意味或纯粹起呈现作用的元素

### 6.2 元素选用原则
- 我们没有为书籍、技术规范、合同和博客文章中的section各自定义一个术语，而是使用一个通用的术语。附加一定的解释。
- 在选择用来标记内容的元素方面作者总结了几条原则

#### 6.2.1 少亦可为多
- 标记只应该应内容对语义的需要使用
  - 不需要定义复杂标题也就不需要使用hgroup元素
  - 只有那些引文比较重要的文档(如期刊文章)才需要用cite元素标记的详细引文
- 问问自己打算如何发挥一个元素的语义作用，如果不能马上答出就不用这个元素

#### 6.2.2 别误用元素
- 每个元素针对的是一种特定类型的内容--即便像b元素这类纯属呈现用途的元素也是如此
- 对内容进行标记时，只宜将元素用于它们原定的用途，不要创造自有的语义
- 如果找不到适合自己所要含义的元素，可以考虑使用通用元素(span或div), 并且用全局属性class表明其含义
- CSS样式不是类属性唯一的用途

#### 6.2.3 具体为佳，一以贯之
- 用来标记内容的元素应该选择最为具体的那个
- 如果已有元素能恰当表明内容的类型，就不要使用通用元素
- 同一个元素的使用在整个页面、网站或Web应用系统上要保持一致

#### 6.2.4 对用户不要想当然
- 呈现与语义分离原则的目的完全是为了让HTML文档更易于程序化处理，所要随着HTML5的采用和实现愈加广泛，HTML内容的这种使用会日益增多
- 如果不关心标记的准确性和一致性，这样的HTML文档处理起来更为困难，用户能为其找到的用处也很有限

### 6.3 元素说明体例

##### 表 6-1 ol元素
元素 | 说明 
:------ | :------ 
元素 | ol
元素类型 | 流元素
允许具有的父元素 | 任何可以包含流元素的元素
局部属性 | start、reversed和type
内容 | 0个或多个li元素
标签用法 | 开始和结束标签
是否为HTML5新增 | 否
在HTML5中的变化 | reversed属性是HTML5新增的。在HTML4中已不赞成使用的start和type属性在HTML5中又得以恢复，不过其含义变成了语义(而不是呈现)方面的。compact属性不再使用
习惯样式 | ol { display: block; list-style-type: decimal; margin-before: 1em; margin-after: 1em; margin-start: 0; margin-end: 0; padding-start: 40px}

- 摘要表中的信息包括: 
  - 哪些元素可成为该元素的父元素
  - 该元素可以包含什么类型的内容
  - 标签应该怎样使用
  - 默认呈现样式
  - 该元素是否为HTML5新增或在HTML5中发生了什么变化
  - 关于允许具有什么父元素和内容的信息，其依据是第3章介绍过的元素类型(主要是流元素和短语元素)

### 6.4 元素速览

#### 6.4.1 文档和元数据元素
- 其用途包括创建HTML文档的上层建筑，向浏览器说明文档的情况，定义脚本程序和CSS样式，提供浏览器禁用脚本时要显示的内容

#### 表 6-2 文档和元数据元素
元素 | 说明 | 类型 | 新增或有无变化
:------ | :------ | :------ | :------
base | 设置相对URL的基础 | 元数据 | 无变化
body | 表示HTML文档的内容 | 无 | 有变化
DOCTYPE | 表示HTML文档的开始 | 无 | 有变化
head | 包含文档的元数据 | 无 | 无变化
html | 表示文档中HTML部分的开始 | 无 | 有变化 
link | 定义与外部资源(通常是样式表或网站图标)的关系 | 元数据 | 有变化
meta | 提供关于文档的信息 | 元数据 | 有变化
noscript | 包含浏览器禁用脚本或不支持脚本时显示的内容 | 元数据、短语 | 无变化
script | 定义脚本程序，可以是文档内嵌的也可以是外部文件中的 | 元数据、短语 | 有变化
style | 定义CSS样式 | 元数据 | 有变化
title | 设置文档标题 | 元数据 | 无变化

#### 6.4.2 文本元素
- 文本元素用来为内容提供基本的结构和含义

元素 | 说明 | 类型 | 新增或有无变化
:------ | :------ | :------ | :------
a | 生成超链接 | 短语、流 | 有变化
abbr | 缩略语 | 短语 | 无变化
b | 不带强调或着重意味地标记一段文字 | 短语 | 有变化 
br| 表示换号 | 短语 | 无变化 
cite | 表示其他作品的标题 | 短语 | 有变化
code | 表示计算机代码片段 | 短语 | 无变化
del | 表示从文档中删除的文字 | 短语、流 | 新增
dfn | 表示术语定义 | 短语 | 无变化
em | 表示着重强调的一段文字 | 短语 | 无变化
i | 表示与周边内容秉性不同的一段文字、例如来自另一种语言的词语 | 短语 | 有变化
ins | 表示加入文档的文字 | 短语、流| 无变化
kbd | 表示用户输入内容 | 短语 | 无变化
mark | 表示一段因为与上下文中另一词语相关而被突出显示的内容 | 短语 | 新增
q | 表示引自他处的内容 | 短语 | 无变化
rp | 与ruby元素结合使用，标记括号 | 短语 | 新增
rt | 与ruby元素结合使用，标记注音符号 | 短语 | 新增
ruby | 表示位于表意文字上方或右方的注音符号 | 短语 |新增
s | 表示文字已不再准确 | 短语 | 有变化
samp | 表示计算机程序的输出内容 | 短语 | 无变化
small | 表示小号字体内容 | 短语 | 有变化
span | 一个没有自己的语义的通用元素。可以用在希望应用一些全局属性却又不想引入额外语义的情况 | 短语 | 无变化
strong | 表示重要的内容 | 短语 | 无变化
sub | 表示小标文字 | 短语 | 无变化
sup | 表示上标文字 | 短语 | 无变化
time | 表示时间或日期 | 短语 | 新增
u | 不带强调或着重意味地标记一段文字 | 短语 | 有变化
var | 表示程序或计算机系统中的变量 | 短语 | 无变化
wbr | 表示可安全换行的地方 | 短语 | 新增

#### 6.4.3 对内容分组

##### 表 6-4 用于分组的元素

元素 | 说明 | 类型 | 新增或有无变化
:------ | :------ | :------ | :------
blockquote | 表示引自他处的大段内容 | 流 | 无变化
dd | 用在dl元素之中，表示定义 | 无 | 无变化
div | 一个没有任何既定语义的通用元素，是span元素在流元素中的对应物 | 流 | 无变化
dl | 表示包含一系列术语和定义的说明列表 | 流 | 无变化
dt | 用在dl元素之中，表示术语| 无 | 无变化
figcation |表示figure元素的标题 | 无 | 新增
figure | 表示图片 | 流 | 新增
hr | 表示段落级别的主题转换 | 流 | 新增
li | 用在ul、ol和menu元素中，表示列表项 | 无 | 有变化
ol | 表示有序列表 | 流 | 有变化
p | 表示段落 | 流 | 有变化
pre | 表示其格式应被保留的内容  | 流 | 无变化
ul | 表示无序列表 | 流 | 有变化

#### 6.4.4 划分内容
- 让每个概念、观点或主题彼此分隔开

##### 表6-5 用于划分内容的元素

元素 | 说明 | 类型 | 新增或有无变化
:------ | :------ | :------ | :------
address | 表示文档或article的联系信息 | 流 | 新增
article | 表示段独立的内容 | 流 | 新增
aside | 表示与周边内容稍有牵涉的内容 | 流| 新增
details | 生成一个区域，用户将其展开可以获得更多细节知识 | 流| 新增
footer | 表示尾部 | 流 | 新增
h1~h6 | 表示标题 | 流 | 无变化
header | 表示首部 | 流| 新增 
hgroup | 将一组标题组织在一起，以便文档大纲只显示其中第一个标题 | 流| 新增
nav | 表示有意集中在一起的导航元素 | 流| 新增
section |表示一个重要的概念或主题 | 流| 新增
summary | 用在detais元素中，表示该元素内容的标题或说明 | 无 | 新增

#### 6.4.5 制表
- 表 6-6 中的元素用于制作显示数据的表格
- 表格在HTML5中的主要变化是不能再用来控制页面布局

##### 表 6-6 表格元素

元素 | 说明 | 类型 | 新增或有无变化
:------ | :------ | :------ | :------
caption | 表示表格标题  | 无 | 有变化
col | 表示一列 | 无 | 有变化
colgroup | 表示一组列 | 无 | 有变化
table | 表示表格 | 流 | 有变化
tbody | 表示表格主体 | 无 | 有变化
td | 表示单元格 | 无 | 有变化
tfoot | 表示表脚 | 无 | 有变化
th | 表示标题行单元格 | 无 | 有变化
thead | 表示标题行 | 无 | 有变化
tr | 表示一行单元格 | 无 | 有变化

#### 6.4.6 创建表单
- 表6-7中的元素用于创建HTML表单，以便获取用户的输入数据

##### 表 6-7 表单元素

元素 | 说明 | 类型 | 新增或有无变化
:------ | :------ | :------ | :------
button | 表示可用来提交或重置表单的按钮(或一般按钮) | 短语 | 有变化
datalist | 定义一组提供给用户的建议值 | 流 | 有变化
fieldset | 表示一组表单元素 | 流 | 有变化
form | 表示HTML表单 | 流 | 有变化
input | 表示用来收集用户输入数据的控件 | 短语 | 有变化
keygen | 生成一对公钥和私钥 | 短语 | 新增
label | 表示表单元素的说明标签 | 短语 | 有变化
legend | 表示fieldset元素的说明性标签 | 无 | 无变化
optgroup | 表示一组相关的option元素 | 无 | 无变化
option | 表示供用户选择的一个选项 | 无 | 无变化
output | 表示计算结果 | 短语 | 新增
select | 给用户提供一组固定的选项 | 短语 | 有变化
textarea | 用户可以用它输入多行文字 | 短语 | 有变化

#### 6.4.7 嵌入内容
- 表 6-8中的元素用于在HTML文档

##### 表 6-8 嵌入元素

元素 | 说明 | 类型 | 新增或有无变化
:------ | :------ | :------ | :------
area | 表示一个用户客户端分区响应图的区域 | 短语 | 有变化
audio | 表示一个音频资源 | 无| 新增
canvas | 生成一个动态的图形画布 | 短语、流| 新增
embed | 用插件在HTML文档中嵌入内容 | 短语 | 新增
iframe | 通过创建一个浏览上下文在一个文档中嵌入另一个文档 | 短语 | 有变化
img | 嵌入图像 | 短语 | 有变化
map | 定义客户端分区响应图 | 短语、流  | 有变化 
meter | 嵌入数值在许可值范围背景中的图形表示 | 短语 | 新增
object | 在HTML文档中嵌入内容。也可用于生成浏览上下文和生成客户端分区响应图 | 短语、流 | 有变化
param | 表示将通过object元素传递给插件的参数 | 无 | 无变化
progress | 嵌入目标进展或任务完成情况的图形表示 | 短语 | 新增
source | 表示媒体资源 | 无 | 新增
svg | 表示结构化矢量内容| 无 | 新增
track |表示媒体的附加轨道(例如字幕) | 无 | 新增
video |表示视频资源| 无 | 新增

### 6.5 未实现的元素
- 有两个元素目前还没有浏览器实现，而且在HTML5规范中也仅有含糊不清的说明，这两个元素是command和menu

### 6.6 小结
- 尽量使用最具体的元素，不要无用元素，在文档、网站和Web应用系统中元素的使用都要保持一致