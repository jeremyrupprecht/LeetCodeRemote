# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    Dict = {}
    for string in strs:
        sortedString = ''.join(sorted(string))
        if (sortedString in Dict):
            Dict[sortedString].append(string)
        else:
            Dict[sortedString] = [string]
    return list(Dict.values())


if __name__ == "__main__":

    strs = ["eat","tea","tan","ate","nat","bat"]
    strs2 = [""]
    strs3 = ["a"]
    print(groupAnagrams(strs3))