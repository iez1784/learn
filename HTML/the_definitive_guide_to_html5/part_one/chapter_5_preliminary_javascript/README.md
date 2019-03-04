## Chapter 5 -- 初探JavaScript (P60-P87)
______________________________________
- 对于没有编程经验的新手，lifehacker.com这个大众化网站上的系列文章是不错的启蒙读物
- 它没有预设编程知识门槛， 所有例子都已JavaScript写就，非常方便
- 使用说明参见: http://lifehacker.com/5744113/learn-to-code-the-full-beginners-guide
- 有意深入学习JavaScript的读者可以读一下我推荐的两本书
  1. 在语言的一般性知识方面， 推荐David Flanagan写的JavaScript: The Definitive Guide(O'Reilly出版) (JavaScript权威指南(第6版本))
  2. 在高级概念和特性方面，推荐Ross Harmes和Dustin Diaz写的Pro JavaScript Design Patterns(Apress出版) （JavaScript设计模式）

#### 5-1 本章内容概要

问题 | 解决方案 | 代码清单
:------ | :------ | :------
定义文档内嵌脚本程序 | 使用script元素 | 5-1
立即执行一条程序语句 | 将语句直接放在script元素内 | 5-2
定义JavaScript函数 | 使用function关键字 | 5-3 ~ 5-5
定义基本类型的变量 | 使用var关键字，并以字面量表示其值 | 5-6 ~ 5-9
创建对象 | 使用new object()或对象字面量语法 | 5-10 、 5-11
给对象添加方法 | 新建一个属性，然后将一个函数赋给它 | 5-12
获取或设置对象的属性值 | 使用圆点或数组索引符号表示法 | 5-13
枚举对象中的属性 | 使用for...in语句 | 5-14
给对象添加属性或方法 | 将一个值赋给所需属性名 | 5-15 、5-16
删除对象的一个属性 | 使用delete关键字 | 5-17
判断对象是否具有某个属性 | 使用in表达式 | 5-18
判断两个对象的值是否相等(不考虑类型差别) | 使用相等运算符== | 5-19、5-21
判断两个对象是否类型和值都相同 | 使用等同运算符=== | 5-20、5-22
显示类型转换 | 使用Number或String函数 | 5-23 ~ 5-25
创建数组 | 使用new Array()或数组字面量 | 5-26、 5-29
枚举数组内容 | 使用for循环 | 5-30
处理错误 | 使用try...catch语句 | 5-31、5-32
比较null和undefined值 | 将值转换为boolean类型， 或在需要同等对待null和undefined是使用相等运算符==，在要区别对待它们是使用恒等运算符=== | 5-33 ~ 5-36

__________________________________________________________
### 5.1 准备使用 JavaScript
- 在HTML文档中定义脚本有几种方法可供选择
- 既可以定义内嵌脚本(脚本是HTML文档的一部分)，也可以定义外部脚本(脚本包含在另一个文件中，通过一个URL引用)。这两种方法都要用到script元素(第7章)，这章用的是内嵌脚本

##### 代码清单 5-1 一段简单的内嵌脚本
```html
<!DOCTYPE HTML>
<html>
    <head>
       <title>5-1 一段简单的内嵌脚本</title>
    </head>
    <body>
        <script type="text/javascript">
             document.writeln("Hello");
        </script>
    </body>
</html>
```
- 这段小脚本的作用是在文档中加入单词Hello
- script元素位于文档中其他内容之后，这样一来在脚本执行之前浏览器就已经对其他元素进行了解析

### 5.2 使用语句
- JavaScript的基本元素示语句
- 一条语句代表着一条命令，通常以分号(;)结尾
- 实际上分号用不用都可以，不过加上分号可让代码更易阅读，并且可以在一行书写几条语句

##### 代码清单 5-2 使用JavaScript语句
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-2 使用JavaScript语句</title>
    </head>
    <body>
        <script type="text/javascript">
            document.writeln("This is a statement");
            document.writeln("This is also a statement");
        </script>
    </body>
</html>
```
- 浏览器一次执行每条语句。本例做的只是输出两条信息
- This is a statement
- This is also a statement

### 5.3 定义和使用函数
- 在script元素中直接定义语句，那么浏览器一遇到这些语句就会执行它们。也可以把几条语句包装在一个函数中，浏览器只有在遇到一条调用该函数的语句时才会执行它

##### 代码清单 5-3 定义JavaScript函数
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-3 定义JavaScript函数</title>
    </head>
    <body>
      <script type="text/javascript">
            function myFunc() {
              document.writeln("This is a statement");
            };
            myFunc();
      </script>
    </body>
</html>
```
- 函数所含语句被包围在一对大括号({和})之间，称为代码块
- 这个代码清单定义了一个名为myFunc的函数，其代码块只有一条语句
- JavaScript是区分大小写的语言，因此function这个关键字必须小写
- 只有浏览器遇到下面这样一条调用myFunc函数的语句时，该函数中的语句才会执行

#### 5.3.1 定义带参数的函数
- JavaScript中也可以为函数定义参数
- 代码清单5-4

#### 代码清单 5-4 定义带参数的函数
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>5-4 定义带参数的函数</title>
    </head>
    <body>
      <script type="text/javascript">
          function myFunc(name, weather) {
              document.writeln("Hello " + name + ".");
              document.writeln("It is " + weather + " today");
          };
          myFunc("Adam","sunny");
        </script>
      </body>
</html>
```
- 这里为myFunc函数添加了两个函数: name和weather
- JavaScript是门弱类型语言，所以定义函数的时候不必声明参数的数据类型
- 调用函数时提供的参数数目不必与函数定义的参数数目相同
- 如果提供的参数值更少，那么所以未提供值的参数的值均为undefined
- 如果提供的参数值更多，那么多出的值会被忽略
- 要想定义两个同名但参数数目不同的函数，然后让JavaScript根据调用函数时提供的参数数目确定所调用的函数是不可能的
- 要是定义了两个同名的函数，那个第二个定义将会取代第一个

#### 5.3.2 定义会返回结果的函数
- 可以用return 关键字从函数中返回结果

##### 代码清单5-5 从函数中返回结果
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-5 从函数中返回结果</title>
    </head>
    <body>
        <script type="text/javascript">
             function myFunc(name) {
                  return ("Hello" + name + ".")
             };
             document.writeln(myFunc("Adam"));
           </script>
    </body>
</html>
```

- 注意，定义这个函数时不用声明它会返回结果，也不用声明结果的数据类型

### 5.4 使用变量和类型
- 定义变量要使用var关键字
- 在定义的同时还可以像在一条单独的语句中那样为其赋值
- 定义在函数中的变量称为局部变量，只能在该函数范围内使用
- 直接在script元素中定义的变量称为全局变量，可以在任何地方使用-包括在其他脚本中

##### 代码清单 5-6 使用局部变量和全局变量
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-6 使用局部变量和全局变量</title>
    </head>
    <body>
        <script type="text/javascript">
           var myGlobalVar = "apples";
           function myFunc(name) {
               var myLocalVar = "sunny";
               return ("Hello" + name + ". Today is " + myLocalVar + ".");
           };
           document.writeln(myFunc("Adam"));
         </script>
        <script type="text/javascript">
           document.writeln("I like " + myGlobalVar )
         </script>
    </body>
</html>
```
- JavaScript是一种弱类型语言，但这不代表它没有类型，而是指不用明确声明变量的类型以及可随心所欲地用同一变量表示不同类型的值
- javaScript根据赋给变量的值确定其类型，还可以根据使用场景在类型间自由转换

#### 5.4.1 使用基本类型
- JavaScript定义了一小批基本类型(primitive type)，它们包括:
  - 字符串类型(string)
  - 数值类型(number)
  - 布尔类型(boolean)
- 看起来很少，但JavaScript的这三种类型具有很大的灵活性

1. 字符串类型变量
##### 代码清单 5-7 定义字符串变量

```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-7 定义字符串变量</title>
    </head>
    <body>
        <script type="text/javascript">
            var firstString = "This is a string";
            var secondString = 'And so is this';
          </script>
        </body>
</html>
```
- 表示字符串时使用的引号要匹配
- 例如: 字符串前端用单引号而后端用双引号是不行的。 eg: ' "

2. 布尔类型
- boolean类型有两个值: true和false
- 这个类型最重要的使用场合是: 条件语句

##### 代码清单 5-8 定义布尔变量
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-8 定义布尔变量</title>
    </head>
    <body>
        <script type="text/javascript">
            var firstBool = true;
            var secondBool = false;
          </script>
    </body>
</html>
```

3. 数值类型
- 整数和浮点数(也称实数)都用number类型表示

##### 代码清单 5-9 定义数值变量
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-9 定义数值变量</title>
    </head>
    <body>
        <script type="text/javascript">
            var daysInWeek = 7;
            var pi = 3.14;
            var hexValue = oxFFFF;
          </script>
        </body>
</html>
```
- 定义number类型变量时不必言明所用的是哪种数值，只消写出需要的值即可，JavaScript会酌情处理
- 上例使用了一个整数、一个浮点数和一个以0x开头的十六进制数

##### 代码清单 5-10 创建对象
```html
<html>
    <head>
        <title>5-10 创建对象</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = new Object();
            myData.name = "Adam";
            myData.weather = "sunny";

            document.writeln("Hello " + myData.name + ". ");
            document.writeln("Today is " + myData.weather + ".");
      </script>
    </body>
</html>
```
- 通过调用new object()的方式创建了一个对象，然后将其赋给一个名为myData的变量。在此之后，即可像这样通过赋值的方式定义其属性:
myData.name = "Adam";
- 像这样用变量名后加一点再加属性名的方式就能获取该属性的值: document.writeln("Hello " + myData.name + ". ");

1. 使用对象字面量
- 用对象字面量的方式可以一口气定义一个对象及其属性

##### 代码清单 5-11 使用对象字面量

```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-11 使用对象字面量</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
              name: "Adam",
              weather: "sunny"
            };
            document.writeln("Hello " + myData.name + ". ");
            document.writeln("Today is " + myData.weather + ".");
          </script>
    </body>
