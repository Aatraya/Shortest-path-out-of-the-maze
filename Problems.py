class Problem:
    def __init__(self,prb_id,tit,des,cons,testcase,time_l,mem_l):#constructor
        self.problem_id=prb_id #problem id
        self.title=tit #title 
        self.description=des #description
        self.constraint=cons #constraint
        self.testcase=testcase #testcases
        self.time_limit=time_l #time limit
        self.memory_limit=mem_l #memory limit

    