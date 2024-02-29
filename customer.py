from CONSTANTS import CURRENT_YEAR
import jdatetime
from product import Product



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
            f'Age: {self.age}\nID: {self.customer_id}'
        )
        return message


    def show_purchased_list(self) -> None:
        """
        Showing products list that customer has purchased
        """
        print(f'Customer :\n{self}\nbought these:')
        for product in self.bought_products:
            print(f'{product['Product']}\nPurchased date: {str(product['Date'])}')

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


    def buy_product(self, product: Product, date: jdatetime.date):
        """
        Customer buys a product
        Includes id of product and time that customer bought product
        """
        self.bought_products.append(
            {
                'Product': product,
                'Date': date
            }
        )


    @property
    def number_of_products(self) -> int:
        """
        Calculates number of products that customer has bought
        """
        return len(self.bought_products)


    def purchase_each_month_of_year(self, product: str):
        """
        Calculates number of purchases for each month in a year
        """
        number_each_month = list()

        for i in range(12):
            if i == 11:
                start_month = 12
                stop_month = 1
                year = CURRENT_YEAR
            else:
                year = CURRENT_YEAR - 1
                start_month = i + 1
                stop_month = i + 2

            start = jdatetime.date(
                year=year,
                month=start_month,
                day=1
            )
            stop = jdatetime.date(
                year=year,
                month=stop_month,
                day=1
            )

            number_each_month.append(
                self.purchase_in_time(
                    start=start,
                    stop=stop,
                    product=product
                )
            )

        return number_each_month


    def find_product_in_purchased(self, product: str) -> list:
        """
        find all items of the product in bought list
        """
        result = list()

        for purchased in self.bought_products:
            if purchased['Product'].product_name == product:
                result.append(purchased)

        return result




    def purchase_in_time(
        self,
        start: jdatetime.date,
        stop: jdatetime.date,
        product: Product
    ) -> int:
        """
        Calculate number of purchases between start date and stop date
        """
        count = 0
        product_purchased = self.find_product_in_purchased(product=product)

        for purchase in product_purchased:
            if start.year < purchase['Date'].year < stop.year:
                count += 1
            elif start.year == purchase['Date'].year:
                if start.month < purchase['Date'].month < stop.month:
                    count += 1
                elif start.month == purchase['Date'].month:
                    if start.day <= purchase['Date'].day:
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
        product=Product('Book', 1, 25000),
        date=jdatetime.datetime.now().date()
    )

    c1.buy_product(
        product=Product('Book', 1, 98000),
        date=jdatetime.date(day=22, month=11, year=1401)
    )
    c1.buy_product(
        product=Product('Book', 1, 98000),
        date=jdatetime.date(day=22, month=12, year=1401)
    )
    c1.buy_product(
        product=Product('Book', 1, 98000),
        date=jdatetime.date(day=25, month=1, year=1401)
    )
    c1.buy_product(
        product=Product('Book', 1, 98000),
        date=jdatetime.date(day=5, month=3, year=1401)
    )
    c1.buy_product(
        product=Product('Book', 1, 98000),
        date=jdatetime.date(day=1, month=10, year=1401)
    )

    result = c1.purchase_each_month_of_year(product=Product('Book', 1, 98000))
    print(result)
