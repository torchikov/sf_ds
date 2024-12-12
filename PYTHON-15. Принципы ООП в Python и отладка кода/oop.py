class SalesReport():  
    def __init__(self, employee_name):  
        self.deals = []  
        self.employee_name = employee_name  
      
    def add_deal(self, company, amount):   
        self.deals.append({'company': company, 'amount': amount})  
          
    def total_amount(self):  
        return sum([deal['amount'] for deal in self.deals])  
      
    def average_deal(self):  
        return self.total_amount()/len(self.deals)  
      
    def all_companies(self):  
        return list(set([deal['company'] for deal in self.deals]))  
      
    def print_report(self):  
        print("Employee: ", self.employee_name)  
        print("Total sales:", self.total_amount())  
        print("Average sales:", self.average_deal())  
        print("Companies:", self.all_companies())  
      
      
report = SalesReport("Ivan Semenov")  
  
report.add_deal("PepsiCo", 120_000)  
report.add_deal("SkyEng", 250_000)  
report.add_deal("PepsiCo", 20_000)  
  
report.print_report()  

class OwnLogger():
    def __init__(self):
        self.logs = {"info": None, "warning": None, "error": None, "all": None}
        
    def log(self, message, level):
        if self.logs[level] is None:
            self.logs[level] = [message]
        else:
            self.logs[level].append(message)
        
        if self.logs["all"] is None:
            self.logs["all"] = [message]
        else:
            self.logs["all"].append(message)
            
    def show_last(self, level="all"):
        print(self.logs)
        if self.logs[level] is None:
            return None
        else:
            return self.logs[level][-1]
        
        


res = OwnLogger()
res.log(message='System started', level='info')
res.log(message='System started 2', level='info')
res.log(message='Warning message', level='warning')

print(res.show_last())

class Dog():
    
    def bark(self, args):
        return "Bark!"
    
    def give_paw(self, args):
        return "Paw"
