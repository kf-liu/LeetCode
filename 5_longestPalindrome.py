class Solution:
  def longestPalindrome(self, s: str) -> str:
    l=len(s)
    if l==0: return ""
    ans=s[0]
    r=1
    i=0
    while True:
      i+=1
      left=int(i/2)+i%2-int(r/2)-r%2
      right=int(i/2)+int(r/2)+r%2
      if right>=l: break
      if s[left]==s[right]:
        if s[left:right+1]==s[left:right+1][::-1]:
          #print(r,s[left:right+1])
          j=1
          while left-j>=0 and right+j<=l-1:
            if s[left-j]==s[right+j]:
              j+=1
              #print(r,j,s[left-j+1:right+j])
            else: break
          ans=s[left-j+1:right+j]
          r=len(ans)
    return ans
#140ms,89.73%
