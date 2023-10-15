def countGoodSubstrings(s):
    longest = 0
    for r in range(2,len(s)):
        if (s[r] != s[r-1] and s[r] != s[r-2] and s[r-1] != s[r-2]):
            longest += 1
    return longest


if __name__ == '__main__':

    s = "xyzzaz"
    s1 = "aababcabc"
    s2 = "abd"
    s3 = ""
    print(countGoodSubstrings(s1))