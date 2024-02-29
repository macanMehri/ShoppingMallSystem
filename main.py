import pandas as pd
from customer import Customer
from product import Product
from shopping_mall import ShoppingMall
import random
from CONSTANTS import CURRENT_YEAR


names = [
    'Macan', 'Hadi', 'Amir', 'Hassan', 'Hossein', 'Mehran', 'Mehrdad', 'Soroush',
    'Hassan', 'Mina', 'Mehrane', 'Samira', 'Negin', 'Hadis', 'Arman', 'Ahmad', 'Reza',
    'Hamid', 'Mohammad', 'Mohammadreza', 'Ali', 'Mahmod', 'Negar', 'Sarina', 'Armita'
]

last_names = [
    'Mehri', 'Khani', 'Amiri', 'Hassani', 'Hosseini', 'Mehrani', 'Mehrdadi', 'Soroushi',
    'Hassani', 'Minai', 'Mehranei', 'Samirai', 'Negini', 'Hadisi', 'Armani', 'Ahmadi', 'Rezai',
    'Hamidi', 'Mohammadi', 'Mohammadrezai', 'Asadi', 'Mahmodi', 'Negari', 'Sarinai', 'Armitai'
]

product_names = [
    'Pen', 'Book', 'Keyboard', 'Mouse', 'Laptop', 'Mobile', 'Pencil', 'Pencilcase', 'Highlighter',
    'Candle', 'Laser', 'Marker', 'Manitor', 'Handsfree', 'Headset', 'Trashcan', 'Notepad', 'Camera',
    'Paper', 'Doll', 'Glasses', 'Cup', 'Plate', 'Watch'
]


def create_random_customers(mall: ShoppingMall) -> None:
    """Create random customers for shopping mall"""
    for i in range(1000):
        name = random.choice(names)
        last_name = random.choice(last_names)
        birth_year = random.randint(1300, CURRENT_YEAR)

        customer = Customer(
        first_name=name,
        last_name=last_name,
        birth_year=birth_year,
        customer_id=i+1
        )

        mall.add_customer(customer=customer)


def create_products(mall: ShoppingMall) -> None:
    """Create products for shopping mall"""
    for i in range(len(product_names)):
        name = product_names[i]
        price = random.randint(100_000, 5_000_000)
        
        product = Product(
            product_name=name,
            product_price=price,
            product_id=i+1
        )

        mall.add_product(product=product)


if __name__ == '__main__':
    # Create random customers
    mall = ShoppingMall()
    create_products(mall=mall)
    create_random_customers(mall=mall)

    mall.show_customers()
    mall.show_products()
