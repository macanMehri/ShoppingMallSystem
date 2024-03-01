from CONSTANTS import CURRENT_YEAR
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


    def show_purchases(self) -> None:
        """
        This function print all purchased products in the shopping mall
        """
        for purchase in self.purchases:
            print(f'{purchase['Product']} : {purchase['Purchases']}')


    def add_customer(self, customer: Customer):
        """
        Add new customer to the shopping mall list
        """
        if self.find_customer_by_id(customer.customer_id):
            raise AttributeError('There is a customer with such id!')
        self.customers.append(customer)


    def add_product(self, product: Product):
        """
        Add new product to the shopping mall list
        """
        if self.find_product_by_id(product.product_id):
            raise AttributeError('There is a product with such id!')

        self.products.append(product)
        self.purchases.append(
            {
                'Product': product,
                'Purchases': 0,
                'Date': None
            }
        )


    def find_customer_by_id(self, customer_id: int) -> Customer:
        """
        Find a custumer by customer id
        """
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer


    def find_product_by_id(self, product_id: int) -> Product:
        """
        Find a product by product id
        """
        for product in self.products:
            if product.product_id == product_id:
                return product


    def find_product_by_name(self, product_name: str) -> Product:
        """
        Find a product by its name
        """
        for product in self.products:
            if product.product_name == product_name:
                return product


    def customer_buy_product(self, customer: Customer, product: Product, date: jdatetime.date):
        """
        A customer purchases a product
        """
        customer.buy_product(
            product=product,
            date=date
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
    pass
