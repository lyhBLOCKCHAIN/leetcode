class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        k=k%length
        nums.extend(nums[:length-k])
        del nums[:length-k]