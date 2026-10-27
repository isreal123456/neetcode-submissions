class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        op = ["*","/","+","-"]
        n = []
        r = 0
        for i in tokens:
            if i not in op:
                n.append(int(i))
            if i in op:
                b= n.pop()
                a = n.pop()
                if i == "+":
                    n.append(a+b)
                if i == "*":
                    n.append(a*b)
                if i == "/":
                    n.append(int(a/b))
                if i == "-":
                    n.append(a-b)
        return n[0]