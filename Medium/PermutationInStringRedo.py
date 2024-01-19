# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

def checkInclusion(s1, s2):
    s1Dict = {}
    s2Dict = {}

    for s in s1:
        if s in s1Dict:
            s1Dict[s] += 1
        else:
            s1Dict[s] = 1
    L = 0
    R = 0
    while R < len(s2):
        
        if s2[R] in s2Dict:
            s2Dict[s2[R]] += 1
        else:
            s2Dict[s2[R]] = 1

        while ((R - L + 1) > len(s1)):

            if s2[L] in s2Dict:
                if s2Dict[s2[L]] > 1:
                    s2Dict[s2[L]] -= 1
                else:
                    s2Dict.pop(s2[L])
            L += 1

        if s1Dict == s2Dict:
            return True
        
        R += 1

    return False

if __name__ == "__main__":

    # s1 = "abc"
    # s2 = "baxyzabc"

    # s1 = "ab"
    # s2 = "eidbaooo"

    s1 = "ab"
    s2 = "eidblaooo"

    # s1 = "abc"
    # s2 = "bbbca"

    print(checkInclusion(s1, s2))
