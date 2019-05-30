#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (36.33%)
# Total Accepted:    26.2K
# Total Submissions: 72K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # total_needle = len(needle)
        # if total_needle == 0 or haystack == needle:
        #     return 0
        
        # if haystack == '':
        #     return -1
        
        # for i in range(len(haystack) - total_needle +1):
        #     if haystack[i:i+total_needle] == needle:
        #         return i
        # return -1


        if not needle:
            return 0

        for i in range(len(haystack)):
            if haystack[i:len(needle)+i] == needle:
                return i

        return -1