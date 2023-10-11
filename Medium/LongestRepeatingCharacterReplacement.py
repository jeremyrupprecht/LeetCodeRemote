
def characterReplacement(s, k):
    longest = 0
    elemDict = {}
    l = 0
    for r in range(len(s)):
        elemDict[s[r]] = elemDict.get(s[r], 0) + 1
        while (r - l + 1) - max(elemDict.values()) > k:
            elemDict[s[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)
    return longest



if __name__ == "__main__":
    s = "ABAB"
    s1 = "A"
    s2 = "AABABBBA"
    s3 = "AAA"
    s4 = "ABAA"
    k = 2
    print(characterReplacement(s1, k))
