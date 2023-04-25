import requests

def search_recipes(ingredient, meal, cuisine):
    app_id = ''
    app_key = ''
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}&mealType={meal}&cuisineType={cuisine}'
    result = requests.get(url)
    data = result.json()
    return data['hits']

meal_types = {
    'b': 'Breakfast',
    'l': 'Lunch',
    'd': 'Dinner',
    's': 'Snack'
}

cuisine_types = {
    'a': 'American',
    's': 'Asian',
    'b': 'British',
    'c': 'Chinese',
    'f': 'French',
    'i': 'Italian',
    'j': 'Japanese'
}

def get_user_input(input_type, options):
    input_msg = f"Enter the {input_type} you want: "
    options_str = "\n".join([f"({key}) {value}" for key, value in options.items()])
    options_msg = f"Choose one of the following {input_type}s:\n{options_str}\nYour choice: "
    user_input = input(input_msg).lower()
    while user_input not in options:
        user_input = input(options_msg).lower()
    return options[user_input]

def run():
    meal = get_user_input("meal", meal_types)
    cuisine = get_user_input("cuisine", cuisine_types)
    ingredient = input("Enter an ingredient: ")
    while not ingredient:
        ingredient = input("Please enter an ingredient: ")
    results = search_recipes(ingredient, meal.lower(), cuisine.lower())
    print(f"Here are some {cuisine} {meal} recipes that include {ingredient}:")
    print("-" * 80)
    with open("recipes.txt", "w") as recipe_file:
        for result in results:
            recipe = result['recipe']
            lines = [
                f"Title: {recipe['label']}",
                f"Cuisine Type: {recipe['cuisineType']}",
                f"Meal Type: {recipe['mealType']}",
                f"Calories: {int(recipe['calories'])} kcal",
                f"Link: {recipe['url']}",
                "Ingredients: " + ", ".join(recipe['ingredientLines']),
                "-" * 80 + "\n"
            ]
            print("\n".join(lines))
            recipe_file.write("\n".join(lines))

run()
