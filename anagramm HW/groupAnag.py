from typing import List 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            # sort the letters in the word to get a unique key
            key = ''.join(sorted(word))
            # add the word to the list of anagrams for the key
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        # return a list of the anagram groups
        return list(anagrams.values())
