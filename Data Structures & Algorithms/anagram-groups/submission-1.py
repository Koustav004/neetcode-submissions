class Solution:
    def groupAnagrams(self, strs):
        anagram = {}

        for words in strs:
            count = [0] * 26
            for char in words:
                key = ord(char) - ord('a')
                count[key] += 1
            index = tuple(count)


            if index not in anagram:
                anagram[index] = []

            anagram[index].append(words)
        return list(anagram.values())
