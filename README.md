# youdao_translation
youdao translation 有道翻译(可多语言切换)

和有道翻译的官网一样的功能，支持多种语言翻译，实现的原理是这样的，首先我们在有道翻译的网页版里，用开发者工具查看翻译的时候post了什么给服务器，然后我们可以看到当点击翻译按钮的时候，会发出请求，将一个json表格POST到服务器，然后再GET结果到浏览器里。所以我们只需模仿这个步骤就能实现到这个功能了。

主要使用库：requests、json、PyQt4

![image](http://i11.tietuku.com/e7ead9ccb6482e64.jpg)
![image](http://i12.tietuku.com/ec260e778dcb6298.png)
