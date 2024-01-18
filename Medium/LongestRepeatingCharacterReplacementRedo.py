# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

def characterReplacement(s, k):
    longest = 0
    Dict = {}
    L = 0
    R = 0
    freqOfMostFreqElem = 0
    mostFreqElem = s[0]
    while R < len(s):
        # add to dict
        if s[R] in Dict:
            Dict[s[R]] += 1
        else:
            Dict[s[R]] = 1

        if Dict[s[R]] > freqOfMostFreqElem:
            freqOfMostFreqElem = Dict[s[R]]
            mostFreqElem = s[R]

        currentLongest = k + freqOfMostFreqElem

        # have extended beyond what we can replace
        while (R - L + 1) > currentLongest:
            if s[L] in Dict:
                if Dict[s[L]] > 1:
                    Dict[s[L]] -= 1
                else:
                    Dict.pop(s[L])

            if s[L] == mostFreqElem:
                freqOfMostFreqElem -= 1
                # can safely search the dict for a new most freq element
                # b/c s is limited to uppercase englihs letters and 
                # there are only 26 of them --> O(26) = O(1)
                mostFreqElem = max(Dict, key=Dict.get)
                if mostFreqElem != s[L]:
                    freqOfMostFreqElem = Dict[mostFreqElem]

            currentLongest = k + freqOfMostFreqElem
            L += 1

        longest = max(longest, currentLongest)
        R += 1

    if longest > len(s):
        return len(s)

    return longest

if __name__ == "__main__":
    s = "ABAB"
    s2 = "AABABBA"
    s3 = "ABBB"
    s4 = "AB"
    print(characterReplacement(s4, 2))