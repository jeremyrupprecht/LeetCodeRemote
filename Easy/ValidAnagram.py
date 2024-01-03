# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

import string
def isPalindrome(s, t):
    if len(s) != len(t):
        return 
    Dict = {}
    for i in range(len(s)):
        if (s[i] in Dict):
            Dict[s[i]] += 1
            if (Dict[s[i]] == 0):
                Dict.pop(s[i])
        else:
            Dict[s[i]] = 1

        if (t[i] in Dict):
            Dict[t[i]] -= 1
            if (Dict[t[i]] == 0):
                Dict.pop(t[i])
        else:
            Dict[t[i]] = -1
    if not Dict:
        return True
    return False

if __name__ == "__main__":
    s = "anagram"
    t = 'nagaram'
    s1 = 'rat'
    t1 = 'car'
    s2 = 'kayak'
    t2 = 'ayakk'
    print(isPalindrome(s2, t2))