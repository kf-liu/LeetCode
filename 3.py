class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s)<2:
      return len(s)
    l=1
    i=0
    for j in range(1,len(s)):
      if s[j] in s[i:j]:
        if j-i > l:
          l=j-i
        i+=s[i:j].index(s[j])+1
    if j-i+1 > l:
      l=j-i+1
    return l
#68s,97.7%
