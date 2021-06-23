"""
# 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0

链接：https://leetcode-cn.com/problems/reverse-integer/
"""

"""
https://leetcode-cn.com/problems/reverse-integer/solution/chi-xiao-dou-li-jie-gong-shi-tui-dao-jav-aauv/
java
class Solution {
    public int reverse(int x) {
        int result = 0;
        int digit = 0;
        while (x != 0) {
            // 超出Integer的最大最小值范围了
            if (result < Integer.MIN_VALUE/10 || result > Integer.MAX_VALUE/10) {
                return 0;
            }
            digit = x % 10;
            x /= 10;
            result = result*10 + digit;
        }
        return result;
    }
}
"""

def reverse(x: int) -> int:
    INT_MAX = 2**31-1
    INT_MIN = -2**31

    result = 0
    digit = 0

    while x != 0:
        # 超出integer的最大最小值
        if result < INT_MIN // 10 + 1 or result > INT_MAX // 10:
            return 0
        digit = x % 10

        # python 中 如果对负数取模, 如 -7%10 = 3, 我们想要矫正为 -7, 因此再 -10, digit = 0就不需要再矫正了
        if x < 0 and digit != 0:
            digit -= 10

        # 注意使用地板除, 直接除会有余数
        x = (x - digit) // 10
        result = result * 10 + digit

    return result 

if __name__ == '__main__':
    print(reverse(2147483647))
