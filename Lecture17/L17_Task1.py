class Employee:
   def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
   @property
   def salary(self):
       return self.__salary
       
   @salary.setter
   def salary(self,value):
       self.__salary = value
       
   @salary.deleter
   def salary(self):
       del self.__salary
        

class Manager(Employee):
	def __init__(self, name, salary, department):
		super().__init__(name, salary)
		self.department = department
         
	def get_info(self):
		print(f"Name is : {self.name}")
		print(f"Department is : {self.department}")
		print(f"Salary is : {self.salary}")
             
         
man1 = Manager("Giorgi", 7500 , "IT")
try:
	print(man1.__salary)
except AttributeError as e:
    print(f"შეცდომა (AttributeError): {e}")
    
man1.get_info()
         
         