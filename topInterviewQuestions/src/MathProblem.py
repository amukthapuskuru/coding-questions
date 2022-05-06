class Mathproblem:
    def mathproblem(self,s:str ) -> int:
        dic = {'*' :  }
        stack = []
        for i in s:
            if i =='(' :
                stack.append(i)


res=Mathproblem()
print(res.mathproblem('(4*6)/3'))