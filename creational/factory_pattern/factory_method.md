# 创建模式-工厂模式
## 意图
定义好固定的流程，根据传入的属性或对象来创建不同的对象<br/>
工厂模式经常与抽象工厂一起使用<br/>
## 适用性
1、有一批工厂类，提供了相同的接口，可以使用相同的方式进行实例化<br/>
## 场景
1、以django为例，只需要在settings文件中切换数据库引擎，即可使用不同类型的数据库<br/>
## 优缺点
1、提高扩展性，如果要增加一个对象，只需要扩展一个工厂类即可<br/>
2、将对象的组装与产品的内部实现进行结偶，调用者只需要关心接口<br/>
## 实现
这里给了一个最为粗暴的demo<br/>
我们实现一个phone类，同时实现静态方法product，接受一个参数phone_name<br/>
根据传入的phone_name，进行识别并返回对应的对象或实例<br/>
实际应用中，这个过程可能包括很多步骤，也可以接受多个参数，来创建复杂对象，抽象工厂的demo中，对于抽象类的实现就是用了工厂模式<br/>
```python
from creational import Phone
from creational.factory_pattern.example import iPhoneKit, SamsungS20Kit, HuaweiMate30Kit


class Product(object):
    """
    工厂模式
    """

    @staticmethod
    def product(phone_name: str) -> Phone.__subclasses__():
        """
        根据传入的型号名称，返回对应型号的类
        :param phone_name:
        :return:
        """
        if phone_name == 'iphone':
            return iPhoneKit
        elif phone_name == 'samsung':
            return SamsungS20Kit
        elif phone_name == 'huawei':
            return HuaweiMate30Kit
        else:
            return None
```
[具体实现代码](./example/foxconn.py)