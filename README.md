# LeetCode
For Leetcode website
  
  
## Here are something that impressed me
### 2_addTwoNumbers
`Linked list`
```
Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
```
### 3_lengthOfLongestSubstring
When I finished my code，I found out that the way I used is similar to the algorithm called `Sliding window`.
```
for j in range(1,len(s)):            #j traverses
  if s[j] in s[i:j]:                 #condition
    if j-i > l: l=j-i                #sth else，not important
    i+=s[i:j].index(s[j])+1          #i jumps according to the condition above
```
### 5_longestPalindrome
`Central diffusion`(takes too much time) `Dynamic planning`（similar to my code, but not the same） and `Manacher`（extremely similar to KMP）
