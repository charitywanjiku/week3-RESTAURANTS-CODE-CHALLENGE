from config import CURSOR as cus,CONN as c
from reviews import Review
# from restaurant import Restaurant


class Customer():
    all = {}
    def __init__(self, restaurant_id, first_name, last_name):
        
        self.restaurant_id = restaurant_id
        self.first_name = first_name
        self.last_name = last_name
    @classmethod
    def CREATE_TABLE(cls):
        sql="""CREATE TABLE IF NOT EXISTS Customer (id INTEGER PRIMARY KEY AUTOINCREMENT, restaurant_id INTEGER, first_name INTEGER, last_name INTEGER)"""
        cus.execute(sql)
        c.commit()
    @classmethod
    def DROP_TABLE (cls):
        sql="""DROP TABLE IF EXISTS Customer"""
        cus.execute(sql)
        c.commit()   
    def save(self):
        sql="""INSERT INTO Customer (restaurant_id, first_name, last_name) VALUES (?,?,?)"""
        cus.execute(sql, (self.restaurant_id, self.first_name, self.last_name))
        c.commit()
    @classmethod
    def create(cls,  restaurant_id, first_name, last_name):
        a = cls( restaurant_id, first_name, last_name)
        a.save()
        return a  
    @classmethod
    # create customer instance from the database row
    def instance_from_db(cls, row):
        # check if instance already exists
        customer= cls.all.get(row[0])

        if customer:
        #  update existing instance
         customer.restaurant_id = row[1]
         customer.first_name = row[2]
         customer.last_name = row[3]
       
        else:
             #create a new instance
            customer = cls( row[1], row[2], row[3])
            customer.id = row[0]
            cls.all[customer.id] = customer
            return customer
    @classmethod
    def find_by_id(cls, id):
        sql="""SELECT * FROM Customer WHERE id =?"""
        row = cus.execute(sql, (id,)).fetchone()
        
        return cls.instance_from_db(row) if row else None
    def delete(self) :
        # delete customer from the database
        sql="""DELETE FROM Customer WHERE id =?"""
        cus.execute(sql, (self.id,))
        c.commit() 
        # remove  instance from the dictionary
        del type(self).all[self.id]
        self.id= None
    @classmethod
    def customer_full_name(cls, id):
        sql="""SELECT first_name,last_name FROM Customer WHERE id = ?"""
        full_name = cus.execute(sql, (id,)).fetchone()
        if full_name:
            first_name,last_name = full_name
            print (first_name + "" + last_name)
        else:
            print ("Customer not found")
    def reviews(self):
        # Retrieve all reviews left by the customer
        sql = """SELECT * FROM Reviews WHERE customer_id = ?"""
        cus.execute(sql, (self.id,))
        rows = cus.fetchall()
        # Create Review instances from database rows
        reviews = [Review.instance_from_db(row) for row in rows]
        return reviews        
    # def favorite_restaurant(self):
    #     sql = """
    #         SELECT r.id AS restaurant_id, r.name AS restaurant_name, AVG(rv.star_rating) AS avg_star_rating
    #         FROM Reviews rv
    #         JOIN Customer c ON rv.customer_id = c.id
    #         JOIN Restaurants r ON rv.restaurant_id = r.id
    #         WHERE c.id = ?
    #         GROUP BY r.id, r.name
    #         ORDER BY avg_star_rating DESC
    #         LIMIT 1;
    #     """
    #     # Execute the SQL query with the customer's ID as parameter
    #     cus.execute(sql, (self.restaurant_id))
    #     row = cus.fetchone()

    #     # Check if any data is retrieved
    #     if row:
    #         restaurant_id, restaurant_name, avg_star_rating = row
    #         return {'restaurant_id': restaurant_id, 'restaurant_name': restaurant_name, 'avg_star_rating': avg_star_rating}
    #     else:
    #         return None
    

    