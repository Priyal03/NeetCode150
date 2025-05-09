class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:

            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1
            else:
                i += 1
"""
        r=3
        count=[0]*r
        for x in nums:
            count[x]+=1

        i=0
        for x in range(r):
            for _ in range(count[x]):
                nums[i]=x
                i+=1

# Time : O(n). Space : O(r) auxiliary space which is optimal for this problem. Counting Sort 