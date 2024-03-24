from config import CURSOR as cus,CONN as c

class Review:
    all = {}
    def __init__(self, review, customer_id, restaurant_id ,star_rating) :
        self.review = review
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.star_rating = star_rating
        
    @classmethod
    def CREATE_TABLE(cls):
        sql="""CREATE TABLE IF NOT EXISTS Reviews (id INTEGER PRIMARY KEY AUTOINCREMENT,review TEXT, customer_id INTEGER, restaurant_id INTEGER, star_rating INTEGER)"""
        cus.execute(sql)
        c.commit()
   
  
    def save(self):
        sql="""INSERT INTO Reviews (review, customer_id, restaurant_id, star_rating) VALUES (?,?,?,?)"""
        cus.execute(sql, (self.review, self.customer_id, self.restaurant_id, self.star_rating))
        c.commit()
    @classmethod
    def create(cls,review, customer_id, restaurant_id ,star_rating): 
        a = cls(review, customer_id, restaurant_id, star_rating)
        a.save() 
        return a   