```
- 属性的名称和值之间以冒号(:)分隔，而各个属性之间又以逗号(，)分隔

2. 将函数用做方法
- 对象可以添加属性，也能添加函数
- 属于一个对象的函数称为其方法

###### 代码清单 5-12 为对象添加方法
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-12 为对象添加方法</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
                name: "Adam",
                weather: "sunny",
                printMessage: function() {
                    document.writeln("Hello " + this.name + ". ");
                    document.writeln("Today is " + this.weather + ".");
                }
            };

            myData.printMessage(); 
          </script>
    </body>
</html>
```
- 此例将一个函数变成了一个名为printMesage的方法
- 注意:  在方法内部使用对象属性时要用到this关键字。函数作为方法使用时，其所属对象会以关键字this的形式作为一个参数被传给它
- 提示: 在创造和管理对象方面JavaScript还有许多招数可用，可以读一下本章开头推荐的书

#### 5.4.3 使用对象
- 创建对象之后，可以用来做许多事

1. 读取和修改对象属性值
- 对象最显而易见得操作是读取或修改属性值
- 这些操作有两种不同的语法形式

##### 代码清单 5-13 读取和修改对象属性值
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-13 读取和修改对象属性值</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
                name: "Adam",
                weather: "sunny",
            };
            myData.name = "Joe";
            myData["weather"] = "raining" 
            document.writeln("Hello " + myData.name + ".");
            document.writeln("It is " + myData["weather"]);
          </script>
        </body>
