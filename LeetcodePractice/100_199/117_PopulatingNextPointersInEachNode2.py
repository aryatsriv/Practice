#117. Populating Next Right Pointers in Each Node II
#Solved
#Medium
#Topics
#Companies
#Given a binary tree
#
#struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
#}
#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
#Initially, all next pointers are set to NULL.
#
# 
#
#Example 1:
#
#
#Input: root = [1,2,3,4,5,null,7]
#Output: [1,#,2,3,#,4,5,7,#]
#Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#Example 2:
#
#Input: root = []
#Output: []
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [0, 6000].
#-100 <= Node.val <= 100
# 
#
#Follow-up:
#
#You may only use constant extra space.
#The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return root
        q=deque()
        q.append(root)

        while q:
            n=len(q)
            cache=[]
            for i in range(n):
                cache.append(q.popleft())

            for i,item in enumerate(cache):
                if i!=n-1:
                    item.next=cache[i+1]
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)

        return root
