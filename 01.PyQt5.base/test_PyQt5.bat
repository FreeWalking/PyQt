
:编译PyQt5批处理文件

:关闭显示命令，使得所有命令执行前不显示
@ echo off

cd E:\BaiduYunSyncDisk\SyncForBak\GitHub\PyQt\PyQt5.base
e:
echo ----complied pyqt5.ui to *.py
call C:\Python34\Lib\site-packages\PyQt5\pyuic5.bat test.ui -o Ui_test.py


:--------------直接运行
echo ----run test.py
python ./test.py

:--------------python 转换到exe并执行
echo ----py2exe
python setup.py


cd dist
echo ----begin test.exe
test

:pause