</html>
```
- 第一种：用句点将对象名和属性名连接在一起: myData.name = "Joe";
- 第二种: 类似数组索引： myData["weather"] = "raining"; 
  - 这种形式下，属性名作为一个字符串放在一对方括号直接
  - 这种存取属性值的办法非常方便，可用变量表示属性名

```html
var myData = {
  name: "Adam",
  weather: "sunny",
};
var propName = "weather";
myData[propName] = "raining";
``` 
- 在此基础上才能枚举对象属性

2. 枚举对象属性
- 要枚举对象属性可以使用for...in语句

##### 代码清单 5-14 枚举对象属性
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-14 枚举对象属性</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
              name: "Adam",
              weather: "sunny",
              printMessages: function() {
                document.writeln("Hello " + this.name + ".");
                document.writeln("Today is " + this.weather + ".");
              }
            };
            for (var prop in myData) {
              document.writeln("Name: " + prop + "Value: " + myData[prop]);
            }
          </script>
        </body>
</html>
```
- for...in循环代码块中的语句会对myData对象的每一个属性执行一次
- 在每一次迭代过程中，所要处理的属性名会被赋给prop变量
- 例子中使用的类数组索引语法(使用方括号[])获取对象的属性值
- 作为方法定义的那个函数也被枚举出来了。
- 方法本身也被视为对象的属性

