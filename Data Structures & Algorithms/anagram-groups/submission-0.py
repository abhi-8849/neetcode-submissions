class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for str in strs:
            temp = sorted(str)
            key = "".join(temp)
            if key not in anagram_map:
                anagram_map[key] = [str]
            else:
                anagram_map[key].append(str)

        return list(anagram_map.values())
        