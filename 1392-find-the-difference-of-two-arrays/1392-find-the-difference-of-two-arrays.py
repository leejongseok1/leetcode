class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        s_nums1 = set(nums1)
        s_nums2 = set(nums2)

        return [list(s_nums1-s_nums2), list(s_nums2-s_nums1)]

        # tmp1, tmp2 = [], []
        # answer = []

        # for i in range(len(nums1)):
        #     if nums1[i] not in nums2:
        #         tmp1.append(nums1[i])
            
        #     if nums2[i] not in nums1:
        #         tmp2.append(nums2[i])

        # answer.append(list(set(tmp1)))
        # answer.append(list(set(tmp2)))
            
        # return answer
        