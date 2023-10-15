def countGoodSubstrings(s):
    longest = 0
    wSet = set()
    l = 0
    r = 0
    while r < len(s):

        if (r - l) >= 3:
            wSet.discard(s[l])
            l += 1

        wSet.add(s[r])

        if len(wSet) == 3:
            longest += 1

        r += 1
        print(wSet)

    return longest


if __name__ == '__main__':

    s = "xyzzaz"
    s1 = "aababcabc"
    s2 = "abd"
    s3 = ""
    s4 = "abcd"
    print(countGoodSubstrings(s1))