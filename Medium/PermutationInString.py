# 567 Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# Note: this is not the MOST optimal solution (gonna do that later)
# but this solution is the most intuitive (and most attainable in an
# interview setting). This solution is also simpler than the most 
# optimal solution, leaving a focus on the concept/pattern of a sliding 
# window which is the focus of the problem

# O(m) + O(26 * n) --> O(n)

""" 
Use a flexible sliding window and 2 dicts, 1 for each
string, with each's frequency of letters. Slide 
the window up, Move R and L based on window length (move 
R if window smaller than s1, move L if window bigger than
s1, return True if window length equals s1 length and 
s1Dict equals s2Dict.

"""


def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s1Dict = {}
    s2Dict = {}                 # this is the current window
    # add s1 to its Dict
    for i in range(len(s1)):
        s1Dict[s1[i]] = s1Dict.get(s1[i], 0) + 1
    #loop w/ sliding window to check for matches
    l = 0
    r = 0
    while r < len(s2):
        wl = r - l + 1
        # if windowLength <= len(s1) --> move R
        # if windowLength > len(s1) --> move L 
        if wl <= len(s1):
            s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1
            r += 1
        else:
            if s2Dict[s2[l]] > 1:
                s2Dict[s2[l]] -= 1
            else:
                s2Dict.pop(s2[l])
            l += 1
        if wl == len(s1) and s1Dict == s2Dict:
            return True
    return False

if __name__ == "__main__":
    s1 = "abc"
    s2 = "xxxxcybadfdd"
    print(checkInclusion(s1, s2))