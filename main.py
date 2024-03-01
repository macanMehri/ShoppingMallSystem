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


def change_prices_random(mall: ShoppingMall) -> None:
    """Change products prices random"""
    for i in range(10_000):
        product = random.choice(mall.products)
        month = random.randint(1, 12)
        change_product_price(
            product=product,
            new_price=random.randint(100_000, 5_000_000),
            date=jdatetime.date(year=CURRENT_YEAR, month=month, day=1)
        )


def each_month_price(product: Product) -> list:
    """See each month purchase of a product"""
    return product.price_changes_in_year()


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


def customer_purchases(customer: Customer, mall: ShoppingMall) -> list:
    """Customers purchases in a year"""
    final_result = [0] * 12
    for product in mall.products:
        result = customer.purchase_each_month_of_year(product=product)
        final_result = list(map(add, final_result, result))

    return final_result


def each_month(product: Product, mall: ShoppingMall) -> list:
    """See each month purchase of a product"""
    final_result = [0] * 12
    for customer in mall.customers:
        result = customer.purchase_each_month_of_year(product=product)
        final_result = list(map(add, final_result, result))

    return final_result


def create_diagram(purchases: list, time: list, ylabel: str):
    """
    Create a diagram of purchases and times
    """
    plt.bar(time, purchases, color='#47071e')
    plt.xlabel('Month')
    plt.ylabel(ylabel)


if __name__ == '__main__':
    # Create a shopping mall
    shopping_mall = ShoppingMall()
    # Create random products
    create_products(mall=shopping_mall)
    # Create random customers
    create_random_customers(mall=shopping_mall)
    # Customers buy random products
    customer_buy_random(mall=shopping_mall)
    # Change prices randomlly
    change_prices_random(mall=shopping_mall)


    print(
        '1. Show all customers.\n'
        '2. Show all products.\n'
        '3. Show purchased products.\n'
        '4. Find a customer by id.\n'
        '5. Find a product by id.\n'
        '6. Find a product by name.\n'
        '7. Show a product sales diagram.\n'
        '8. Show a customer purchases diagram.\n'
        '9. Show a product price changes diagram.\n'
        '10. Change a product price.\n'
        '0. Exit!'
    )

    order = int(input('Please enter your order: '))
    match order:
        case 1:
            shopping_mall.show_customers()
        case 2:
            shopping_mall.show_products()
        case 3:
            shopping_mall.show_purchases()
        case 4:
            customer_id = int(input('Please enter a customer id: '))
            user_customer = shopping_mall.find_customer_by_id(customer_id=customer_id)
            print(user_customer)
        case 5:
            product_id = int(input('Please enter a product id: '))
            user_product = shopping_mall.find_product_by_id(product_id=product_id)
            print(user_product)
        case 6:
            product_name = input('Please enter a product name: ')
            user_product = shopping_mall.find_product_by_name(product_name=product_name)
            print(user_product)
        case 7:
            product_name = input('Please enter a product name: ')
            user_product = shopping_mall.find_product_by_name(product_name=product_name)
            purchases_each_month = each_month(product=user_product, mall=shopping_mall)
            create_diagram(
                purchases=purchases_each_month,
                time=[i for i in range(1, 13)],
                ylabel='Purchases'
            )
            plt.show()
        case 8:
            customer_id = int(input('Please enter a customer id: '))
            user_customer = shopping_mall.find_customer_by_id(customer_id=customer_id)
            customer_purchese = customer_purchases(customer=user_customer, mall=shopping_mall)
            create_diagram(
                purchases=customer_purchese,
                time=[i for i in range(1, 13)],
                ylabel='Customer purcheses'
            )
            plt.show()
        case 9:
            product_name = input('Please enter a product name: ')
            user_product = shopping_mall.find_product_by_name(product_name=product_name)
            price_changes = each_month_price(product=user_product)
            create_diagram(
                purchases=price_changes,
                time=[i for i in range(1, 13)],
                ylabel='Prices'
            )
            plt.show()
        case 10:
            pass
