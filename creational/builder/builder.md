# 创建模式-生成器模式
## 意图
将一个复杂对象的构建与表示分离，调用者只需要调用类中的方法即可一步步组装并在最后返回生成的对象<br/>
使用生成器是的调用者不需要了解复杂对象的组装过程<br/>
生成器与抽象工厂非常类似，但是生成器着重于一步步组合，在最后才返回生成的对象<br/>
## 适用性
1、当创建复杂对象的过程需要独立于对象的组成<br/>
2、调用方不需要知道这些对象之间怎么组合<br/>
## 场景

## 优缺点
1、可以动态的改变一个对象的内部表示<br/>
2、使得构造代码与实现代码分离<br/>
3、由于每产生一种新的对象，都要生成一个新的类，导致子类过多<br/>
## 实现
创建模式中，除了单例模式，其他的模式将全部使用生产一个手机为示例<br/>
PhoneBuilder为一个生成器类，里面定义了四个方法<br/>
分别是为手机生产并添加一套操作系统、为手机生产并添加一个cpu、为手机生产并配置手机信息，返回最终生产出来的手机<br/>
手机空壳已经在初始化方法中创建<br/>
ConcretePhoneBuilder为具体的手机生产类，继承了PhoneBuilder<br/>
生成器不需要调用者对生产的组建进行组装，直接调用生成器的方法，对象生产和组装的过程将在生成器中执行<br/>
```python
from abc import ABCMeta,abstractmethod
from creational.builder.example import Phone
class PhoneBuilder(metaclass=ABCMeta):
    """
    生成器的抽象类，里面提供了所需的抽象方法
    继承了抽象工厂类的子类，需要实现所有抽象方法
    生成器在于一步步进行装配，然后最后返回创建的对象
    """

    def __init__(self):
        """
        在类进行初始化时，就创建一个具体的手机实例，用于装配
        """
        self._phone = Phone()

    @abstractmethod
    def add_cpu(self) -> None:
        """
        向手机实例中装配cpu
        :return:
        """
        pass

    @abstractmethod
    def add_os(self) -> None:
        """
        向手机实例中装配os
        :return:
        """
        pass

    @abstractmethod
    def add_name(self) -> None:
        """
        向手机实例装配置信息
        :return:
        """
        pass

    def get_phone(self):
        """
        返回手机配置完的手机实例
        :return:
        """
        return self._phone


class ConcretePhoneBuilder(PhoneBuilder):
    """
    具体实现生成器的手机类
    """
    def add_os(self):
        """
        生成os，并直接在手机实例中装配os
        :return:
        """
        self._phone.os = 'os'

    def add_cpu(self):
        """
        生成cpu，并直接在手机实例中装配cpu
        :return:
        """
        self._phone.cpu = 'cpu'

    def add_name(self):
        """
        生成手机信息，并直接在手机实例中配置手机信息
        :return:
        """
        self._phone.name = 'name'
```
[具体实现代码](./example/foxconn.py)