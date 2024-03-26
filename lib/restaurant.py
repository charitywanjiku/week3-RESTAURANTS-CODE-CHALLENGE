from config import CURSOR as cus,CONN as c
class Restaurant():
    all = {}
    def __init__(self, name, price):
        
        self.name = name
        self.price = price
    @classmethod
    def CREATE_TABLE(cls):
        sql="""CREATE TABLE IF NOT EXISTS Restaurant (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER)"""
        cus.execute(sql)
        c.commit()
    @classmethod
    def DROP_TABLE (cls):
        sql="""DROP TABLE IF EXISTS Restaurant"""
        cus.execute(sql)
        c.commit()       
    
    def save(self):
        sql="""INSERT INTO Restaurant ( name, price) VALUES (?,?)"""
        cus.execute(sql,(self.name, self.price))
        c.commit()
    @classmethod
    def create(cls, name, price):
        a = cls( name, price)
        a.save()
        return a
    @classmethod
    # create review instance from the database row
    def instance_from_db(cls, row):
        # check if instance already exists
        restaurant= cls.all.get(row[0])

        if restaurant:
        #  update existing instance
         
         restaurant.name = row[1]
         restaurant.price = row[2]
       
        else:
             #create a new instance
            restaurant = cls( row[1], row[2])
            restaurant.id = row[0]
            cls.all[restaurant.id] = restaurant
            return restaurant
    @classmethod
    def find_by_id(cls, id):
        sql="""SELECT * FROM Restaurant WHERE id =?"""
        row = cus.execute(sql, (id,)).fetchone()
        
        return cls.instance_from_db(row) if row else None
 

    def delete(self) :
        # delete review from the database
        sql="""DELETE FROM Restaurant WHERE id =?"""
        cus.execute(sql, (self.id,))
        c.commit() 
        # remove  instance from the dictionary
        del type(self).all[self.id]
        self.id= None
    @classmethod
    def restaurant_fanciest (cls): 
        sql="""SELECT * FROM Restaurant ORDER BY price DESC LIMIT 1"""
        row = cus.execute(sql, ()).fetchone()
        result = cls.instance_from_db(row) if row else None
        print (result.name)