# HTML 类

对 HTML 进行分类(设置类)， 使我们能够为元素的 类 定义 CSS样式

为相同的类设置相同的样式， 或者为不同的类设置不同的样式

 ____________________________________________________________

 ## 实例
 ```html
<!DOCTYP html>
<html>
<head>
<style>
.cities {
    background-color: black;
    color:white;
    margin:20px;
    padding:20px;
    }
</style>
</head>

<body>
    <div class="cities">
        <h2>London</h2>
        <p>
            London is the capital city of England.
            It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants.
        </p>
    </div>
</body>

</html>
 ```

______________________________________________________

## 分类块级元素
HTML `<div>` 元素是块级元素。 它能够用作其他 HTML 元素的容器。
设置 `<div>` 元素的类， 使我们能够为相同的 `<div>` 元素设置相同的类:

## 实例

```html
<!DOCTYPE html>
<html>
<head>
    <style>
    .cities {
        background-color: black;
        color:white;
        margin:20px;
        padding:20px;
    }
</style>
</head>

<body>

<div class="cities">
    <h2>London</h2>
    <p>London is the capital city of England.
        It is the most populous city in the United Kingdom,
        with a metropolitan area of over 13 million inhabitants.</p>
    </div>

<div class="cities">
    <h2>Paris</h2>
    <p>Paris is the capital and most populous city of France.</p>
</div>

<div class="cities">
    <h2>Tokyo</h2>
    <p>Tokyo is the capital of Japan, the center of the Greater Tokyo Area,
        and the most populous metropolitan area in the world.</p>
    </div>

</body>
</html>

```