# 结构模式-桥接模式
## 意图
将抽象部分与实现部分分离，使得这两个部分可以独立地实现<br/>
在实现过程中，可以发现桥接模式和适配器模式的逻辑非常相似<br/>
但实际上，桥接模式是在程序设计之初就考虑了实现的解偶以及不同的实现方式<br/>
而适配器则是基于以后的接口进行修改<br/>
两者没有孰优孰劣，只是应对不同的场景<br/>
## 适用性
1、希望抽象和实现进行松耦合，而不是强绑定的关系<br/>
2、抽象的实现不会影响调用<br/>
3、实现类可以动态的变化及扩充<br/>
## 场景
1、以iOS系统的白天和黑夜模式为例，同一个app的窗口渲染同时支持两种方式，根据实时的系统模式进行不同样式窗口的渲染<br/>
2、同一个软件兼容不同版本的系统（甚至不同系统）<br/>
## 优缺点
1、可以分离接口及其实现部分，降低系统的耦合性<br/>
2、可以动态修改实现部分，提高了系统的可扩展性<br/>
## 实现
本来想搞一个扩系统工具包的demo，但是想了很久没有想到合适的例子，所以代码实例中我们只呈现一个比较简单的demo，等有好例子了再行替换<br/>
这里提供一个最直观而且python开发中很常见的一个用法：<br/>
用过强加解密工具包crypto的同学一定会发现，windows系统的包名是pycryptodome，而mac及linux系统的包名是pycrypto<br/>
如果有一个三方模块，依赖了crypto进行加解密，难道要为windows和linux分别写写两个依赖项，然后当两个包发到pypi上？<br/>
不，这里就可以引入桥接的思想，在setup.py文件中，识别当前系统，然后根据不同系统安装不同的crypto模块<br/>
可以参照 [cad](https://pypi.org/project/cad) 这个模块，这个模块中使用了AES加密算法，然后在setup.py中处理了不同系统之间不同依赖的问题<br/>
以下demo纯属yy，绝对不可能雷同<br/>
继续模拟一个软件，在不同系统中，调用系统接口获取设备坐标，并向服务器上传数据
```python
import sys

from structural.bridge.example import ProgramAbstraction, Implementor, mac_system_location, linux_system_location, \
    windows_system_location


class MacImp(Implementor):
    """
    模拟一个mac的implementor
    """

    def get_location(self) -> (float, float):
        """
        mac系统中获取坐标信息
        假设mac系统返回坐标的api为mac_sysytem_location
        返回的坐标为lon和lat，类型为字符串
        :return:
        """
        lon, lat = mac_system_location()
        return float(lon), float(lat)


class LinuxImp(Implementor):
    """
    模拟一个Linux系统的implementor
    """

    def get_location(self) -> (float, float):
        """
        linux系统中获取坐标的信息
        假设linux系统返回坐标的api为linux_system_location
        返回的坐标为一个字符串
        :return:
        """
        lon, lat = linux_system_location().split(',')
        return float(lon), float(lat)


class WindowsImp(Implementor):
    """
    模拟一个Windows系统的Implementor
    """

    def get_location(self) -> (float, float):
        """
        windows系统中获取坐标的信息
        假设windoes系统返回坐标的api为windows_system_location
        返回的坐标为一个字符串
        :return:
        """
        return windows_system_location()


class Program(ProgramAbstraction):
    def _get_imp(self) -> Implementor:
        """

        :return:
        """
        if not self._imp:
            platform = sys.platform
            # 判断当前操作系统
            if platform == 'darwin':
                # mac
                print('system: mac')
                self._imp = MacImp()
            elif platform == 'win32':
                # windows
                print('system: windows')
                self._imp = WindowsImp()
            elif platform == 'linux':
                # linux
                print('system: linux')
                self._imp = LinuxImp()
            else:
                # 其他
                pass
        return self._imp

    def upload(self):
        lon, lat = self._imp.get_location()
        # 执行上传操作
        print(f'get location info lon:{lon}, lat:{lat}')
```
[具体实现代码](./example/main.py)
