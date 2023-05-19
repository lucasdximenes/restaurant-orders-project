from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    spaghettiDish = Dish("Spaghetti", 10.99)
    assert spaghettiDish.name == "Spaghetti"
    assert spaghettiDish.price == 10.99
    assert spaghettiDish.recipe == {}

    with pytest.raises(TypeError):
        Dish("Burger", "9.99")

    with pytest.raises(ValueError):
        Dish("Salad", -5.0)

    pizzaDish = Dish("Pizza", 15.99)
    assert repr(pizzaDish) == "Dish('Pizza', R$15.99)"

    soup1 = Dish("Soup", 6.99)
    soup2 = Dish("Soup", 6.99)
    salad = Dish("Salad", 8.99)
    assert soup1 == soup2
    assert soup1 != salad
    assert soup2 != salad

    chicken1 = Dish("Chicken", 12.99)
    chicken2 = Dish("Chicken", 12.99)
    assert hash(chicken1) == hash(chicken2)
    assert hash(chicken1) != hash(soup1)

    pasta = Dish("Pasta", 9.99)
    pastaIngredient1 = Ingredient("Tomato")
    pastaIngredient2 = Ingredient("Cheese")
    pasta.add_ingredient_dependency(pastaIngredient1, 2)
    pasta.add_ingredient_dependency(pastaIngredient2, 1)
    assert pasta.recipe == {pastaIngredient1: 2, pastaIngredient2: 1}

    cheeseBreadIngredient1 = Ingredient("ovo")
    cheeseBreadIngredient2 = Ingredient("farinha")
    cheeseBreadIngredient3 = Ingredient("queijo mussarela")
    cheeseBreadDish = Dish("Cheese bread", 7.99)
    cheeseBreadDish.add_ingredient_dependency(cheeseBreadIngredient1, 2)
    cheeseBreadDish.add_ingredient_dependency(cheeseBreadIngredient2, 1)
    cheeseBreadDish.add_ingredient_dependency(cheeseBreadIngredient3, 1)
    expected_restrictions = {
        Restriction.ANIMAL_DERIVED: 'ANIMAL_DERIVED',
        Restriction.LACTOSE: 'LACTOSE',
        Restriction.GLUTEN: 'GLUTEN'
    }
    assert set(
        cheeseBreadDish.get_restrictions()
    ) == set(expected_restrictions)

    ingredient1 = Ingredient("Chicken")
    ingredient2 = Ingredient("Broccoli")
    ingredient3 = Ingredient("Carrots")
    dish = Dish("Stir Fry", 9.99)
    dish.add_ingredient_dependency(ingredient1, 1)
    dish.add_ingredient_dependency(ingredient2, 2)
    dish.add_ingredient_dependency(ingredient3, 1)
    assert dish.get_ingredients() == {ingredient1, ingredient2, ingredient3}
