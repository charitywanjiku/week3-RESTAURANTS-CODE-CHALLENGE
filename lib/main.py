from config import  CURSOR ,CONN
from reviews import Review
from customer import Customer
from restaurant import Restaurant
#CURSOR.execute("""DELETE FROM Review """)

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

review = Review.find_by_id(23)
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

# review_instance = Review()
# reviews = review_instance.reviews("","","","")
# Create a Customer instance
# customer = Customer.create(restaurant_id=1, first_name="John", last_name="Doe")

# # Call the favorite_restaurant() method
# favorite_restaurant_info = customer.favorite_restaurant()

# # Print the result
# if favorite_restaurant_info:
#     print("Favorite Restaurant ID:", favorite_restaurant_info['restaurant_id'])
#     print("Favorite Restaurant Name:", favorite_restaurant_info['restaurant_name'])
#     print("Average Star Rating:", favorite_restaurant_info['avg_star_rating'])
# else:
#     print("No favorite restaurant found for this customer.")