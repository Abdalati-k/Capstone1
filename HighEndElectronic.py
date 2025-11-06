from Item import Item
class HighEndElectronic(Item):
    def __init__(self, item_id: int, name: str, price: float, quantity: int, warranty_period: int):
        super().__init__(item_id, name, price, quantity)

        self.warranty_period = warranty_period

    def __str__(self) -> str:
        # Get the base string from the parent class and add the new info
        return super().__str__() + f", Warranty: {self.warranty_period} months"