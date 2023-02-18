from classes.DbMongo import DbMongo

class Student:

    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.__collection = "estudiante"

    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()

    def update_student(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        #collection.set(self.last_name.__dict__)
        #collection.update_one({'name':"Pedrito"}, { "$set": {'last_name':"zambo"}})

        collection.update_one({'name':self.name}, { "$set": {'last_name':self.last_name}}) #By giving the argument name, the method update_one updates the argument last_name
        client.close()
