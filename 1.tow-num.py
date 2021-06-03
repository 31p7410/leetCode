"""
1. 两数之和

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

链接：https://leetcode-cn.com/problems/two-sum
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_map:dict = {} # 查找表

    for index,num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            print(f"{complement}+{num}={target} index 分别为 {hash_map[complement]} 和 {index}")
            return [complement,num]
        else:
            hash_map[num] = index

twoSum([2,7,11,15], 9)
twoSum([3,2,4], 6)
twoSum([3,3], 6)
