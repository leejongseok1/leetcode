class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        str1 = []
        idx1 = []

        for i in range(len(s)):
            if s[i] in vowels:
                str1.append(s[i])
                idx1.append(i)

        str1 = str1[::-1]

        for i in range(len(idx1)):
            s[idx1[i]] = str1[i]

        return ''.join(s)


            


