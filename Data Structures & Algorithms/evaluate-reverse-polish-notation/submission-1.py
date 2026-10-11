
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        p = 0
        op = ['+', '-', '*', '/']

        for i in tokens:
            if i not in op:
                l.append(int(i))

            if i in op:
                b = l.pop()
                a = l.pop()

                if i == "+":
                    p = a + b
                if i == "*":
                    p = a * b
                if i == "-":
                    p = a - b
                if i == "/":
                    p = int(a / b)

                l.append(p)

        p = l.pop()
        return p
