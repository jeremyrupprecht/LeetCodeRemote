# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

def isPalindrome(s):
    if len(s) == 1:
        return True
    cleanedString = "".join(ch for ch in s if ch.isalnum()).lower()
    l = 0
    r = len(cleanedString) - 1
    while (l < r):
        if cleanedString[l] != cleanedString[r]:
            return False
        l += 1
        r -= 1
    return True

if __name__ == "__main__":

    s = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = "k.a.y.a.k"
    s4 = " "
    s5 = "a b      a"
    s6 = "ab_a"
    print(isPalindrome(s5))