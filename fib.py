
# coding: utf-8

# <img src="http://2.bp.blogspot.com/-H2m-BFydExw/Wkc9gJQE8GI/AAAAAAAAcZI/pJhLUIEj9zMe2fmVsQuK2UWFbrVagaongCK4BGAYYCw/s0/%25E6%2588%2590%25E5%258A%259F%25E9%2581%258E%25E7%25A8%258B.png"
# style="width:100px;height:100px;float:left"><br/><br/><br/><br/><br/>  
# ### 專案名稱: python測試  
# ### 功能描述: 費式數列
# ### 版權所有: Dunk  
# ### 程式撰寫: Dunk  
# ### 參考網址: https://www.runoob.com/python3/python3-module.html
# ### 撰寫日期：2020/02/18
# ### 改版日期:  
# ### 改版備註:  

# In[2]:

def fib(n):
    """定义到 n 的斐波那契数列"""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
 
def fib2(n):
    """返回到 n 的斐波那契数列"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result