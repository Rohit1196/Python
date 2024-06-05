 ###Project Bank###

class user():
    def __init__(s,name,gender,salary,uan):
        s.name=name
        s.gender=gender
        s.salary=salary
        s.uan=uan

    def showdetails(s):
        print (f'Name: {s.name}\nGender: {s.gender}\nSalary: {s.salary}\nUAN: {s.uan}')

class bank(user):
    
    def __init__(s,name,gender,salary,uan,balance):
        super().__init__(name,gender,salary,uan)
        s.balance=balance

    def deposite(s,amount):
        s.amount=amount
        s.amount=s.amount+s.balance
        return s.amount

    def withdraw(s,amount):
        s.amount=amount
        if s.amount>s.balance:
            print(f'Insufficient Balance\n{s.balance}')
        elif s.amount>=100 and s.amount<=s.balance:
            s.amount=s.balance-s.amount
            return s.amount
        else:
            print(f'You cannot withdraw less than 100\n{s.balance}')

    def viewbalance(s):
        print(f'UAN: {s.uan}\nBalance: {s.balance}')

    def transfer(s,amount,user):
        s.amount=amount
        s.user=user
                
        if s.amount>s.balance:
            print(f'Insufficient Balance\n{s.balance}')

        elif s.amount>=1 and s.amount<=s.balance:
            s.user=s.amount+s.balance
            s.name=s.balance-s.amount
            print(f'User Balance: {s.user}\nBalance: {s.name}')

        else:
            print(f'You cannot withdraw less than 1\n{s.balance}')


person1=bank('Rohit','male',4200,123,50000)
person2=bank('Deepti','Female',4500,456,35000)
person3=bank('Sonu','Female',1600,789,20000)

       
         
            
        

            
        
