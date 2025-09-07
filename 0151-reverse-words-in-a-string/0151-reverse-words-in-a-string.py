class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        results = s.split()
        results = results[::-1]

        return ' '.join(results)
        