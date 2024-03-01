import jdatetime
from CONSTANTS import CURRENT_YEAR


class Product:
    """A product object"""
    def __init__(self,
            product_name: str,
            product_id: int,
            product_price: float
    ) -> None:
        self.product_name = product_name
        self.product_id = product_id
        self.product_price = product_price
        # A list of dictionaries with price changes and datetime of change
        self.product_price_changes = list()
        self.product_price_changes.append(
            {
                'Price': self.product_price,
                'Date': jdatetime.date(year=CURRENT_YEAR, month=1, day=1)
            }
        )

    def __str__(self) -> str:
        """Override string method"""
        return f'ID: {self.product_id}\nName: {self.product_name}\nPrice: {self.product_price}'


    def change_product_price(self, new_price: float, date: jdatetime.date):
        """Change a product price"""
        self.product_price = new_price
        self.product_price_changes.append(
            {
                'Price': new_price,
                'Date': date

            }
        )



    def price_in_month(self, month: int) -> float:
        """
        This function get a month number and return the price of produt
        in the month
        """
        for price in self.product_price_changes:
            if price['Date'].month == month and price['Date'].year == CURRENT_YEAR:
                return price['Price']

        return self.price_in_month(month=month-1)


    def price_changes_in_year(self) -> list:
        """
        return a list of float numbers for changes of price each month of last year
        """
        prices = list()
        for month in range(12):
            prices.append(self.price_in_month(month=month+1))

        return prices



if __name__ == '__main__':
    product1 = Product(
        product_name='Pen',
        product_id=1,
        product_price=25000
    )
    print(product1)

    product1.change_product_price(35000, jdatetime.date(
        year=1402,
        month=11,
        day=25
    ))
    product1.change_product_price(50000, jdatetime.date(
        year=1402,
        month=8,
        day=25
    ))


    print(product1.price_changes_in_year())
    print(product1)
