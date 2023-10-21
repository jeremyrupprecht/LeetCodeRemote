# 1456 Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

def maxVowels(s, k):
    vowels = {"a", "e", "i", "o", "u"}
    Dict = {}
    longest = 0
    longestUpToK = 0
    l = 0
    for r in range(len(s)):
        Dict[s[r]] = Dict.get(s[r], 0) + 1
        if s[r] in vowels:
            longest += 1
        
        while (r - l + 1) > k:
            if Dict[s[l]] > 1:
                Dict[s[l]] -= 1
            else:
                Dict.pop(s[l])
            if s[l] in vowels:
                longest -= 1
            l += 1

        if longest >= k:
            return k
        longestUpToK = max(longest, longestUpToK)
        
    return longestUpToK


if __name__ == "__main__":

    s = "abciiidef"
    s1 = "aeiou"
    s2 = "leetcode"
    k = 3
    print(maxVowels(s2, 3))