#LeetCode Problem 01

def twoSums(nums, target):
    for u in range(0, len(nums)-1):
        for d in range(u+1, len(nums)):
            if nums[u] + nums[d] == target:
                print( [u,d])
            
twoSums([2,7,11,15], 9)
twoSums([3,2,4], 6)
twoSums([3,3], 6)
