from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap
        anagram_map = defaultdict(list)

        # iterate through the given list
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())