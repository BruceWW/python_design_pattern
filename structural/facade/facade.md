# 结构模式-外观模式
## 意图
为子系统的多个接口定义一个高层接口，以减少用户对子系统不必要的了解，简化子系统的使用<br/>
## 适用性
1、为一个复杂的子系统提供简单的接口<br/>
2、将用户与子系统之间进行结偶，避免业务逻辑与底层逻辑的深度耦合<br/>
## 场景
1、维护大型遗留系统时，一定程度上使用外观模式可以减少新维护者对老系统的认知成本<br/>
## 优缺点
1、减少用户对子系统的了解，减少系统的耦合度<br/>
## 实现
这里提供了一个demo，主要目的是体现外观模式对多个接口及子系统的调用组合<br/>
实现了一个支付工具类，即外观类<br/>
我们这里假设有：<br/>
一个央行存储了所有用户及其开户银行的信息<br/>
每个银行存储了用户的余额<br/>
用户现在有3个操作，分别是：<br/>
创建账户，向银行提交账户创建，并向央行提交用户及开户银行信息<br/>
查询余额，查询开户银行的余额信息<br/>
执行转账，检查转出账户及转入账户的余额及是否有没有完成的转账，并向两个账户的开户银行执行金额转移<br/>
```python
from structural.facade.example.facade import AccountManager


class ViMaPay(object):
    def __init__(self, account_mapping: AccountManager, banks: dict):
        self._account_mapping = account_mapping
        self._banks = banks

    def create_account(self, account_name: str, amount: int, bank: str) -> bool:
        """
        创建账户
        :param account_name: 账户名
        :param amount: 账户金额
        :param bank: 银行名
        :return:
        """
        if bank not in self._banks or amount < 0:
            return False
        else:
            if self._banks[bank].add_account(account_name, amount):
                self._account_mapping.add_account_mapping(account_name, self._banks[bank])
                return True
        return False

    def query(self, account_name: str) -> int:
        """
        查询账户余额
        :param account_name:
        :return:
        """
        bank = self._account_mapping.get_bank_by_account(account_name)
        if bank:
            return bank.get_surplus(account_name)
        else:
            return -1

    def trans(self, source_account: str, target_account: str, amount: int) -> bool:
        """
        执行转账
        外观方法，只需要转出数据和转入数据以及转账金额，不需要知道里面具体的银行类、央行类、用户类的操作接口
        :param source_account: 转出账户
        :param target_account: 转入账户
        :param amount: 转账金额
        :return:
        """
        # 去央行获取用户账户所在银行
        source_bank = self._account_mapping.get_bank_by_account(source_account)
        target_bank = self._account_mapping.get_bank_by_account(target_account)
        # 检查用户所在银行的余额及交易状态
        source_pre = source_bank.pre_trans_in(source_account, amount)
        target_pre = target_bank.pre_trans_out(source_account, amount)
        # 执行交易
        if source_pre and target_pre:
            source_bank.confirm(source_account)
            target_bank.confirm(target_account)
            return True
        else:
            return False

```