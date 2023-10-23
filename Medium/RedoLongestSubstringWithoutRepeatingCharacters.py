# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    longest = 0
    currentLongest = 0
    Dict = {}
    l = 0
    for r in range(len(s)):

        Dict[s[r]] = Dict.get(s[r], 0) + 1
        currentLongest += 1

        while (r - l + 1) > len(Dict.keys()): # if window length equals set length --> only unqiue elements 
            if Dict[s[l]] > 1:
                Dict[s[l]] -= 1
            else:
                Dict.pop(s[l])
            l += 1
            currentLongest -= 1

        longest = max(currentLongest, longest)

    return longest

if __name__ == "__main__":
    s = "abcabcbb"
    s1 = "bbbbb"
    s2 = "pwwkew"
    s3 = "abcdefghjkonm"
    s4 = "aab"
    print(lengthOfLongestSubstring(s4))