def letterCombination(digits):
    lib = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'}
    res = []
    def backtrack(i, currStr):
        if len(currStr) == len(digits):
            res.append(currStr)
            return 
        for d in lib[digits[i]]:
            backtrack(i+1, currStr+d)
    if digits:
        backtrack(0, '')
    return res
print(letterCombination('234'))