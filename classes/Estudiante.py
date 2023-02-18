from classes.DbMongo import DbMongo

class Estudiante:

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__collection = "estudiante"

    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()

    def update_student(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        #collection.set(self.apellido.__dict__)
        #collection.update_one({'nombre':"Pedrito"}, { "$set": {'apellido':"zambo"}})

        collection.update_one({'nombre':self.nombre}, { "$set": {'apellido':self.apellido}}) #By giving the argument nombre, the method update_one updates the argument apellido
        client.close()
