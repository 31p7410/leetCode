"""
# 寻找两个正序数组的中位数

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""

"""
# 本题是 "在两个数组中找第 K 个小的数" 的特殊情况
采用二分查找,每一步去掉二分查找中比较结果中小的数组t, k = k - len(t), 直到 k 为 0 为止
"""

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: l[int]
    :type nums2: l[int]
    :rtype: float
    """
    nums1_len, nums2_len = len(nums1), len(nums2)

    def get_kth_element(k: int) -> int:
        index1, index2 = 0, 0 # 最开始两个数组的index都是0
        while k != 0:
            if index1 == nums1_len: # index1 和 nums1 的长度相同,表示 nums1 遍历完成
                return nums2[index2 + k - 1] # 返回 nums2 里第k小的数
            if index2 == nums2_len:
                return nums1[index1 + k - 1]
            if k == 1: # 1//2 = 0 的情况要判断一下
                return min(nums1[index1], nums2[index2])

            new_index1 = min(index1 + k//2 - 1, nums1_len - 1) # 找到每个数组中从现在的下标到第 k//2 的数的下标,如果 k//2 大于数组的长度,下标取数组的长度
            new_index2 = min(index2 + k//2 - 1, nums2_len - 1)
            if nums1[new_index1] <= nums2[new_index2]: 
                k = k - (new_index1 - index1 + 1) # 把小的那段扔掉
                index1 = new_index1 + 1 # 更新 index1
            else:
                k -= (new_index2 - index2 + 1)
                index2 = new_index2 + 1

    n = nums1_len + nums2_len
    if n % 2 == 1: # 奇数向下取整
        return get_kth_element( (n+1) // 2 ) # [0 1 2] n=3 取第2个
    else:
        return ( get_kth_element( n//2 ) + get_kth_element( (n+2)//2 ) ) / 2.0  # [0 1 2 3] n=4 取第2个和第3个的平均数

if __name__ == '__main__':
     print((2+3)/2)
     print(findMedianSortedArrays([1,2], [3,4]))
     print(findMedianSortedArrays([1], [2,3]))
     print(findMedianSortedArrays([1,3], [2]))
     print(findMedianSortedArrays([], [1]))
     print(findMedianSortedArrays([2], []))
     print(findMedianSortedArrays([], [1,2,3,4,5]))
     print(findMedianSortedArrays([1,2,3,4,5], []))
     print(findMedianSortedArrays([100000], [100001]))
     print(findMedianSortedArrays([3], [-2,-1]))
     print(findMedianSortedArrays([1,3], [2]))
     print(findMedianSortedArrays([0,0], [0,0]))
