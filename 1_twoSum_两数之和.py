class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    k=-1
    while len(nums)>0:
      k+=1
      i = nums[0]
      del nums[0]
      if target - i in nums:
        return [k,k + nums.index(target - i) + 1]