3. 增删属性和方法
- 就算是用对象字面量生成的对象，也可以为其定义新属性

##### 代码清单 5-15 为对象添加新属性
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-15 为对象添加新属性</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
              name: "Adam",
              weather: "sunny",
            };
            myData.dayofWeek = "Monday";
          </script>
    </body>
</html>
```
- 为对象添加了一个名为dayOfWeek的新属性，这里使用的是圆点表示法(用句点将对象和属性的名称链接在一起)
- 通过将属性值设置为一个函数也能为对象添加新方法

###### 5-16 为对象添加新方法

```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-16 为对象添加新方法</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
              name: "Adam",
              weather: "sunny",
            };
            myData.sayHello = function() {
              document.writeln("Hello");
            };
          </script>
    </body>
</html>

- 对象的属性和方法可以用delete关键字删除

##### 5-17 删除对象的属性
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-17</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
              name: "Adam",
              weather: "sunny",
            };
            myData.sayHello = function() {
              document.writeln("Hello");
            };
            delete myData.name;
            delete myData["weather"];
            delete myData.sayHello;
          </script>
    </body>
</html>
```

4. 判断对象是否具有某个属性
- 可以用in表达式判断对象是否具有某个属性

##### 代码清单 5-18 检查对象是否具有某个属性
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-18 检查对象是否具有某个属性</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
              name: "Adam",
              weather: "sunny",
            };

            var hasName = "name" in myData;
            var hasDate = "date" in myData;
            document.writeln("hasName: " + hasName);
            document.writeln("hasDate: " + hasDate);
          </script>
    </body>
</html>
```
- 分别用一个已有的和一个没有的属性进行测试
- hasName变量的值会是true
- hasDate变量的值会是false


### 使用JavaScript运算符
- JavaScript定义了大量标准的运算符 表5-2罗列了最常用的一些运算符

##### 表 5-2 常用的JavaScript运算符
运算符 | 说明
:------ | :------
++ 、 -- | 前置或后置自增或自减
+、-、*、/、% | 加、减、乘、除、求余
< 、<= 、> 、>= | 小于、小于等于、大于、大于等于
== 、!= | 相等和不相等
=== 、 !== | 等同和不等同
&&、`<||>` | 逻辑与、逻辑或
= | 赋值
+ | 字符串连接
`<?:>` | 三元条件语句

#### 5.5.1 相等和等同运算符
- 相等运算符会尝试将操作数转换为同一类型以便判断是否相等

##### 代码清单 5-19 使用相等运算符
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-19 使用相等运算符</title>
    </head>
    <body>
        <script type="text/javascript">
            var firstVal = 5;
            var  secondVal = "5";
            if (firstVal == secondVal) {
              document.writeln("They are the same");
            }
            else {
              document.writeln（"The are NOT the same");
            }</script>
    </body>
