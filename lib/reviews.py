from config import CURSOR as cus,CONN as c

class Review:
    # dictionary to show all instances of Review
    all = {}
    # INITIALIZE ALL ATTRIBUTES
    def __init__(self, review, customer_id, restaurant_id ,star_rating, id=None) :
        self.id= id
        self.review = review
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.star_rating = star_rating
        
    @classmethod
    def CREATE_TABLE(cls):
        #create review tables if not exists
        sql="""CREATE TABLE IF NOT EXISTS Reviews (id INTEGER PRIMARY KEY AUTOINCREMENT,review TEXT, customer_id INTEGER, restaurant_id INTEGER, star_rating INTEGER)"""
        cus.execute(sql)
        c.commit()

        
   
  #save instances to the database
    def save(self):
        sql="""INSERT INTO Reviews (review, customer_id, restaurant_id, star_rating) VALUES (?,?,?,?)"""
        cus.execute(sql, (self.review, self.customer_id, self.restaurant_id, self.star_rating))
        c.commit()
    @classmethod
    #create a new review instance and save it in the database
    def create(cls,review, customer_id, restaurant_id ,star_rating): 
        a = cls(review, customer_id, restaurant_id, star_rating)
        a.save() 
        return a  
    @classmethod
    # create review instance from the database row
    def instance_from_db(cls, row):
        # check if instance already exists
        review= cls.all.get(row[0])

        if review:
        #  update existing instance
         review.review = row[1]
         review.customer_id = row[2]
         review.restaurant_id = row[3]
         review.star_rating = row[4]
        else:
             #create a new instance
            review = cls( row[1], row[2], row[3], row[4])
            review.id = row[0]
            cls.all[review.id] = review
            return review
    @classmethod
    def find_by_id(cls, id):
        sql="""SELECT * FROM Reviews WHERE id =?"""
        row = cus.execute(sql, (id,)).fetchone()
        
        return cls.instance_from_db(row) if row else None
 

    def delete(self) :
        # delete review from the database
        sql="""DELETE FROM Reviews WHERE id =?"""
        cus.execute(sql, (self.id,))
        c.commit() 
        # remove  instance from the dictionary
        del type(self).all[self.id]
        self.id= None
    def reviews(self):
        # Retrieve all reviews left by the customer
        sql = """SELECT * FROM Reviews WHERE customer_id = ?"""
        cus.execute(sql, (self.id,))
        rows = cus.fetchall()
        # Create Review instances from database rows
        reviews = [Review.instance_from_db(row) for row in rows]
        return reviews
    
