# 结构模式-装饰器模式  & 结构模式-代理模式
## 前言
由于装饰器模式和代理模式在python中很常见，而且两者的代码实现也非常相似，所以把他们放在一起进行讲解<br/>
但是，需要注意，这两个是不同的设计模式，它们有着各自不同的作用<br/>
## 意图
### 装饰器模式
1、在不改变接口的输入的前提下，为接口增加额外的功能或处理<br/>
### 代理模式
1、为接口提供权限或防伪的控制<br/>
顾名思义，代理模式其实就是调用一个代理去操作实际被操作的对象<br/>
在这个代理中，提供了一些权限或其他功能的控制<br/>
## 适用性
### 装饰器模式
1、不改变对象的情况下，可以动态地给对象添加职责或额外的功能<br/>
2、不能采用生成子类的方式进行功能的扩展<br/>
## 代理模式
1、一个对象在不同的地址空间提供局部的映射<br/>
2、当一个对象的创建或调用需要很大的开销，只有在必须使用的情况下，才执行对象的创建或调用（类似于懒加载）<br/>
3、一个对象的调用需要收到相应的权限控制<br/>
4、一个对象的使用需要有额外的操作<br/>
## 场景
### 装饰器模式
1、python collections模块中的lru_cache方法<br/>
2、
### 代理模式
1、web项目中，不同路由的权限管控以及调用记录跟踪<br/>
2、浏览器渲染页面时，对于大型的图片，先提供一个占位符，当用户将页面浏览到对应位置时，再加载图片<br/>
3、重载运算符，以提供相关权限或其他控制<br/>
4、flask、fatsapi等web框架中的路由注册修饰器<br/>
## 优缺点
### 装饰器模式
1、相对于继承的方式，更加灵活，可以使被添加的功能和原有功能进行分离<br/>
2、避免过多的子类生成<br/>
3、对于被修饰的对象本身没有任何依赖<br/>
4、从代码结构上，对不熟悉代码的人会有一定的困扰
### 代理模式
1、对被操作原始对象提供保护<br/>
## 对比
两种模式在实现方面，尤其是使用python的修饰器方式实现时，整体结构非常相似<br/>
但是<br/>
装饰器模式主要目的是给对象动态地添加职责<br/>
而代理模式则是控制对象的访问<br/>
## 实现
下面的demo会使用修饰器来实现装饰器模式<br/>
同时重载运算符，给运算添加一个权限控制，来实现代理模式<br/>
实现过程中使用了wraps来保持被修饰对象属性的一致性<br/>

两种修饰器<br/>
由于装饰器的实现方式在之前的创建模式以及很多地方都有使用，这里不再进行详细讲解<br/>
偷个懒，继续用单例模式里面的demo<br/>
```python
from functools import wraps


def function_decorator(func):
    """
    函数修饰器，修饰器不接受其他参数
    :param func:
    :return:
    """
    # 使用wraps修饰器，将被修饰函数的属性赋予修饰器
    @wraps(func)
    def inner(*args, **kwargs):
        """
        修饰器内部函数
        :param args:
        :param kwargs:
        :return:
        """
        # 修饰器添加的相关逻辑
        func(*args, **kwargs)
        # 修饰器添加的相关逻辑

    return inner


def function_decorator_with_params(*args, **kwargs):
    """
    修饰器函数，修饰器接受其他参数
    :param args:
    :param kwargs:
    :return:
    """
    def wrapper(func):
        # 使用wraps修饰器，将被修饰函数的属性赋予修饰器
        @wraps(func)
        def inner(*inner_args, **inner_kwargs):
            """
            修饰器内部函数
            :param inner_args:
            :param inner_kwargs:
            :return:
            """
            # 修饰器添加的相关逻辑
            func(*inner_args, **inner_kwargs)
            # 修饰器添加的相关逻辑

        return inner

    return wrapper
```
[具体实现代码](./example/decorator.py)


代理模式，重载运算符，以实现权限控制<br/>
创建了一个Card类，用于表示银行卡，<br/>
其中设置了是否限额、限定额度，余额和本次操作金额四个属性<br/>
重载 + 操作，首先判断是否可以转账，如果可以，则将other的金额转到self中<br/>
重载 - 操作，首先判断是否可以转账，如果可以，则将self的金额转到other中<br/>
```python
class Card(object):
    """
    卡片类
    """

    def __init__(self, name: str, limited: bool = False, limited_num: int = 100000, surplus: int = 0):
        """
        初始化一张卡
        :param limited: 是否限额
        :param limited_num: 限额数量
        :param surplus: 余额
        """
        self.name = name
        # 是否限额
        self.limited = limited
        # 限额总数
        self.limited_num = limited_num
        # 余额
        self.surplus = surplus
        # 本次操作的金额
        self.operator_num = 0

    def __add__(self, other) -> bool:
        """
        将other中本次操作的金额转移到self对象中
        即从other中划一部分钱到本卡
        :param other:
        :return:
        """
        # 判断是否可以转账
        if (self.limited and self.surplus + other.operator_num > self.limited_num) or other.surplus - other.operator_num < 0:
            return False
        else:
            # 可以转入
            self.surplus += other.operator_num
            other.surplus -= other.operator_num
            other.operator_num = 0
            return True

    def __sub__(self, other) -> bool:
        """
        将本卡中的一部分钱转到otehr中
        :param other:
        :return:
        """
        # 判断是否可以转账
        if self.surplus - self.operator_num >= 0 and (
                not other.limited or other.surplus + self.operator_num <= other.limited_num):
            self.surplus -= self.operator_num
            other.surplus += self.operator_num
            self.operator_num = 0
            return True
        else:
            return False
```
[具体实现代码](./example/proxy.py)