</html>
```
- 结果:They are the same
- JavaScript先将两个操作数转换为同一类型再对其进行比较--从本质上讲，相等运算符测试两个值是否相等，不管其类型
- 如果想判断值和类型是否都相同，那么应该使用的是等同运算符(===，由三个等号组成。相等运算符是由两个等号组成)

###### 代码清单 5-20 使用等同运算符
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-20 使用相同运算符</title>
    </head>
    <body>
        <script type="text/javascript">
            var firstVal = 5;
            var  secondVal = "5";
            if (firstVal === secondVal) {
              document.writeln("They are the same");
            }
            else {
              document.writeln（"The are NOT the same");
            }</script>
    </body>
</html>
```
- 结果: They are Not the same
- 等同运算符判定两个变量不一样。这两个运算符不会进行类型转换
- 提示: 代码清单 5-19 和 5-20 使用了if条件语句。这个语句先对一个条件进行评估，要是结果为true，就执行代码块中的语句；if语句还可以加上一个else字句，字句所含代码块中的语句会在条件为false的情况下执行

- JavaScript基本类型(值字符串和数值等内置类型)的比较是值德比较，而JavaScript对象的比较则是引用的比较

###### 代码清单 5-21 对象的相等和等同测试
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-21 对象的相等和等同测试</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData1 = {
                name: "Adam",
                weather: "sunny",
            };
            var myData2 = {
                name: "Adam",
                weather: "sunny",
            };
            var myData3 = myData2;
            var test1 = myData1 == myData2;
            var test2 = myData2 == myData3;
            var test3 = mydata1 === myData2;
            var test4 = myData2 === myData3;

            document.writeln("Test1 ": + test1 + "Test 2:" + test2);
            document.writeln("Test3 ": + test3 + "Test 4:" + test4);
          </script>
        </body>
</html>
```
- 结果: 
  - Test 1: false  Test 2: true
  - Test 3: false  Test 4: true

##### 代码清单 5-22 基本类型的相等和等同测试
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title> 5-22 基本类型的相等和等同测试</title>
    </head>
    <body>
        <script type="text/javascript">
        var myData1 = 5;
        var myData2 = "5";
        var myData3 = myData2;

        var test1 = myData1 == myData2;
        var test2 = myData2 == mydata3;
        var test3 = mydata1 === myData2;
        var test4 = myData2 === myData3;

        document.writeln("Test 1: " + test1  + "Test 2: " + test2);
        document.writeln("Test 3: " + test3  + "Test 4: " + test4);
      </script>
    </body>
</html>
```
- 结果:
  - Test 1: true   Test 2: true
  - Test 3: flase  Test 4: true

#### 5.5.2 显示类型转换
- 字符串链接运算符(+)比加法运算符(也是+)优先级更高
- 这可能会引起混乱，这是因为JavaScript在计算结果时会自动进行类型转换，其结果未必跟预期一样

##### 5-23 字符串连接运算符的优先权
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title> 5-23 字符串连接运算符的优先权</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData1 =  5 + 5;
            var myData2 = 5 + "5";

            document.writeln("Result1 1:" + myData1);
            document.writeln("Result1 2:" + myData2);
        </script>
    </body>
</html>
```
- 结果
  - Result 1: 10
  - Result 2: 55
- 第二个结果正是混乱所在
- 原想的可能是加法运算，而在运算符优先级别和过分热心的类型转换这两个因素的共同作用下，结果却被诠释成了字符串连接运算
- 为了避免这种局面，可以对值得类型进行显示转换，以确保执行的是正确的运算

1. 将数值转换为字符串
- 如果想把多个数值类型变量作为字符串连接起来，可以用toString方法将数值转换为字符串

##### 代码清单 5-24 使用Number.toString方法
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-24 使用Number.toString方法</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData1 = (5).toString() + String(5);
            document.writeln("Result: " myda1);
        </script>
      </body>
</html>
```
- 把数值放在括号中然后才调用toString方法
- 因为要想调用number类型定义的toString方法，必须先让JavaScript将字面量转换为一个number类型的值
- 示范了与调用toString方法等效的另一种做法，即调用String函数并将要转换的数值作为参数传递给它
- 这两种做法的作用都是将number类型的值转换为string类型，因此 + 这个运算符会被用来进行字符串连接而不是加法运算
- 结果:
  - Result: 55
