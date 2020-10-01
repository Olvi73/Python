# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:34:52 2020

@author: Oliver
"""
#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

def singleNumber1(nums) -> int:
        return sum(set(nums))*2-sum(nums)
    
var=input("输入数字:")
nums=[int (n) for n in var.split(" ")]
print(singleNumber1(nums))

#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现三次。找出那个只出现了一次的元素。

def singleNumber2(nums) -> int:
        return (sum(set(nums))*3-sum(nums))//2
    
var=input("输入数字:")
nums=[int (n) for n in var.split(" ")]
print(singleNumber2(nums))