from config import  CURSOR ,CONN
from reviews import Review
from customer import Customer
from restaurant import Restaurant
Review.CREATE_TABLE()
Review.create("GOOD",1,1,2)
Customer.CREATE_TABLE()
Customer.create(1,"John", "Doe")
Restaurant.CREATE_TABLE()
Restaurant.create(1, "Pizza", 100)