# **Star-Rail---automatic**

*Doing the daily task automaticly*

**打包的方法：**


```
pip install pyinstaller
Pyinstaller -F -i cielo.ico main.py
```


打包完成会有一个dict文件夹，exe文件就在里面

把他复制出来到star rail目录里面就能直接用了（懒得做路径检索）


**初始化坐标的方法：**
运行init.py 文件来更改坐标文件position.npy

 - [ ] 5.11：肝了一晚上的成果，目前来看能用（仅限于我个人），睡了睡了

 - [ ] 5.12: 加入了坐标初始化，可以根据自己的坐标重新设置