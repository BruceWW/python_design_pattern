# 创建模式-工厂模式
## 意图
定义好固定的流程，根据传入的属性或对象来创建不同的对象
工厂模式经常与抽象工厂一起使用
## 适用性
1、
## 场景

## 优缺点
1、
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