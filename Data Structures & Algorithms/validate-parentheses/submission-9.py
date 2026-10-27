class Solution:
    def isValid(self, s: str) -> bool:
        n= []
        o = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in o:
                if n and n[-1] == o[c]:
                    n.pop()
                else:
                    return False
            else:
                n.append(c)
        return True if not n else False