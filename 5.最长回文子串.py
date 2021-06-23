"""
# 最长回文子串

给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

链接：https://leetcode-cn.com/problems/longest-palindromic-substring/
"""

"""
马拉车算法
中心扩展 : 算出以下标index为中心的字符向两边扩展的臂长
参考连接 https://www.cxyxiaowu.com/2665.html
"""

class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        index_arm_len = []
        max_right_index = -1
        max_right_center_index = -1 # max_right 对应的中心
        for index in range(len(s)):
            if max_right_index >= index:
                mirror_index = 2 * max_right_center_index - index
                min_index_arm_len = min(index_arm_len[mirror_index], max_right_index - index)
                current_index_arm_len = self.expand(s, index - min_index_arm_len, index + min_index_arm_len)
            else:
                current_index_arm_len = self.expand(s, index, index)
            index_arm_len.append(current_index_arm_len)

            if index + current_index_arm_len > max_right_index:
                max_right_center_index = index
                max_right_index = index + current_index_arm_len # 最右的下标更新

            if 2 * current_index_arm_len + 1 > end - start: # 判断以下标为index的字符为中心的回文串的长度,如果比之前记录的大,更新
                start = index - current_index_arm_len
                end = index + current_index_arm_len

        return s[start+1:end+1:2]
