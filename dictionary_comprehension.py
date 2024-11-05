recipes = {
    'omelette': 10,
    'lasagna': 60,
    'risotto': 30,
    'frittata': 15
    }

quick_recipes = {
    recipe: time for recipe, time in recipes.items() if time < 20
    }

print(quick_recipes)