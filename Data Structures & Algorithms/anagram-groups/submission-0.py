from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map character count tuples to lists of anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create a frequency array for 'a' through 'z'
            count = [0] * 26
            for char in s:
                # Map character to index 0-25 using ASCII values
                count[ord(char) - ord('a')] += 1
                
            # Convert list to an immutable tuple to use as a dictionary key
            anagram_map[tuple(count)].append(s)
            
        # Return all the grouped sublists
        return list(anagram_map.values())