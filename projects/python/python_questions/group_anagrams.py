# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#makes no sense atm.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# example solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        print(res)
        for s in strs:
            count=[0] * 26

            for c in s:
                count[ord(c) - ord("a")] +=1


            res[tuple(count)].append(s)

        return list(res.values())
        




#Other solutions:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())