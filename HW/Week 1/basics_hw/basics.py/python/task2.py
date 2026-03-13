class User:
    def __init__(self, name, email, password):
        self.name = name          
        self.email = email        
        self._password = password 
    def set_password(self, password):
     return self._password == password

    def check_password(self, password):
        return self._password == password

    def show_info(self):
         print("Name:", self.name)
         print("Email:", self.email)
        
class Student(User):
          def __init__(self, name, email,password,Level):
                super().__init__(name, email,password) 
                self.Level =  Level
          def show_info(self):
             print(f"Student Name: {self.name}, Email: {self.email}, Level: {self.Level}")
  
class Instructor(User):
         def __init__(self, name, email, password , Specialty):
          super().__init__(name, email,password)
          self.Specialty = Specialty

         def show_info(self):
          print(f"Instructor Name: {self.name}, Email: {self.email}, Specialty: {self.Specialty}")
        
std = Student("Alaa", "Alaa@email.com", "77788","beginner")
Inst = Instructor("Mona", "mona@email.com", "Python","Machine learning")
std.show_info()
Inst.show_info()
print(std.check_password("77788"))


 