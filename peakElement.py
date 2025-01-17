class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return int(sys.maxsize)
        
        low = 0
        high = len(nums)-1
        
        while low<=high:
            mid= low+(high-low)//2
            
            if (mid == len(nums)-1 or nums[mid] > nums[mid+1]) and (mid == 0 or nums[mid] > nums[mid-1]):
                return mid
            
            elif nums[mid+1]>nums[mid]:
                low=mid+1
                
            else:
                high=mid-1
                
        return 5456
             
            