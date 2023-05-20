from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv

# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = []
        self._load_dishes()

    def _load_dishes(self):
        with open(self.source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not self._get_dish(row["dish"]):
                    self.dishes.append(Dish(row["dish"], float(row["price"])))
                dish = self._get_dish(row["dish"])
                dish.add_ingredient_dependency(
                    Ingredient(row["ingredient"]),
                    int(row["recipe_amount"])
                )

    def _get_dish(self, name: str) -> Dish:
        for dish in self.dishes:
            if dish.name == name:
                return dish
        return None

    def get_all_dishes(self) -> list:
        return self.dishes

    def get_dishes_without_restrictions(self, restriction) -> list:
        return [
            dish
            for dish in self.dishes
            if restriction not in dish.get_restrictions()
        ]
