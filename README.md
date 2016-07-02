# 简要
* 个人通过PyQt5开发的程序(pyqt5+python3.4)
* 通过PyQt5将写好的python脚步在Py2exe下转换成可以在windows下可执行的工具；
    

##`开发说明：`

    1、安装python3.4
        设置环境变量3.4版本为默认
    2、安装PyQt5
        PyQt5 Desinger设计ui界面
    3、通过pip安装py2exe
        【开发方式1】：运行test_PyQt5.bat，进行ui转换和py转exe并运行测试
        【PyQt5.base】：基础版本，PyQt5+Py2exe+Eric+Python3.4
    4、eric6-6.1.4
        可以通过Eric开发更方便；
        通过eric6.py运行（第一次配置：
        1.点击编辑器->自动完成->QScintilla。勾上显示单条和使用填充符号。
        2.点击编辑器->API。语言：选择python3。
        然后从C:\Python34\Lib\site-packages\PyQt5\qsci\api\python导入eric6.api，点击编译api，点击ok）
        【开发方式2】：在eric6中直接进入PyQt5 Desinger，回到eric 6将刚才的界面文件编译，py2exe打包成exe文件
    

[以上软件下载地址](http://pan.baidu.com/s/1c1GVhgk "百度云盘")

`编译过程`如下图：

![py2exe.bat批处理](https://github.com/liaohw/PyQt/blob/master/EncodeConv/res/py2exe.jpg)

## PyQt5.base
* 基础模板

## EncodeConv
* py2exe.bat批处理，通过ui生成界面代码，并生成可执行工具dist\EncodeConv.exe；
* EncodeConv.py实现了编码格式转换逻辑；
    执行过程如下图：
![EncodeConv.exe执行](https://github.com/liaohw/PyQt/blob/master/EncodeConv/res/runExe.jpg)

## ContactsApp