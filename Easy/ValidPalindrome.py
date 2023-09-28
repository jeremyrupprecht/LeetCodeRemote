# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/submissions/

import string
def isPalindrome(s):
    s = ''.join([char for char in s if char not in string.punctuation]).lower().replace(" ", "")
    for i in range(len(s)):
        o = (len(s)- 1) - i
        if (s[i] != s[o]):
            return False
    return True

if __name__ == "__main__":
    s = "kayak"
    print(isPalindrome(s))