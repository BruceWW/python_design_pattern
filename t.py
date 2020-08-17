#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/8/8
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        while k > 0:
            if num not in arr:
                k -= 1
            num += 1
        return num

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        import collections
        lack = []
        for i in range(len(s)):
            gap =  ord(t[i]) - ord(s[i])
            if gap<0:
                gap = 26+gap
                lack.append(gap)
            elif gap !=0:
                lack.append(gap)

        nums = collections.Counter(lack)
        for key, value in nums.items():
            if key != 0 and ((value - 1) * 26 + key) > k:
                return False
        return True

    def minInsertions(self, s: str) -> int:
        res = 0
        left_num = 0
        right_num = 0
        for i in range(len(s)):
            if s[i]=='(':
                if right_num !=0:
                    if left_num !=0:
                        res +=1
                        right_num=0
                    else:
                        res +=2
                        right_num = 0
                        left_num+=1
                else:
                    left_num +=1
            elif s[i]==')':
                right_num+=1
                if right_num == 2:
                    if left_num == 0:
                        res +=1
                        right_num = 0
                    else:
                        left_num -=1
                        right_num=0
            if left_num==1 and right_num ==2:
                left_num=0
                right_num=0
        if right_num >0:
            m = right_num%2
            if m !=0:
                if left_num>0:
                    left_num -=1
                    res +=1
                else:
                    res +=2
            res += right_num //2
        res += 2*left_num
        return res

    def longestAwesome(self, s: str) -> int:
        import collections
        if not s:
            return 0
        left = 0
        right = len(s)
        res = 1
        while left < right:
            nums = collections.Counter(s[left:right])
            ji = 0
            for value in nums.values():
                if value % 2 != 0:
                    ji += 1
                if ji == 2:
                    left_num = nums[s[left]]
                    right_num = nums[s[right - 1]]
                    if left_num % 2 == 0:
                        if right_num % 2 == 0:
                            if left_num < right_num:
                                left += 1
                                continue
                            else:
                                right -= 1
                                continue
                        else:
                            right -= 1
                            continue
                    else:
                        if right_num % 2 == 0:
                            left += 1
                            continue
                        else:
                            if left_num < right_num:
                                left += 1
                                continue
                            else:
                                right -= 1
                                continue
            if ji <=1:
                res = max(res, (right - left))
                left_num = nums[s[left]]
                right_num = nums[s[right - 1]]
                if left_num < right_num:
                    left += 1
                else:
                    right -= 1
        return res

if __name__ == '__main__':
    obj = Solution()
    # obj.findKthPositive([2,3,4,7,11],5)
    # print(obj.canConvertString("atmtxzjkz","tvbtjhvjd",35))
    # print(obj.minInsertions("()()()()()))"))
    print(obj.longestAwesome('3242415'))