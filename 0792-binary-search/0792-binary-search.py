class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # index = bisect.bisect_left(nums,target)
        # if index<len(nums) and nums[index] == target:
        #     return index
        # else:
        #     return -1

        left=0
        right=len(nums)-1

        while left<=right:

            mid = (left+right)//2

            if nums[mid]==target:
                return mid

            if nums[mid]<target:
                left = mid+1
                
            else:
                right=mid-1

        return -1