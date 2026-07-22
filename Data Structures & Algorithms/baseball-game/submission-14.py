class Solution:
    def calPoints(self, operations: List[str]) -> int:
        self.stack = []
        for i in range(len(operations)):
            if operations[i] == '+':
                self.stack.append(self.stack[-1]+self.stack[-2])
            elif operations[i] == 'D':
                self.stack.append(self.stack[-1]*2)
            elif operations[i] == 'C':
                self.stack.pop()
            else:
                self.stack.append(int(operations[i]))
        return sum(self.stack)
                
            
            