#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        item1 = None
        item2 = None

        if not list1 and not list2:
            return None

        while True:
            item1 = list1
            while True:
                item2 = list2

                if item1.val >= item2.val:
                    node2 = ListNode(val=item2.val)
                    if result is None:
                        result = node2
                    else:
                        result.next = node2
                        node2 = None
                else:
                    break
                
                list2 = list2.next
                if item2.next is None:
                    break
            
            node1 = ListNode(val=item1.val)
            if result is None:
                result = node1
            else:
                result.next = node1
                node1 = None
            
            list1 = list1.next
            if item1.next is None:
                break
        
        return result
# @lc code=end

