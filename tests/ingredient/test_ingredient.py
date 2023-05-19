from src.models.ingredient import Ingredient, restriction_map  # noqa: F401, E261, E501
import pytest


@pytest.fixture
def ingredient():
    return Ingredient("bacon")


baconIngredient = Ingredient("bacon")
cheeseIngredient = Ingredient("cheese")

# Req 1


def test_ingredient(ingredient):
    assert ingredient.name == "bacon"
    assert ingredient == baconIngredient
    assert ingredient != cheeseIngredient
    assert hash(ingredient) == hash(baconIngredient)
    baconRestrictions = restriction_map().get("bacon", set())
    assert ingredient.restrictions == baconRestrictions
