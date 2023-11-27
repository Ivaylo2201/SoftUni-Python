from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import session_decorator
from models import Recipe, Chef

DATABASE_URL = 'postgresql+psycopg2://postgres:5432@127.0.0.1/postgres'
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str) -> None:
    session.add(
        Recipe(
            name=name,
            ingredients=ingredients,
            instructions=instructions
        )
    )


@session_decorator(session)
def update_recipe_by_name(name: str, new_name: str, new_ingredients: str, new_instructions: str) -> None:
    recipe_to_update = session.query(Recipe).filter_by(name=name).first()  # Select

    recipe_to_update.name = new_name  #
    recipe_to_update.ingredients = new_ingredients  # Update
    recipe_to_update.instructions = new_instructions  #

    records_changed: int = (  # Bulk update (Updates all records caught by the filter with the new values)
        session.query(Recipe)  # Returns the amount of changed records
        .filter_by(name=name)
        .update(
            {
                Recipe.name: new_name,
                Recipe.ingredients: new_ingredients,
                Recipe.instructions: new_instructions
            }
        )
    )

@session_decorator(session)
def delete_recipe_by_name(name: str):
    records_changes: int = (  # Bulk delete (Deletes all records caught by the filter)
        session.query(Recipe)
        .filter_by(name=name)
        .delete()
    )

@session_decorator(session)
def get_recipes_by_ingredient(ingredient_name: str) -> list:
    recipes_with_ingredient = (
        session.query(Recipe)
        .filter(Recipe.ingredients.ilike(f'%{ingredient_name}%'))
        .all()
    )

    # filter() -> Low level SQL
    # filter_by() -> High level SQL

    return recipes_with_ingredient

@session_decorator(session)
def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str):
    first_recipe = (
        session.query(Recipe)
        .filter_by(name=first_recipe_name)
        .first()
        # .with_for_update()   Locks the object (can't be updated)
        # .one()   An error is raised if the query returned more than 1 object
    )

    second_recipe = (
        session.query(Recipe)
        .filter_by(name=second_recipe_name)
        .first()
    )

    first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients

@session_decorator(session)
def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str) -> str:
    recipe = (
        session.query(Recipe)
        .filter_by(name=recipe_name)
        .first()
    )

    if recipe and recipe.chef:
        return f'Recipe: {recipe_name} already has a related chef'

    chef = (
        session.query(Chef)
        .filter_by(name=chef_name)
        .first()
    )

    recipe.chef = chef
    return f'Related recipe {recipe_name} with chef {chef_name}'

@session_decorator(session)
def get_recipes_with_chef() -> str:
    recipes_with_chef = (
        # SELECT recipe.name, chef.name AS chef FROM recipes
        session.query(Recipe.name, Chef.name.label('chef'))
        .join(Chef, Recipe.Chef)  # Matches the recipe Chef with the Chef
        .all()
    )

    return '\n'.join(
        [f'Recipe: {recipe_name} made by {chef_name}'
         for recipe_name, chef_name in recipes_with_chef]
    )
