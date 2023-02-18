from classes import Estudiante
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("asdasd","asdasd","asdasd")
    #estudiante.apellido = "eeeeeee"
    estudiante.save()
    
    estudiante.apellido = "dos" #this just change the argument apellido
    estudiante.update_student() #Method that updates the object estudiante that was recently created 
    #estudiante.apellido.update()
    #estudiante.update_student()
    

if __name__ == "__main__":
    load_dotenv()
    main()