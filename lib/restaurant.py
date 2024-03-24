from config import CURSOR as cus,CONN as c
class Restaurant():
    all = {}
    def __init__(self, restaurant_id, name, price):
        self.restaurant_id = restaurant_id
        self.name = name
        self.price = price
    @classmethod
    def CREATE_TABLE(cls):
        sql="""CREATE TABLE IF NOT EXISTS Restaurant (id INTEGER PRIMARY KEY AUTOINCREMENT, restaurant_id INTEGER, name TEXT, price INTEGER)"""
        cus.execute(sql)
        c.commit()
    def save(self):
        sql="""INSERT INTO Restaurant (restaurant_id, name, price) VALUES (?,?,?)"""
        cus.execute(sql, (self.restaurant_id, self.name, self.price))
        c.commit()
    @classmethod
    def create(cls,restaurant_id, name, price):
        a = cls(restaurant_id, name, price)
        a.save()
        return a