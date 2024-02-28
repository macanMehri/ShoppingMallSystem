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

    def __str__(self) -> str:
        """Override string method"""
        return f'ID: {self.product_id}\nName: {self.product_name}\nPrice: {self.product_price}'


if __name__ == '__main__':
    product1 = Product(
        product_name='Pen',
        product_id=1,
        product_price=25000
    )
    print(product1)
