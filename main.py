import pandas as pd
from customer import Customer
from product import Product
from shopping_mall import ShoppingMall
import random
from CONSTANTS import CURRENT_YEAR
import jdatetime
from operator import add
import matplotlib
import matplotlib.pyplot as plt


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
    product_length = len(product_names)

    for i in range(product_length):
        name = product_names[i]
        price = random.randint(100_000, 5_000_000)

        product = Product(
            product_name=name,
            product_price=price,
            product_id=i+1
        )

        mall.add_product(product=product)


def change_product_price(product: Product, new_price: float, date: jdatetime.date) -> None:
    """Change a product price"""
    product.change_product_price(new_price=new_price, date=date)


def customer_buy_random(mall: ShoppingMall) -> None:
    """Random customers buy random products"""
    for i in range(10_000):
        customer = random.choice(mall.customers)
        product = random.choice(mall.products)

        day = random.randint(1, 29)
        month = random.randint(1, 12)
        year = random.randint(1400, CURRENT_YEAR)

        mall.customer_buy_product(
            customer=customer,
            product=product,
            date=jdatetime.date(
                year=year,
                month=month,
                day=day
            )
        )


def each_month(product: str, mall: ShoppingMall) -> None:
    """See each month purchase of a product"""
    final_result = [0] * 12
    for customer in mall.customers:
        result = customer.purchase_each_month_of_year(product=product)
        final_result = list(map(add, final_result, result))

    return final_result


def create_purchase_diagram(purchases: list, time: list):
    """
    Create a diagram of purchases and times
    """
    plt.bar(time, purchases, color='#47071e')
    plt.xlabel('Month')
    plt.ylabel('Purchases')


if __name__ == '__main__':
    # Create random customers
    shopping_mall = ShoppingMall()
    create_products(mall=shopping_mall)
    create_random_customers(mall=shopping_mall)
    customer_buy_random(mall=shopping_mall)

    #mall.show_customers()
    #mall.show_products()
    shopping_mall.show_purchases()

    product_name = input(
        'Please enter a product name to see products sells each month for a year: '
    )
    purchases_each_month = each_month(product=product_name, mall=shopping_mall)
    # A list of purchases in last year
    # Each index shows the month index
    last_year_purchase = purchases_each_month

    print(last_year_purchase)

    create_purchase_diagram(
        purchases=last_year_purchase,
        time=[i for i in range(1, 13)]
    )
    plt.show()
