from config import CURSOR as cus,CONN as c

class Customer():
    all = {}
    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
    @classmethod
    def CREATE_TABLE(cls):
        sql="""CREATE TABLE IF NOT EXISTS Customer (id INTEGER PRIMARY KEY AUTOINCREMENT, customer_id INTEGER, first_name INTEGER, last_name INTEGER)"""
        cus.execute(sql)
        c.commit()
    def save(self):
        sql="""INSERT INTO Customer (customer_id, first_name, last_name) VALUES (?,?,?)"""
        cus.execute(sql, (self.customer_id, self.first_name, self.last_name))
        c.commit()
    @classmethod
    def create(cls,customer_id, first_name, last_name):
        a = cls(customer_id, first_name, last_name)
        a.save()
        return a    
       
       