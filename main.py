from argparse import ArgumentParser
import logging
from customer import Customer
from product import Product
from shopping_mall import ShoppingMall
import random
from CONSTANTS import CURRENT_YEAR
import jdatetime
from operator import add
import matplotlib
import matplotlib.pyplot as plt
import sys


# Logging configuration
logging.basicConfig(filename='Logs.txt')

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


def create_diagram(y: list, x: list, ylabel: str, xlabel: str='Month') -> None:
    """
    Create a diagram of purchases and times
    """
    plt.bar(x, y, color='#47071e', width=0.9)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def create_customer(mall: ShoppingMall) -> None:
    """Create a customer and add to mall customers list"""

    while True:
        first_name = input('Please enter your first name: ').capitalize()
        if not first_name.isdigit() and len(first_name) > 3:
            break
        print('This name is not allowed! Please try again.')

    while True:
        last_name = input('Please enter your last name: ').capitalize()
        if not last_name.isdigit() and len(last_name) > 3:
            break
        print('This last name is not allowed! Please try again.')

    while True:
        birth_year = int(input('Please enter your birthdate year: '))
        if 1300 < birth_year < CURRENT_YEAR:
            break
        print('Entery is not correct! Please try again.')

    # Last id of customers + 1 to create new customer id
    new_customer_id = len(mall.customers) + 1

    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        birth_year=birth_year,
        customer_id=new_customer_id
    )

    mall.add_customer(customer=customer)
    print(customer)



def create_product(mall: ShoppingMall) -> None:
    """This function creates a product and add to mall products"""
    while True:
        product_name = input('Please enter your product name: ')
        if not product_name.isdigit() and len(product_name) > 3:
            break
        print('This name is not allowed! Please try again.')
    while True:
        product_price = float(input('Please enter your product price: '))
        if product_price > 0:
            break
        print('This value is not allowed for price! Please try again.')

    new_product_id = len(mall.products) + 1

    product = Product(
        product_name=product_name,
        product_price=product_price,
        product_id=new_product_id
    )
    mall.add_product(product=product)



def get_info_of_top_five():
    """Returns two lists of top five product names and sales"""
    top_five_purchases = shopping_mall.top_five_sales()
    names = list()
    purchases = list()
    for purchase in top_five_purchases:
        names.append(purchase['Product'].product_name)
        purchases.append(purchase['Purchases'])
    return names, purchases


def get_product_names(mall: ShoppingMall) -> list:
    """Returns a list of product names"""
    result = list()
    for product in mall.products:
        result.append(product.product_name)

    return result


def show_three_diagrams() -> None:
    """
    Shows three diagrams of:
    five most purchased, total number of sales and total money earned
    """
    figure, axis = plt.subplots(1, 3)

    monthly_sale = shopping_mall.each_month_purchases()
    monthly_earning = shopping_mall.each_month_earnings()
    names, purchases = get_info_of_top_five()

    months = list(range(1, len(monthly_sale)+1))

    # For monthly sales
    axis[0].bar(months, monthly_sale)
    axis[0].set_title('Monthly Sales')

    # For monthly earning
    axis[1].bar(months, monthly_earning)
    axis[1].set_title('Monthly Earning')

    # For top five sales
    axis[2].bar(names, purchases)
    axis[2].set_title('Top five sales')

    plt.show()



