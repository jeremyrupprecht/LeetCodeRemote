def lengthOfLongestSubstring(s):
    hSet = set()
    longest = 0
    l = 0
    for r in range(len(s)):
        while s[r] in hSet:
            hSet.remove(s[l])
            l += 1
        hSet.add(s[r])
        longest = max(longest , r - l + 1)
    return longest

if __name__ == "__main__":
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))
