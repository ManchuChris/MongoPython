vowel = ['a', 'e', 'o', 'i', 'u']
def solution(s):
    left = 0
    right = len(s) - 1
    res = 0
    while left < right:
        if s[left] in vowel :
           left = left + 1
           res = res + 1
        elif s[right] in vowel:
           right = right - 1
           res = res + 1
        else:
            break
    print("{} and {}".format("left", left))
    print("{} and {}".format("right", right))
    res = res + longestVowelSubstring(s, left, right)
    return res


def longestVowelSubstring(s, left, right):
    res_tmp = 0
    maxlen = 0
    for i in range(left + 1, right):
        if s[i] in vowel:
            if res_tmp == 0:
               res_tmp = 1
            if s[i-1] in vowel:
               res_tmp = res_tmp + 1
            maxlen = max(maxlen, res_tmp)
        else:
            res_tmp = 0
    return maxlen