- 将数值转换为字符还有一些别的方法(表 5-3 数值到字符串的常用转换方法)

##### 表 5-3 数值到字符串的常用转换方法
方法 | 说明 | 返回
:------ | :------
toString | 以十进制形式表示数值 | 字符串
toString(2)、toString(8)、toString(16) | 以二进制、八进制、十六进制形式表示数值 | 字符串
toFixed(n) | 以小数点后有n位数字的形式表示实数 | 字符串
toExponential(n) | 以指数表示法表示数值。尾数的小数点前后分别有1位数字和n位数字 | 字符串
toPrecision(n) | 用n位有效数字表示数值，在必要的情况下使用指数表示法 | 字符串

2. 将字符串转换为数值
- 有时需要把字符串转换为数值，以便进行加法运算而不是字符串连接。这可以用Number函数办到

##### 代码清单 5-25 将字符串转换为数值
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-25 将字符串转换为数值</title>
    </head>
    <body>
        <script type="text/javascript">
            var firstVal = "5";
            var secondVal = "5";

            var result = Number(firstVal) + Number(secondVal);
            document.writeln("Result: " + result);
        </script>
    </body>
</html>
```  
- 结果: 
  - Result: 10
- Number函数解析字符串值的方式很严格
- 在这方面parseInt和parseFloat函数更为灵活，后面这两个函数还会忽略数字字符串后面的非数字字符

##### 表 5-4 字符串到数值的常用转换函数
函数 | 说明
:------ | :------
Number(`<str>`) | 通过分析指定字符串，生成一个整数或实数值
parseInt(`<str>`) | 通过分析指定字符串，生成一个整数值
parseFloat(`<str>`) | 通过分析指定字符串，生成一个整数或实数值

### 5.6 使用数组
- JavaScript数组的工作方式与大多数编程语言中的数组类似

##### 代码清单 5-26 创建和填充数组
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title> 5-26 创建和填充数组</title>
    </head>
    <body>
        <script type="text/javascript">
            var myArray = new Array();
            myArray[0] = 100;
            myArray[1] = "Adam";
            myArray[2] = true;
        </script>
    </body>
</html>
``` 
- 例子中通过调用new Array()创建一个新的数组
- 这是一个空数组，它被赋值给myArray
- 后面的语句给数组中的几个索引位置设置了值
- 此例子有几处说明一下:
  1. 首先，创建数组的时候不需要声明数组中元素的个数，JavaScript数组会自动调整大下以便容纳所有元素
  2. 不必声明数组所含数据的类型。JavaScript数组可以混合包含各种类型的数据

#### 5.6.1 使用数组字面量
- 使用数组字面量，可以在一条语句中创建和填充数组

##### 代码清单 5-27 使用数组字面量
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>5-27 使用数组字面量</title>
    </head>
    <body>
      <script type="text/javascript">
      var myArray = [100, "Adam", true];
      </script>
    </body>
</html>
```
- 此例通过在一对方括号[]之间指定所需数组元素的方式创建了一个新数组，并将其赋给变量myArray

#### 5.6.2 读取和修改数组内容
- 要读取指定索引位置的数组元素之，应使用一对方括号[]并将索引值放在方括号间
- JavaScript数组的索引值从0开始

##### 代码清单 5-28 读取指定索引位置的数组元素值
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-28 读取指定索引位置的数组元素值</title>
    </head>
    <body>
        <script type="text/javascript">
            var myArray = [100, "Adam", true];
            document.writeln("index 0: " + myArray[0]);
          </script>
        </body>
</html>
```
- 要修改JavaScript数组中指定位置的数据，只消将新值赋给该索引位置的数组元素即可
- 与普通变量一样，改变数组元素的数据类型没有任何问题

##### 代码清单 5-29 修改数组内容
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-29 修改数组内容</title>
    </head>
    <body>
        <script type="text/javascript">
            var myArray = [100, "Adam", true];
            myArray[0] = "Tuesday";
            document.writeln("Index 0: " + myArray[0]);
          </script>
        </body>
