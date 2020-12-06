import pandas as pd
import operator

class csv :
    def __init__(self,path):
        self.path=path
        try:
           
            self.data =  pd.read_csv(path)
            #print(self.data.head())
        except FileNotFoundError as ex:
            print(ex)

        print("#################")
    
    def operator_fn(self,op):
        return{
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '<=':operator.le,
            '>=':operator.ge,
            '<':operator.lt,
            '>':operator.gt,
            '=':operator.eq,
            '!=':operator.ne,
        }[op]

    def search_condition(self,df,condition):
        if(not(condition)):
            return self.data
        if(condition[0]=='and'):
            return pd.merge(self.search_condition(df,condition[1]),self.search_condition(df,condition[2]),how='inner')
        if(condition[0]=='or'):
            return pd.merge(self.search_condition(df,condition[1]),self.search_condition(df,condition[2]),how='outer')
        return df[self.operator_fn(condition[0])(df[condition[1]],condition[2])]
    
    def select(self,nodes):
        if(nodes[3]):
            self.data = self.search_condition(self.data,nodes[3])
        if(nodes[4]):
            data=data.sort_values(by=nodes[4])

        if nodes[1][0]=='*':
                    return self.data
                
        if(type(nodes[1]) is list):
            # if(type(nodes[1][0] is int)):
            #     names = list(self.data.columns)
            #     for i in range(len(nodes[1])):
            #         nodes[1][i]=names[nodes[1][i]]
            try:
                
                Selecteddata = self.data[nodes[1]]
                return Selecteddata
            except:
                return "Check Column name"

# s=csv("student.csv")  

# # return data
# print(s.select(('select', '*', 'student', None, None)))

#s.select(('select', '*', 'student', None, None))
#s.select(('select', [0, 1], 'student', ('=', 'first_name', 'Doe'), None))
#s.select(('select', ['id', 'first_name'], 'student', ('=', 'first_name', 'Doe'), None))

