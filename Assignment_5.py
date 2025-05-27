class Student:
    def __init__(self, student_id, name, balance):
        self.student_id = student_id
        self.name = name
        self.balance = balance  
   

    def enroll_course(self, course_fee):
        
        self.balance += course_fee
        print(f"{self.name}  New tuition balance: {self.balance}")

    def pay_tuition(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} paid {amount}. New tuition balance: {self.balance}")
        else:
            print("Payment exceeds balance.")

    def display_balance(self):
        print(f"Student {self.name} (ID: {self.student_id}), Tuition Balance: {self.balance}")

class Undergraduate(Student):
    def __init__(self, student_id, name, balance):
        super().__init__(student_id, name, balance)
        
    
class Graduate(Student):
    def __init__(self, student_id, name, balance):
        super().__init__(student_id, name, balance)
        

undergrad = Undergraduate("23/U/5690/EVE", "Jessica Alupo", 26000000)
grad = Graduate("23/U/9001", "Akiteng Josephine", 10000000)

undergrad.display_balance()


undergrad.pay_tuition(1500000)
print()
grad.display_balance()


grad.pay_tuition(5000)