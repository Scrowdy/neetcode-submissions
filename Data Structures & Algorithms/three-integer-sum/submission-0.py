class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue                          # skip duplicate anchors

            l = i + 1
            r = len(nums) - 1
            target = -nums[i]

            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1                     # skip duplicate l values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1                     # skip duplicate r values

        return result