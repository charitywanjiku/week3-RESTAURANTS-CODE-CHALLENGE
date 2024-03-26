from config import  CURSOR ,CONN
from reviews import Review
from customer import Customer
from restaurant import Restaurant
#CURSOR.execute("""DELETE FROM Customer """)

Review.CREATE_TABLE()
# Review.create("GOOD",1,1,2)
Customer.DROP_TABLE()
Customer.CREATE_TABLE()
Customer.create(1,"John", "Doe")
Customer.create(2,"mary", "raved")
Restaurant.DROP_TABLE()
Restaurant.CREATE_TABLE()
Restaurant.create( "Movenpick", 100)
Restaurant.create( "Westwood", 200)
Restaurant.create( "Fourpoint", 300)
Restaurant.create( "Billionaires", 400)
Restaurant.create( "Intigator",500)

review = Review.find_by_id(1)

review = Review.find_by_id(9)
if review:
    review.delete()
    print("Review deleted successfully")
else:

    print("Review not found")

customer = Customer.find_by_id(1)
if customer:
    customer.delete()
    print("Customer deleted successfully")
else:

    print("Customer not found")
restaurant = Restaurant.find_by_id(1)
if restaurant:
    restaurant.delete()
    print("Restaurant deleted successfully")
else:

    print("Restaurant not found")
Restaurant.restaurant_fanciest()
Customer.customer_full_name(2)