def pass_arguments():
    """Parses arguments and performs actions based on them."""
    parser = ArgumentParser(add_help=False)
    run_args_help = (
        'Show three diagrams of five most purchased, total number of sales and total money earned.'
    )
    help_args_help = (
        'If you want to see three diagrams you can use -r argument.'
    )
    parser.add_argument('-r', '--report', action='store_true', help=run_args_help)
    parser.add_argument('-h', '--help', action='store_true', help=help_args_help)

    args = parser.parse_args()

    if args.report:
        show_three_diagrams()
    elif args.help:
        parser.print_help()




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


    if len(sys.argv) > 1:
        pass_arguments()
        sys.exit()



    while True:
        print(
            '1. Show all customers.\n'
            '2. Show all products.\n'
            '3. Show purchased products.\n'
            '4. Show receipts.\n'
            '5. Find a customer by id.\n'
            '6. Find a product by id.\n'
            '7. Find a product by name.\n'
            '8. Show a product sales diagram.\n'
            '9. Show a customer purchases diagram.\n'
            '10. Show a product price changes diagram.\n'
            '11. Change a product price.\n'
            '12. Add new customer.\n'
            '13. Add new product.\n'
            '14. Show diagram of number of products a customer purchased.\n'
            '15. Show diagram of a customers purchases price each month.\n'
            '16. Show most purchased product.\n'
            '17. Show top five most purchased products.\n'
            '18. Show diagram of five most purchased products.\n'
            '19. Show diagram of total number of sales of a year.\n'
            '20. Show diagram of total money earned in a year.\n'
            '21. Show three diagrams of five most purchased, total number of sales and '
            'total money earned.\n'
            '0. Exit!'
        )
        try:
            order = int(input('Please enter your order: '))
            match order:
                case 1:
                    shopping_mall.show_customers()
                case 2:
                    shopping_mall.show_products()
                case 3:
                    shopping_mall.show_purchases()
                case 4:
                    shopping_mall.show_receipts()
                case 5:
                    while True:
                        customer_id = int(input('Please enter a customer id: '))
                        user_customer = shopping_mall.find_customer_by_id(customer_id=customer_id)
                        if user_customer:
                            break
                        print('There is no such customer! Please try again.')
                    print(user_customer)
                case 6:
                    while True:
                        product_id = int(input('Please enter a product id: '))
                        user_product = shopping_mall.find_product_by_id(product_id=product_id)
                        if user_product:
                            break
                        print('There is no such product! Please try again.')
                    print(user_product)
                case 7:
                    while True:
                        product_name = input('Please enter a product name: ')
                        user_product = shopping_mall.find_product_by_name(product_name=product_name)
                        if user_product:
                            break
                        print('There is no such product! Please try again.')
                    print(user_product)
                case 8:
                    while True:
                        product_name = input('Please enter a product name: ')
                        user_product = shopping_mall.find_product_by_name(product_name=product_name)
                        if user_product:
                            break
                        print('There is no such product! Please try again.')
                    purchases_each_month = each_month(product=user_product, mall=shopping_mall)
                    create_diagram(
                        y=purchases_each_month,
                        x=list(range(1, len(purchases_each_month)+1)),
                        ylabel='Purchases'
                    )
                    plt.show()
                case 9:
                    while True:
                        customer_id = int(input('Please enter a customer id: '))
                        user_customer = shopping_mall.find_customer_by_id(customer_id=customer_id)
                        if user_customer:
                            break
                        print('There is no such customer! Please try again.')
                    customer_purchese = customer_purchases(
                        customer=user_customer,
                        mall=shopping_mall
                    )
                    create_diagram(
                        y=customer_purchese,
                        x=list(range(1, len(customer_purchese)+1)),
                        ylabel='Customer purcheses'
                    )
                    plt.show()
                case 10:
                    while True:
                        product_name = input('Please enter a product name: ')
                        user_product = shopping_mall.find_product_by_name(product_name=product_name)
                        if user_product:
                            break
                        print('There is no such product added to mall system! Please try again.')
                    price_changes = each_month_price(product=user_product)
                    create_diagram(
                        y=price_changes,
                        x=list(range(1, len(price_changes)+1)),
                        ylabel='Prices'
                    )
                    plt.show()
                case 11:
                    while True:
                        product_name = input('Please enter a product name: ')
                        user_product = shopping_mall.find_product_by_name(product_name=product_name)
                        if user_product:
                            break
                        print('There is no such product added to mall system! Please try again.')
                    price = float(input('Please enter new price for product: '))
                    user_product.change_product_price(
                        new_price=price,
                        date=jdatetime.datetime.now().date()
                    )
                    print('Product price changed successfully')
                    print(user_product)
                case 12:
                    create_customer(mall=shopping_mall)
                    print('New customer added successfully')
                case 13:
                    create_product(mall=shopping_mall)
                    print('New product added successfully')
                case 14:
                    while True:
                        customer_id = int(input('Please enter a customer id: '))
                        user_customer = shopping_mall.find_customer_by_id(customer_id=customer_id)
                        if user_customer:
                            break
                        print('There is no such customer! Please try again.')
                    purchases = shopping_mall.number_of_custmer_product_purchases(user_customer)
                    names = get_product_names(mall=shopping_mall)
                    create_diagram(
                        y=purchases,
                        x=names,
                        ylabel='Number of purchases',
                        xlabel='Products'
                    )
                    plt.show()
                case 15:
                    while True:
                        customer_id = int(input('Please enter a customer id: '))
                        user_customer = shopping_mall.find_customer_by_id(customer_id=customer_id)
                        if user_customer:
                            break
                        print('There is no such customer! Please try again.')
                    spent_money = user_customer.total_money_spent_monthly()
                    create_diagram(
                        y=spent_money,
                        x=list(range(1, len(spent_money)+1)),
                        ylabel='Spent money',
                    )
                    plt.show()
                case 16:
                    most_purchased = shopping_mall.max_purchased(purchases=shopping_mall.purchases)
                    print(most_purchased['Product'])
                    print('Number of purchases', most_purchased['Purchases'])
                case 17:
                    top_five_purchases = shopping_mall.top_five_sales()
                    for purchase in top_five_purchases:
                        print(purchase['Product'])
                        print('Number of purchases', purchase['Purchases'])
                        print('--------------------------------')
                case 18:
                    names, purchases = get_info_of_top_five()

                    create_diagram(
                        y=purchases,
                        x=names,
                        ylabel='Number of purchases',
                        xlabel='Products'
                    )
                    plt.show()
                case 19:
                    monthly_sale = shopping_mall.each_month_purchases()
                    create_diagram(
                        y=monthly_sale,
                        x=list(range(1, len(monthly_sale)+1)),
                        ylabel='Purchases'
                    )
                    plt.show()
                case 20:
                    monthly_earning = shopping_mall.each_month_earnings()
                    create_diagram(
                        y=monthly_earning,
                        x=list(range(1, len(monthly_earning)+1)),
                        ylabel='Purchases'
                    )
                    plt.show()
                case 21:
                    show_three_diagrams()
                case 0:
                    break

        except AttributeError as error:
            print('AttributeError:', error)
            logging.error(error)
        except ValueError as error:
            print('ValueError:', error)
            logging.error(error)
