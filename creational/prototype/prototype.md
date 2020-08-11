# 创建模式-原型模式
## 意图
基于原型实例，通过拷贝进行对象的创建<br/>
## 适用性
1、当一个对象初始化时，需要消耗大量资源或步骤比较繁杂<br/>
## 场景
1、python重的copy函数（python中copy、deepcopy建议了解一下）<br/>
## 优缺点
1、快速创建一个新的实例<br/>
2、如果需要维护老类，则比较困难<br/>
## 实现
这里我们以手机的Os为例<br/>
当我们需要一个操作系统时怎么办？<br/>
简单，去网上下载个开源的系统，然后换个启动界面，直接就是自己开发的操作系统了。。。<br/>
好了，那么操作系统有了，要安装到手机上呢？每次都去下载一份？太麻烦，说不定还要科学上网<br/>
不不不，直接基于已经下载的，拷贝一份进去不就好了，于是乎。。。<br/>
我们提供一个Prototype基类，里面定一个clone方法<br/>
其他子类继承这个Prototype，同时实现clone方法，返回克隆的实例<br/>
```python
from abc import abstractmethod, ABCMeta
from copy import deepcopy


class Prototype(metaclass=ABCMeta):
    """
    原型对象使用的基类
    """

    def __init__(self, info: str):
        self._info = info

    @abstractmethod
    def clone(self):
        """
        原型对象使用的copy方法，需要用户进行实现
        :return:
        """
        pass


class Logo(Prototype):
    """
    logo类，继承了原型原型基类
    """
    def __init__(self, info):
        super(Logo, self).__init__(info)

    def clone(self):
        """
        实现clone方法
        :return:
        """
        # 这是一种方法，但是不推荐，你想想，现在只有一个属性，如果有十万个属性呢
        # logo = Logo(self._info)
        # return logo
        # python中建议使用deepcopy实现
        return deepcopy(self) 
```
[具体实例代码](./example/foxconn.py)
