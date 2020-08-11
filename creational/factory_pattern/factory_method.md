# 创建模式-工厂模式
## 意图
定义好固定的流程，根据传入的属性或对象来创建不同的对象
## 适用性
1、
## 场景

## 优缺点
1、
## 实现
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