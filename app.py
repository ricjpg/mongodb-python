from classes import Student
from dotenv import load_dotenv

def main():
    student = Student("9999999","77777777","5555555")
    #Student.last_name = "eeeeeee"
    student.save()
    
    student.last_name = "dos" #this just change the argument apellido
    student.update_student() #Method that updates the object Student that was recently created 
    #Student.apellido.update()
    #Student.update_student()
    

if __name__ == "__main__":
    load_dotenv()
    main()