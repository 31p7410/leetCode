"""
# 两数相加

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。请你将两个数相加，并以相同形式返回一个表示和的链表。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

链接：https://leetcode-cn.com/problems/add-two-numbers/
"""

"""
# 加法通用解题逻辑
while A没完 or B没完 or 进位carry
    A 的当前位
    B 的当前位
    和 = A 的当前位 + B 的当前位 + 进位carry
    当前位 = 和 % 10
    进位 = 和 / 10
"""

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None 

class LinkedList():
    def __init__(self, head = None):
        self.head = head
    
    def append(self, val): # 输入val,作为节点插入到末尾
        if val is None:
            return None
        append_node = ListNode(val)
        if self.head is None:
            self.head = append_node
            return append_node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = append_node
        return append_node

def generateLinkedListHeadNode(l1):
    ll = LinkedList()
    for i in l1:
        ll.append(i)
    return ll.head

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry_in = 0 # 进位数
    res_head = ListNode()
    curr_node = res_head # 指向当前 node 的指针
    while l1 or l2 or carry_in:
        sum_i = 0 # l1 和 l2 的每一位相加 再加上进位的和
        if l1:
            sum_i += l1.val
            l1 = l1.next
        if l2:
            sum_i += l2.val
            l2 = l2.next
        if carry_in:
            sum_i += carry_in
        carry_in, sum_i = divmod(sum_i, 10)
        curr_node.next = ListNode(sum_i)
        curr_node = curr_node.next
    return res_head.next

if __name__ == '__main__':
    lh1 = generateLinkedListHeadNode([2,4,3])
    lh2 = generateLinkedListHeadNode([5,6,4])
    res = addTwoNumbers(lh1, lh2) # 模拟加法
    
    while res is not None:
        print(res.val)
        res = res.next