</html>
```
- 将一个字符串赋值给了数组第0位的元素，该元素原来保存的是一个数值

#### 5.6.3 枚举数组内容
- 可以用for循环数组内容

##### 代码清单 5-30 枚举数组内容
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-30 枚举数组内容</title>
    </head>
    <body>
        <script type="text/javascript">
            var myArray = [100, "Adam", true];
            for (var i = 0, i < myArray.length; i++) {
              document.writeln("Index " + i + ":" + myArray[i]);
            }
          </script>
        </body>
```
- JavaScript中的循环语句的工作方式与大多数语言中的类似
- 要确定数组中的元素个数可以使用length属性
- 代码输出结果:
  - Index 0: 100  Index 1: Adam  Index 2: true

#### 5.6.4 使用内置的数组方法
- JavaScript中的Array对象定义了许多方法
- 表 5-5 常用数组方法

##### 表5-5 常用数组方法
方法 | 说明 | 返回
:------ | :------ | :------
concat(`<otherArray>`) | 将数组和参数所指数组的内容合并为一个新数组。可指定多个数组 | 数组
join(`<separator>`) | 将所有数组元素连接为一个字符串。各元素内容用参数制定的字符分隔| 字符串
pop() | 把数组当做栈使用，删除并返回数组的最后一个元素 | 对象
push(`<item>`) | 把数组当做栈使用，将指定的数据添加到数组中 | void
reverse() | 就地反转数组元素的次序 | 数组
shif() | 类似pop，但操作的是数组的第一个元素 | 对象
slice(`<start>,<end>`) | 返回一个子数组 | 数组
sort() | 就地对数组元素排序 | 数组
unshift(`<item>`) | 类似push，但新元素被插到数组的开头位置 | void

### 5.7 处理错误
- JavaScript用try...catch语句处理错误

##### 代码清单 5-31 异常处理
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-31 异常处理</title>
    </head>
    <body>
      <script type="text/javascript">
          try {
            var myArray;
            for (var i = 0; i < myArray.length; i++) {
                document.writeln("Index " + i + ": " + myArray[i]);
            }
          } catch (e) {
            document.writeln("Error: " + e);
          }
      </script>
    </body>
</html>
```
- 这个脚本中的问题：试图使用未恰当初始化的变量
- 可能会引发错误的代码被包装在try字句中
- 如果没有发生错误，那么try字句中语句的执行将立即停止，控制权转移到catch子句中
- 发生的错误由一个Error对象描述，它会被传递给catch子句

##### 表 5-6 Error对象
属性 | 说明 | 返回
:------ | :------ | :------
message | 对错误条件的说明 | 字符串
name | 错误的名称，默认为Error | 字符串
number | 该错误的错误代号(如果有的话) | 数值

- catch 子句提供了一个从错误中恢复或在错误发生后进行一些清理工作的机会
- 如果不管是否发生错误都执行一些语句，那么可以加上一条finally子句并将它们置于其中

##### 代码清单 5-32 使用finally子句
```html
<!DOCTYPE HTML>
<html>
    <head>
      <title>5-32 使用finally子句</title>
    </head>
    <body>
      <script type="text/javascript">
          try {
            var myArray;
            for (var = i, i < myArray.length; i++) {
              document.writeln("Index " + i + ":" + myArray[i]);
            }
          } catch (e) {
              document.writeln("Error " + e);              
          } finally {
              document.writeln("statements here are always execued");
          }
        </script>
      </body>
</html>
```

### 5.8 比较 undefined 和 null 值
- JavaScript中有两个特殊值: undefined 和 null， 在比较它们的时候需要留心
- 在读取未赋值的变量或试图读取对象没有的属性时得到的就是undefined值

###### 代码清单 5-33 特别的undefined值
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-33 特别的undefined值</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
              name: "Adam",
              weather: "sunny",
            };
            document.writeln("prop " + myData.doesntexist);
        </script>
    </body>
</html>
```
- 结果:
  - Prop: undefined
- JavaScript怪就怪在又定义了一个特殊值null，这个值与undefined略有不同
- undefined在未定义值得情况下得到的值
- null则用于表示已经赋了一个值但该值不是一个有效的object、string、number或boolean值(也就是说所定义的是一个无值[no value])

