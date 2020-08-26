# 结构模式-装饰器模式  & 结构模式-代理模式
## 前言
由于装饰器模式和代理模式在python中很常见，而且两者的代码实现也非常相似，所以把他们放在一起进行讲解<br/>
但是，需要注意，这两个是不同的设计模式，它们有着各自不同的作用<br/>
## 意图
### 装饰器模式
1、在不改变接口的输入的前提下，为接口增加额外的功能或处理<br/>
2、
### 代理模式
1、为接口提供权限或处理流程的控制<br/>
## 适用性
## 场景
## 优缺点
## 实现
下面的demo会展示两个函数修饰器（代理）的实现<br/>
实现过程中使用了wraps来保持被修饰对象属性的一致性<br/>
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