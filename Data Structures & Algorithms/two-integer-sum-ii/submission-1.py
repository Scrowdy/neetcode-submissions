class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r=0, len(numbers)-1

        while l < r:
            currentSum = numbers[l] + numbers[r]
            if currentSum > target:
                r-=1
            elif currentSum < target:
                l+=1
            else:
                return [l+1,r+1]
        return []
        # Target = 9
        # 1+11=12  > 9
        # 1+7 =8 < 9
        # 3+7 =10 > 9
        # 3+5 =8 < 9
        # 4+5= 9 