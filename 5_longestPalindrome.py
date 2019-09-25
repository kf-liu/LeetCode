class Solution:
  def longestPalindrome(self, s: str) -> str:
    l=len(s)
    r=l
    while r>1:
      for i in range(l-r+1):
        if s[i:i+r]==s[i:i+r][::-1]:
          return s[i:i+r]
      r-=1
    if r>0:
      return s[0]
    return ""
