# Variables and Printing

- Question 1

Change all the variables so there is no my_ in front of each one.
Make sure you change the name everywhere, not just where you used = to set them.

- Question 2

Try to write some variables that convert the inches and pounds to centimeters and kilograms.
Do not just type in the measurements. Work out the math in Python.

- Question 3

Search online for all of the Python format characters.

[Python格式化字符串](https://docs.python.org/2/library/stdtypes.html#string-formatting)

- Question 4

Try more format characters. %r is a very useful one. It's like saying "print this no matter what."

``%``表示格式化占位符的开始， 用来表示格式化的规则，

``%r`` 表示通过``repr()``内建方法来转化Python对象. 例如下面的代码：

```Python
space_in_car = 4
print 'space in car: %r' % space_in_car
# it's equals
print 'space in car: ' + repr(space_in_car)
```

类似的格式化操作还有：

``%s`` 使用``str()``内建方法来转化Python对象

``%d`` 转换为整型


### Extra

Python中的String和Unicode类型有一个独特的内建操作符： ``%`` 操作符，通常被称为
字符串格式化，或者插值操作符。使用方式 ``format % values``, 其中format可以是String类型
或者Unicode类型对象，操作符``%``将用values中的值替换format中的所有占位符。

使用有这样的一个限制： format必须是一个单值，而values可以有三种选择

- 单值

```Python
height = 175
print 'You are %d' % height
```

- 元组

```Python
values = (175, 60)
print 'You are %d, %d' % values
```

- 字典

```Python
values ={'height':175, 'weight': 60}
print 'You are %(height)d, %(weight)d' % values
```

**Important**: 注意格式化中的``%(height)d``和其他例子的区别


**Important**: 其实字符串格式操作已经不推荐使用，取而代之的是``string.format()``
使用方式如下：

```Python
height=175
weight=60
print 'You are {0}, {1}'.format(height, weight)
print 'You are {height}, {weight}'.format(height=height, weight=weight)
print 'You are {height}, {weight}'.format(weight=weight, height=height)
```

[format-string-syntax 详细说明](https://docs.python.org/2/library/string.html#format-string-syntax)
