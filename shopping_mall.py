from customer import Customer
from product import Product
import jdatetime
from CONSTANTS import CURRENT_YEAR



class ShoppingMall:
    """A class to manage shopping mall"""
    def __init__(self) -> None:
        self.customers = list()
        self.products = list()
        # A list of dictionaries of purchases
        # Every item has a product and number of purchases
        self.purchases = list()
        # A list of dictionaries
        # Receipt of each purchase
        self.receipts = list()


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
        This function prints all purchased products in the shopping mall
        """
        for purchase in self.purchases:
            print(f'{purchase['Product']}\nNumber of sales: {purchase['Purchases']}')


    def show_receipts(self) -> None:
        """
        This function prints all receipts
        """
        for receipt in self.receipts:
            print(f'Customer:\n{receipt['Customer']}')
            print(f'Product:\n{receipt['Product']}')
            print(f'Purchased date:\n{str(receipt['Date'])}')
            print('----------------------------------')


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
                'Purchases': 0
            }
        )


    def number_of_custmer_product_purchases(self, customer: Customer) -> list:
        """Returns a list of numbers that shows you number of purchases of each product"""
        result = list()
        for product in self.products:
            count = customer.number_of_product_purchases(product=product)
            result.append(count)

        return result


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

        self.receipts.append(
            {
                'Customer': customer,
                'Product': product,
                'Date': date
            }
        )


    def top_five_sales(self) -> list:
        """Returns top five sales list of products"""
        temp = self.purchases
        top_five = list()
        for i in range(5):
            maximum = self.max_purchased(purchases=temp)
            top_five.append(maximum)
            temp.remove(maximum)

        return top_five



    def max_purchased(self, purchases: list) -> dict:
        """Returns a dictionary with must purchased"""
        temp = {
                'Product': None,
                'Purchases': 0
        }
        for purchase in purchases:
            if purchase['Purchases'] > temp['Purchases']:
                temp = purchase

        return temp


    def sell_product(self, product: Product):
        """
        Sell a product
        """
        for purchase in self.purchases:
            if purchase['Product'].product_id == product.product_id:
                purchase['Purchases'] += 1


    def each_month_purchases(self) -> list:
        """Returns a list of numbers for sales of each month of year"""
        result = list()
        for month in range(12):
            purchases = self.purchases_in_a_month(month=month+1)
            result.append(purchases)

        return result



    def purchases_in_a_month(self, month: int) -> int:
        """Returns number of sales of a month"""
        total_purchase = 0
        for receipt in self.receipts:
            if receipt['Date'].month == month and receipt['Date'].year == CURRENT_YEAR:
                total_purchase += 1

        return total_purchase



    def earning_in_a_month(self, month: int) -> int:
        """Returns total earnings of a month"""
        total_erning = 0
        for receipt in self.receipts:
            if receipt['Date'].month == month and receipt['Date'].year == CURRENT_YEAR:
                total_erning += receipt['Product'].product_price

        return total_erning


    def each_month_earnings(self) -> list:
        """Returns a list of total earnings of a month in last year"""
        result = list()
        for month in range(12):
            earnings = self.earning_in_a_month(month=month+1)
            result.append(earnings)

        return result


if __name__ == '__main__':
    pass
