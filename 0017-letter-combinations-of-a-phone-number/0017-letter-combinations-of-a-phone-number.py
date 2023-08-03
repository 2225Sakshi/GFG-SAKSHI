class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        map_digits ={
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }
        
        output = [""]
        for d in digits:
            tmp = []
            for m  in map_digits[d]:
                for o in output:
                    tmp.append(o+m)
            output = tmp
        return output
        
        
        