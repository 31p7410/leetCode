"""
# 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

"""
# 窗口滑动
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    search_table = ""
    res_len_list = [0] # 所有不重复的子串长度
    for i in s:
        if i not in search_table:
            search_table = search_table + i
        else:
            res_len_list.append(len(search_table))
            search_table = search_table.split(i)[1] + i
    res_len_list.append(len(search_table))
    print(max(res_len_list))
    return max(res_len_list) 

if __name__ == '__main__':
    lengthOfLongestSubstring("")
    lengthOfLongestSubstring(" ")
    lengthOfLongestSubstring("dvdf")
    lengthOfLongestSubstring("abcabcbb")
    lengthOfLongestSubstring("pwwkew")
    lengthOfLongestSubstring("aaaaaaaa")
