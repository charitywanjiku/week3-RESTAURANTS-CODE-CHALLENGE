from config import CURSOR as cus,CONN as c

class Review:
    all = {}
    def __init__(self, review, customer_id, restaurant_id ,star_rating, id=None) :
        self.id= id
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
    @classmethod
    def instance_from_db(cls, row):
        review= cls.all.get(row[0])

        if review:
         review.review = row[1]
         review.customer_id = row[2]
         review.restaurant_id = row[3]
         review.star_rating = row[4]
        else:
             
            review = cls( row[1], row[2], row[3], row[4])
            review.id = row[0]
            cls.all[review.id] = review
            return review
    # @classmethod
    # def find_by_id(cls, id):
    #     sql="""SELECT * FROM Reviews WHERE id =?"""
    #     cus.execute(sql, (id,))
    #     row = cus.fetchone()
    #     return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_id(cls, id):
        sql = """SELECT * FROM Reviews WHERE id = ?"""
        cus.execute(sql, (id,))
        row = cus.fetchone()
        if row:
            return cls.instance_from_db(row)
        else:
            return None
    

   
    def delete(self) :
        sql="""DELETE FROM Reviews WHERE id =?"""
        cus.execute(sql, (self.id,))
        c.commit() 
        del type(self).all[self.id]
        self.id= None