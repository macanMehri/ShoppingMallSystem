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
