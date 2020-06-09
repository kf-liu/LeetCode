# LeetCode
For Leetcode website
  
  
## 划重点
### 2_addTwoNumbers_两数相加
python中定义`单链表singly-Linked list`
```
Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
```
### 3_lengthOfLongestSubstring_无重复字符的最长子串
When I finished my code，I found out that the way I used is similar to the algorithm called `滑动窗口Sliding window`.Amazing.
```
for j in range(1,len(s)):            #j traverses
  if s[j] in s[i:j]:                 #condition
    if j-i > l: l=j-i                #sth else，not important
    i+=s[i:j].index(s[j])+1          #i jumps according to the condition above
```
### 5_longestPalindrome_最长回文子串
`中央扩散Central diffusion`(takes too much time)   
`动态规划Dynamic planning`（similar to my code, but not the same） and   
`Manacher`（extremely similar to KMP）

### 7_reverse_整数反转
new record： 0ms,100% && 6MB,100%（第三次提交）  
第一次提交：错误；忽略了整数溢出的问题。  
第二次提交：4ms6MB-->0ms6MB；解决的问题在于c++很多语法记忆不清晰，从php搬过来的时候保留了取绝对值abs()分正负讨论，实际上c++的/和%都是不影响符号的。
