class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        current = float('inf')
        absCurrent = abs(current)
        for num in nums:
            if abs(num) < absCurrent:
                current = num
            elif num == absCurrent and num > current:
                current = num
            absCurrent = abs(current)
        return current
