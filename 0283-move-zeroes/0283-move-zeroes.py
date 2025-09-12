class Solution(object):
    def moveZeroes(self, nums):
        answer = []
        for n in nums:
            if n != 0:
                answer.append(n)

        answer.extend([0] * (len(nums) - len(answer)))

        for i in range(len(nums)):
            nums[i] = answer[i]
