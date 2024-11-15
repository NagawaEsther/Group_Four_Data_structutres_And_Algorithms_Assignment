from collections import defaultdict

#Represents each expense entry
class Expense:
    def __init__(self,date,amount,category):
        self.date=date
        self.amount=amount
        self.category=category
        self.next=None
        
#Manages the linked list of expenses 
class ExpenseManager:
    def __init__(self):
        self.head=None
        
    def add_expense(self,date,amount,category):
        new_expense =Expense(date,amount,category)
        new_expense.next=self.head
        self.head=new_expense
        
#Tracks and categorizes expense
class ExpenseTracker:
    def __init__(self):
        self.manager=ExpenseManager()
        self.category_expenses=defaultdict(list)
    
    def add_expense(self,date,amount,category):
        self.manager.add_expense(date,amount,category)
        self.category_expenses[category].append((date,amount))
    
    def get_total_spending_for_month(self,month):
        current_expense =self.manager.head
        total_spent=0
        while current_expense:
            if current_expense.date.startswith(month):
                total_spent += current_expense.amount
            current_expense = current_expense.next
        return total_spent
    
    def get_expenses_by_category(self,category):
        return self.category_expenses.get(category,[])
    
#Example usage of Expense Tracker
tracker = ExpenseTracker()
    
#Adding sample expenses
tracker.add_expense("2023-10-01",50,"Food")
tracker.add_expense("2023-10-02",20,"Transport")
tracker.add_expense("2023-10-05",100,"Utilities")
tracker.add_expense("2023-10-06",35,"Food")
tracker.add_expense("2023-11-01",75,"Food")
    
    
#Check total spending for october 2023
october_total =tracker.get_total_spending_for_month("2023-10")
print(f"Total spending in october 2023:{october_total}")
    
#View food-related expenses
food_expenses =tracker.get_expenses_by_category("Food")
print("Food-related expenses:")
for expense in food_expenses:
        print(f"on {expense[0]},spent {expense[1]}")
    
    