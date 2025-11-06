from Item import Item


class BrandedClothing(Item):
    def __init__(self, item_id: int, name: str, price: float, quantity: int, size: str, color: str):
        super().__init__(item_id, name, price, quantity)
        self.size = size
        self.color = color

    def __str__(self) -> str:
        return super().__str__() + f", Size: {self.size}, Color: {self.color}"