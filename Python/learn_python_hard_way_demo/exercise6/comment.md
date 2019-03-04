# Strings and Text

**Study Drills**

- 1

Go through this program and write a comment above each line explaining it.

- 2

Find all the places where a string is put inside a string. There are four places.

``%d``, ``%s``, ``%r`` and ``%r`` in the chactors "Isn't that joke so funny?! %r"


- 3

Are you sure there are only four places? How do you know? Maybe I like lying.

answer: more than 4 places, but other is the same place to use


- Question 4

Explain why adding the two strings w and e with + makes a longer string.
字符串连接可以用+， 也可以用join

- Question 1

What is the difference between %r and %s?


Use the %r for debugging, since it displays the "raw" data of the variable, 
but the others are used for displaying to users.

``%``表示格式化占位符的开始， 用来表示格式化的规则，

``%r`` 表示通过``repr()``内建方法来转化Python对象. 

- Question 2

What's the point of %s and %d when you can just use %r?
The %r is best for debugging, and the other formats are for actually displaying variables to users.

- Question 3

I get the error TypeError: not all arguments converted during string formatting.
You need to make sure that the line of code is exactly the same. 
What happens in this error is you have more % format characters in the string than variables to put in them. 
Go back and figure out what you did wrong.

- Question 4

Why do you put ' (single-quotes) around some strings and not others?
Mostly it's because of style, but I'll use a single-quote inside a string that has double-quotes. 
Look at line 10 to see how I'm doing that.


- Question 5

If you thought the joke was funny could you write hilarious = True?
Yes, and you'll learn more about these boolean values in Exercise 27.