from config import  CURSOR ,CONN
from reviews import Review
from customer import Customer
from restaurant import Restaurant
Review.CREATE_TABLE()
Review.create("GOOD",1,1,2)
Customer.CREATE_TABLE()
Customer.create(1,"John", "Doe")
Customer.create(1,"mary", "raved")
Restaurant.CREATE_TABLE()
Restaurant.create(1, "Pizza", 100)

# Find review by ID
review = Review.find_by_id(1)

# Delete the review if found
if review:
    review.delete()
    print("Review deleted successfully")
else:
    print("Review not found")

