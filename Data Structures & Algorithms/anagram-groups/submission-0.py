class Solution:
    def groupAnagrams(self, strs):
        Anagrams = {}
        for words in strs:
            count = [0] * 26
            for char in words:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in Anagrams:
                Anagrams[key] = []

            Anagrams[key].append(words)
        return list(Anagrams.values())
                