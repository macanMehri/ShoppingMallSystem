from customer import Customer
from product import Product
import jdatetime



class ShoppingMall:
    """A class to manage shopping mall"""
    def __init__(self) -> None:
        self.customers = list()
        self.products = list()
        # A list of dictionaries of purchases
        # Every item has a product and number of purchases
        self.purchases = list()


    def show_customers(self) -> None:
        """
        This function print all customers in the shopping mall
        """
        for customer in self.customers:
            print(customer)


    def show_products(self) -> None:
        """
        This function print all products in the shopping mall
        """
        for product in self.products:
            print(product)


    def add_customer(self, customer: Customer):
        """
        Add new customer to the shopping mall list
        """
        self.customers.append(customer)


    def add_product(self, product: Product):
        """
        Add new product to the shopping mall list
        """
        self.products.append(product)
        self.purchases.append(
            {
                'Product': product,
                'Purchases': 0
            }
        )


    def customer_buy_product(self, customer: Customer, product: Product):
        """
        A customer purchases a product
        """
        customer.buy_product(
            product=product,
            date=jdatetime.datetime.now().date()
        )
        self.sell_product(product=product)



    def sell_product(self, product: Product):
        """
        Sell a product
        """
        for purchase in self.purchases:
            if purchase['Product'].product_id == product.product_id:
                purchase['Purchases'] += 1



if __name__ == '__main__':
    mall = ShoppingMall()

    customer1 = Customer(
        first_name='Macan',
        last_name='Mehri',
        birth_year=1380,
        customer_id=1
    )
    customer2 = Customer(
        first_name='Amir',
        last_name='Mehri',
        birth_year=1381,
        customer_id=2
    )
    product1 = Product(
        product_name='Pen',
        product_id=1,
        product_price=35_000
    )
    product2 = Product(
        product_name='Book',
        product_id=2,
        product_price=100_000
    )
    product3 = Product(
        product_name='Table',
        product_id=3,
        product_price=1_000_000
    )


    mall.add_customer(customer=customer1)
    mall.add_customer(customer=customer2)
    mall.add_product(product=product1)
    mall.add_product(product=product2)
    mall.add_product(product=product3)

    mall.customer_buy_product(
        customer=mall.customers[0],
        product=mall.products[0]
    )
    mall.customer_buy_product(
        customer=mall.customers[0],
        product=mall.products[1]
    )
    mall.customer_buy_product(
        customer=mall.customers[0],
        product=mall.products[2]
    )
    mall.customer_buy_product(
        customer=mall.customers[0],
        product=mall.products[2]
    )
    mall.customer_buy_product(
        customer=mall.customers[0],
        product=mall.products[2]
    )
    mall.customer_buy_product(
        customer=mall.customers[0],
        product=mall.products[2]
    )

    for purchase in mall.purchases:
        print(purchase['Product'])
        print(f'Number of purchases: {purchase['Purchases']}')
