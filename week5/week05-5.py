# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = [] #先把a設定成很小的、短短的矩陣list
        while head != None:
            a.append(head.val) # 先把head的那串東西,轉換成陣列A
            head = head.next
        #print(a) #先印出陣列,等一下可以刪掉    
        N = len(a)#先印出法陣
        for i in range(N):# a有多少數字, i就照迴圈跑
           if a[i] != a[N-1-i] : return False #頭尾不同
        return True #先亂寫
        