# 创建模式-抽象工厂
## 意图
提供一个类并实现一些接口，用来创建一系列相关或者依赖的对象<br/>
抽象工厂与生成器非常相似，但是抽象工厂做重点在于直接返回需要产生的对象，并由调用者进行组装<br/>
抽象工厂经常与工厂方法一起使用<br/>
## 适用性
1、创建一个复杂的对象，而这个复杂对象由一系列相关的对象组成<br/>
2、这个复杂对象独立于它的组合对象进行创建<br/>
## 场景
1、生成一套互相关联的实例，例如windows系列窗口组件、mac系统窗口组件等<br/>
## 优缺点
1、一个类提供不同接口生成不同对象，保证了最终生成对象的一致性<br/>
2、由于使用接口封装具体对象的生成，使具体的类与调用方实现了分离<br/>
3、确定类之后，不再需要选择接口<br/>
4、由于每产生一种新的对象，都要生成一个新的类，导致子类过多<br/>
## 实现
创建模式中，除了单例模式，其他的模式将全部使用生产一个手机为示例<br/>
PhoneFactory为一个抽象工厂类，里面定义了四个方法<br/>
分别是生产一个空壳手机、生产一套操作系统、生产一个cpu、配置手机信息<br/>
为了节约代码，生产一个空壳手机已经预先实现，其他三个接口定义为抽象接口<br/>
ConcretePhone为具体的手机生产类，继承了PhoneFactory<br/>
以操作系统为例，ConcretePhone类生产的手机操作系统为iOS11<br/>
如果要生产操作系统为iOS12的手机，则需要重新定义一个类，修改os的返回<br/>
另外抽象工厂直接返回直接返回已经生成的对象，需要由调用者自行组装生成最后的对象<br/>
```python
from abc import ABCMeta,abstractmethod
from creational.abstract_factory.example import Phone
class PhoneFactory(metaclass=ABCMeta):
    """
    抽象工厂类，里面提供了所需的抽象方法
    继承了抽象工厂类的子类，需要实现所有抽象方法
    抽象工厂着重于一个系列的产品创建，创建的对象直接返回
    """

    @staticmethod
    def phone():
        """
        直接返回一个新建的手机实例
        可以理解为一个空手机
        :return:
        """
        return Phone()

    @abstractmethod
    def os(self) -> str:
        """
        操作系统
        :return:
        """
        pass

    @abstractmethod
    def cpu(self) -> str:
        """
        手机cpu
        :return:
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """
        手机名称
        :return:
        """
        pass


class ConcretePhone(PhoneFactory):
    """
    具体实现抽象工厂的手机类
    可以理解为一个具体的手机
    """

    def os(self) -> str:
        """
        返回concrete phone的操作系统，（返回的操作系统是一个已经实现的整体）
        :return:
        """
        return 'iOS11'

    def cpu(self) -> str:
        """
        返回concrete phone的cpu，（返回的cpu是一个已经实现的整体）
        :return:
        """
        return 'cpu'

    def name(self) -> str:
        """
        返回concrete phone的信息，（返回的手机信息是一个已经实现的整体）
        :return:
        """
        return 'name'
```
这里的demo同时使用的工厂模式
[具体实现代码](./example/foxconn.py)