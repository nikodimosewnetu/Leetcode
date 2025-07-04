class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexed_nums={}
        for i, num in enumerate(nums):
            num2=target-num
            if num2 in indexed_nums:
                index2=indexed_nums[num2]
                index1=i
                return [min(index1,index2),max(index1,index2)]
            indexed_nums[num]=i
        return []
