
:编译PyQt5批处理文件

:关闭显示命令，使得所有命令执行前不显示
@ echo off

cd E:\BaiduYunSyncDisk\SyncForBak\GitHub\PyQt\AiBrowser
e:
:是否从新生成ui的py
:echo ----complied pyqt5.ui to *.py
:call C:\Python34\Lib\site-packages\PyQt5\pyuic5.bat browser.ui -o Ui_browser.py

:--------------直接运行
echo ----run browser.py
python ./browser.py

:pause