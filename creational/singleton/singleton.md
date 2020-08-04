# 创建模式-单例模式
## 意图
 保证一个类只有一个实例
## 适用性
 1、类只能有一个或有限个数的实例<br/>
 2、单例的实现与具体的类无关<br/>
## 场景
 1、日志输出文件<br/>
 2、应用配置<br/>
 3、DB实例<br/>
## 优缺点
### 1、可以增强对类的访问控制：
 由于单例模式下，类只能有一个或有限个数的实例，所以它们可以被严格地控制如何访问或使用<br/>
### 2、缩小命名空间：
 单例模式实际上是对全局变量的一种优化，可以避免过多的全局变量存储以及全局变量命名冲突<br/>
### 3、实例属性的意外变化
 由于单例模式下，一个类只能有一个或有限个数的实例，对象可能在不同环节被调用时导致属性值变化，从而影响执行结果<br/>
## 实现
python中有多种单例模式的实现，这里主要讲解4种<br/>
之前的几种创建模式都使用手机作为案例，这里我们转变一下思路，采用公民和国籍作为案例，因为每个公民的国籍都是唯一的，而且每个国籍对应的国家也是唯一的，不能因为多次实例化而产生多个实例<br/>
### 1、__new__方法
__new__方法本身是python类内置的魔术方法，用于类的实例化，功能类似于c++的构造函数<br/>
下面的例子创建了一个类，并实现了它的__new__方法<br/>
在__new__方法执行过程中，程序会有限判断类种是否有_instance这个属性<br/>
如果没有这个属性，则调用super方法创建一个实例，并将返回的实例赋予属性_instance<br/>
如果有这个属性，则说明这个类之前已经被调用且被实例化，直接返回属性的内容<br/>
```python
class SingletonByNewMethod(object):
    """
    使用构造函数实现单例
    所有继承的子类在执行构造函数时，自动执行单例创建　
    这里的思路使用了懒汉模式
    """

    def __new__(cls, *args, **kwargs):
        # 判断类变量中是否有singleton属性
        if not hasattr(cls, '_instance'):
            # 如果没有singleton属性，则调用super方法，创建一个实例并赋予singleton属性
            cls._instance = super().__new__(cls, *args, **kwargs)
            print('return instance by created')
            return cls._instances
        else:
            print('return instance from class attribute')
            return cls._instances
```
[具体实现代码](./example/new_method.py)<br/>


### 2、修饰器方法
修饰器在很多编程语言中都有类似的功能或使用，在python中使用尤为方便<br/>
但是我们这里实现的方式虽然叫修饰器，但实际上应该属于代理模式，两者具体的区别会在修饰器模式和代理模式中详细讲解<br/>
修饰器方法有两种使用方式，分别是函数修饰器和类修饰器<br/>
函数修饰器代码如下<br/>
```python
def singleton_proxy(cls):
    """
    使用函数装饰器
    这里使用了python的修饰器方法
    同时python的修饰器方法，使用了典型的面向函数编程闭包思想
    :param cls: 需要实例化的类
    :return:
    """
    # 用于存储已实例话的对象
    _instances = {}

    def inner(*args, **kwargs):
        # 调用外部函数的变量判断传入的类是否已经被实例化
        if cls in _instances:
            print('return instance from outer attribute')
            return _instances[cls]
        else:
            _instances[cls] = cls(*args, **kwargs)
            print('return instance by created')
            return _instances[cls]

    return inner
```
[具体实现代码](./example/method_proxy.py)

类修饰器代码如下<br/>
```python
class SingletonProxy(object):
    """
    使用类装饰器
    这里使用了python的修饰器方法，但实际上这个属于代理模式，所以使用proxy命名
    """

    def __init__(self, cls):
        """
        类装饰器初始化函数
        :param cls: 需要实例化的类
        """
        self._cls = cls
        self._instances = {}

    def __call__(self, *args, **kwargs):
        """
        类装饰器需要实现__call__方法，用于自身的调用
        :param args:
        :param kwargs:
        :return:
        """
        if self._cls in self._instances:
            print('return instance from class proxy attribute')
            return self._instances[self._cls]
        else:
            self._instances[self._cls] = self._cls(*args, **kwargs)
            print('return instance by created')
            return self._instances[self._cls]
```
[具体实现代码](./example/class_proxy.py)

### 3、元类方法
python中一切皆为对象，而元类是python中一个特殊的对象，它实际上是定义类的类<br/>
使用元类将覆盖类的__init__方法和__new__方法，直接在类的实例化时保证单例实现<br/>
```python
class SingletonMetaClass(type):
    """
    元类，即创建类的类
    使用元类在对象实例化时实现单例操作
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print('return instance by created')
            cls._instances[cls] = super().__call__(cls, *args, **kwargs)
            return cls._instances[cls]
        else:
            print('return instance from metaclass')
            return cls._instances[cls]
```
[具体实现代码](./example/meatclass.py)


### 4、import方法
通过在特定文件中声明并实例化一个对象<br/>
在其他文件中通过import的方式饮用这个被实例化的对象以实现单例的调用<br/>
由于这种方式比较简单，且不满足单例模式的第二个优点，这里不进行讲解<br/>

