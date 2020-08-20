# 结构模式-适配器模式
## 意图
将一个类的接口转换成另一个接口，可以是入参和出参的改变<br/>
适配器模式用于解决由于接口入参或出参问题导致的不兼容情况<br/>
一般情况下，适配器模式更多的是处理已有的但是不兼容的类，而桥接模式则是在设计时就考虑兼容性的问题<br/>
## 适用性
1、使用一个已经存在的但是接口不符合要求的类（一般是参数数量、或类型不同，由于python是动态类型语言，一般不存在类型不兼容的问题）<br/>
2、希望扩展已有类的兼容性<br/>
3、重新定义一个兼容现有调用方式的接口比较困难或复杂<br/>
4、多个不同的调用方需要调用同一个不兼容的对象时，可以使用双向适配器<br/>
## 场景
1、面向对象编程里面的多态一定程度上是一种适配器<br/>
2、已有的一个软件，可以在A系统中运行，现在需要移植到B系统，而且B系统的调用方式与A系统不同<br/>
## 优缺点
1、提升已有类及其接口的兼容性<br/>
2、使用适配器时需要考虑不同接口之间对接的复杂性<br/>
## 实现
适配器一般有三个对象：<br/>
target：客户端调用的特定方式的接口<br/>
adaptee：已经存在的接口，需要适配器进行适配<br/>
adapter：适配器，将adaptee的接口适配为target可调用的方式<br/>
适配器中adapter需要同时继承target和adaptee两个类，而且adaptee类需要私有继承<br/>
由于python没有私有继承，所以ProgramAdaptee类的方法被定义为私有方法<br/>
以AlphaTarget为例，<br/>
Alpha系统上传用户信息的方法为upload，接受两个参数表示经纬度，类型为字符串<br/>
由于adaptee类的接受的参数类型为浮点类型，所以需要adapter进行适配处理<br/>
```python
from abc import abstractmethod
from structural.adapter.example import ProgramAdaptee


class AlphaTarget(object):
    """
    Alpha系统
    """
    @abstractmethod
    def upload(self, lon: str, lat: str):
        """
        alpha系统调用的函数名称为upload，入参是lon和lat，类型是字符串
        :param lon:
        :param lat:
        :return:
        """
        pass


class ProgramAlphaAdapter(ProgramAdaptee, AlphaTarget):
    """
    Alpha系统的适配器，继承两个类
    Program类为适配器的被适配方（adaptee），提供数据上传服务
    AlphaTarget为适配器的目标方（target），提供被调用的接口，并重写接口的逻辑来调用被适配方的函数
    """
    def upload(self, lon: str, lat: str):
        """
        Alpha系统调用的接口传入的经纬度为字符串类型，需要修改类型后再调用adaptee的方法
        重写target的方法，实现类型的转换以打到适配器的目的
        :param lon:
        :param lat:
        :return:
        """
        # 将字符串转为浮点型，并调用_location方法
        self._location(float(lon), float(lat))
``` 
[具体实现代码](./example/main.py)
