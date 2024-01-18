# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def lengthOfLongestSubstring(s):
    longest = 0
    Dict = {}
    numUniqueElems = 0
    L = 0
    R = 0
    while R < len(s):
        if s[R] in Dict: 
            Dict[s[R]] += 1
        else:
            Dict[s[R]] = 1
            numUniqueElems += 1
        
        while (numUniqueElems != (R - L + 1)):
            if s[L] in Dict:
                if Dict[s[L]] > 1:
                    Dict[s[L]] -= 1
                else:
                    Dict.pop(s[L])
                    numUniqueElems -= 1
            L += 1
        longest = max(longest, (R - L + 1))
        R += 1
    return longest
 

if __name__ == "__main__":
    s = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s4 = "abaaaaaaaaaaaaaaaaaaaacde"
    print(lengthOfLongestSubstring(s4))
