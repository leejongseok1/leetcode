class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict1 = {}

        for i in range(len(arr)):
            if arr[i] not in dict1:
                dict1[arr[i]] = 1
            elif arr[i] in dict1:
                dict1[arr[i]] += 1

        return len(dict1.values()) == len(set(dict1.values()))