##### 代码清单 5-34 使用undefined和null
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title> 5-34 使用undefined和null</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
              name: "Adam",
            };

            document.writeln("Var: " + myData.weather);
            document.writeln("Prop: " + ("weather" in myData));

            myData.weather = "sunny";
            document.writeln("Var: " + myData.weather);
            document.writeln("Prop: " + ("weather" in myData));

            myData.weather = null;
            document.writeln("Var: " + myData.weather);
            document.writeln("Prop: " + ("weather" in myData));
          </script>
    </body>
</html>
```
- 例子中创建了一个对象，然后试图读取其weather属性，而该属性在这段代码的开头部分尚为定义:
```html
            document.writeln("Var: " + myData.weather);
            document.writeln("Prop: " + ("weather" in myData));
```
- 此时weather属性还不存在，因此表达式myData.weather的值为undefined，而且in关键字判断对象是否具有这个属性时得到的结果是flase。这两条语句的输出结果如下:
  - Var: undefined
  - Prop: flase
- 随后给weither属性赋值了一个值，其效果是将该属性添加到对象中:
```html
            myData.weather = "sunny";
            document.writeln("Var: " + myData.weather);
            document.writeln("Prop: " + ("weather" in myData));
```
- 现在重新读取该属性的值并看看对象是否有值了
  - Var: sunny
  - Prop: true
- 接下来，把该属性的值设置为null:
```html
            myData.weather = null;
            document.writeln("Var: " + myData.weather);
            document.writeln("Prop: " + ("weather" in myData));
```
- 其作用很明确: 对象依然具有该属性，但程序员表示它没有值
- 结果如下:
  - Var: null
  - Prop: true

##### 5.8.1 检查变量或属性是否为undefined或null
- 如果想检查某属性是否为null或undefined(不管是哪一个)，那么只要使用if语句和逻辑非运算(!)即可

##### 代码清单 5-35 检查属性是否为null或undefined
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-35 检查属性是否为null或undefined</title>
    </head>
    <body>
        <script type="text/javascript">
            var myData = {
                name: "Adam",
                city: null
            };

            if (!myData.name) {
                document.writeln("name IS null or undefined");
            } else {
                 document.writeln("name IS NOT null or undefined");
            }

            if (!myData.city) {
               document.writeln("city IS null or undefined");
            } else {
                 document.writeln("city IS NOT null or undefined"); 
            }

          </script>
        </body>
</html>
```
- 这种方法借助了JavaScript执行的类型转换，有了这中转换，例中检查的值会被当做布尔值处理
- 如果变量或属性为null或undefined， 则转换而得到的布尔值为false

#### 5.8.2 区分 null 和 undefined
- 在比较两个值时，所用办法应视需要而定
- 如果想同等对待undefined值和null值，那么应该使用相等运算符(==)，让JavaScript进行类型转换
- 此时值为undefined的变量会被认为与值为null的变量相等
- 如果要区分null和undefined，则应使用等同运算符(===)

#### 代码清单 5-36 null和undefined值得相等和等同比较
```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>5-36 null和undefined值得相等和等同比较</title>
    </head>
    <body>
        <script type="text/javascript">
            var firstVal = null;
            var secondVal;

            var equality = firstVal == secondVal;
            var identity = firstVal === secondVal;

            document.writeln("Equality: " + equality);
            document.writeln("Identity: " + identity);
          </script>
    </body>
</html>
```
- 脚本输出结果
  - Equality: true
  - Identity: false

### 5.9 常用的JavaScript工具
- 可用来简化javaScript编程工作

#### 5.9.1 使用JavaScript调试器
- Chrome
- Firefox的Firebug

#### 5.9.2 使用JavaScript库
- [JQuery](http://jquery.com)
- [Dojo](http://dojotoolkit.org)

### 5.10 小结
- JavaScript核心特性
- JavaScript是HTML5的有机组成部分
- 非常有必要掌握一些这门语言的基础知识和用法