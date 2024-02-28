from CONSTANTS import CURRENT_YEAR
import jdatetime



class Customer:
    """A customer object"""
    def __init__(
            self, first_name: str,
            last_name: str,
            birth_year: int,
            customer_id: int
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.customer_id = customer_id
        # A list of dictionaries that contains product id and purchased time
        self.bought_products = list()


    def __str__(self) -> str:
        """Override string method"""
        message = (
            f'Name: {self.full_name}\nBirthday: {self.birth_year}\n'
            f'ID: {self.customer_id}'
        )
        return message


    def show_purchased_list(self) -> None:
        """
        Showing products list that customer has purchased
        """
        for product in self.bought_products:
            print(f'{product['Product']} : {str(product['Date'])}')

    @property
    def full_name(self) -> str:
        """
        Concatinate first name and last name to create full name
        """
        return f'{self.first_name} {self.last_name}'


    @property
    def age(self) -> int:
        """
        Calculate customers age
        """
        return CURRENT_YEAR - self.birth_year


    def buy_product(self, product_name: str, date: jdatetime.date):
        """
        Customer buys a product
        Includes id of product and time that customer bought product
        """
        self.bought_products.append(
            {
                'Product': product_name,
                'Date': date
            }
        )


    @property
    def number_of_products(self) -> int:
        """
        Calculates number of products that customer has bought
        """
        return len(self.bought_products)


    def purchase_each_month(self) -> list:
        """
        Calculates number of purchases for each month in a year
        """



    def purchase_in_time(self, start: jdatetime.date, stop: jdatetime.date) -> int:
        """
        Calculate number of purchases between start date and stop date
        """
        count = 0
        for purchase in self.bought_products:
            if start.year < purchase['Date'].year < stop.year:
                count += 1
            elif start.year == purchase['Date'].year:
                if start.month < purchase['Date'].month:
                    count += 1
                elif start.month == purchase['Date'].month:
                    if start.day < purchase['Date'].day:
                        count += 1
            elif stop.year == purchase['Date'].year:
                if start.month > purchase['Date'].month:
                    count += 1
                elif start.month == purchase['Date'].month:
                    if start.day > purchase['Date'].day:
                        count += 1

        return count


if __name__ == '__main__':

    c1 = Customer(
        first_name='Macan',
        last_name='Mehri',
        birth_year=1380,
        customer_id=1
    )

    c1.buy_product(
        product_name='Pen',
        date=jdatetime.datetime.now().date()
    )

    c1.buy_product(
        product_name='Book',
        date=jdatetime.date(day=22, month=11, year=1400)
    )

    c1.show_purchased_list()
