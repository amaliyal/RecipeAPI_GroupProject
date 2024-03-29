import requests

def search_recipe(ingredient):
    app_id = '' # Enter your own app_id
    app_key = '' # Enter your own app_key
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient:')
    results = search_recipe(ingredient)
    for result in results:
        print('-----------------------------------------------------------------------------------------------------')
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        components = recipe['ingredients']
        for i in components:
            print(i['text'])
        print()
# run()

def file():
    ingredient = input('Enter an ingredient:')
    results = search_recipe(ingredient)
    with open('recipe.txt', 'w+') as recipe_file:
        for result in results:
            recipe_file.write('-------------------------------------------------------------------------------------')
            recipe_file.write('\n')
            recipe = result['recipe']
            recipe_file.write(recipe['label'])
            recipe_file.write('\n')
            recipe_file.write(recipe['url'])
            recipe_file.write('\n')
            components = recipe['ingredients']
            for i in components:
                recipe_file.write(i['text'])
                recipe_file.write('\n')
            recipe_file.write('\n')
    with open('recipe.txt', 'r') as recipe_file:
        recipe = recipe_file.read()
    print(recipe)
# file()

def order_by_main_weight():
    ingredient = input('Enter an ingredient:').lower()
    results = search_recipe(ingredient)
    raw_list = []
    for result in results:
        weight = 0
        recipe = result['recipe']
        # print(recipe['label'])
        # print(recipe['url'])
        components = recipe['ingredients']
        components_list = []
        # print(components)
        for i in components:
            components_list.append(i['text'])
            if i['foodCategory'] is not None:
                if (ingredient in i['food'].lower()) or (ingredient in i['foodCategory'].lower()):
                    weight = weight + i['weight']
            else:
                if ingredient in i['food'].lower():
                    weight = weight + i['weight']
        # print(weight)
        raw_list.append({'label': recipe['label'], 'url': recipe['url'], 'main ingredient weight': weight, 'ingredient': components_list})
    for i in range(0, len(raw_list)):
        for j in range(i + 1, len(raw_list)):
            if raw_list[i]['main ingredient weight'] > raw_list[j]['main ingredient weight']:
                temp = raw_list[i]
                raw_list[i] = raw_list[j]
                raw_list[j] = temp
    for recipe in raw_list:
        print('-------------------------------------------------------------------------------------------------------')
        print(recipe['label'])
        print(ingredient, 'weight (g): ', recipe['main ingredient weight'])
        print(recipe['url'])
        components_list = recipe['ingredient']
        for i in components_list:
            print(i)
        print()
# order_by_main_weight()

def order_by_alphabet_asc():
    ingredient = input('Enter an ingredient:')
    results = search_recipe(ingredient)
    raw_list = []
    for result in results:
        recipe = result['recipe']
        # print(recipe['label'])
        # print(recipe['url'])
        components = recipe['ingredients']
        components_list = []
        # print(components)
        for i in components:
            components_list.append(i['text'])
        raw_list.append({'label': recipe['label'].title(), 'url': recipe['url'], 'ingredient': components_list})
    for i in range(0, len(raw_list)):
        for j in range(i + 1, len(raw_list)):
            if raw_list[i]['label'] > raw_list[j]['label']:
                temp = raw_list[i]
                raw_list[i] = raw_list[j]
                raw_list[j] = temp
    for recipe in raw_list:
        print('-------------------------------------------------------------------------------------------------------')
        print(recipe['label'])
        print(recipe['url'])
        components_list = recipe['ingredient']
        for i in components_list:
            print(i)
        print()
# order_by_alphabet_asc()

def diet_requirement():
    ingredient = input('Enter an ingredient: ')
    no_diets = int(input('How many dietary requirements do you have? '))
    diets_list = []
    for i in range(0, no_diets):
        diet = input('Enter one of your dietary requirements: e.g. low potassium, kidney-friendly, gluten-free, soy-free')
        diets_list.append(diet)
    # print(diets_list)
    results = search_recipe(ingredient)
    components = []
    for result in results:
        recipe = result['recipe']
        count = 0
        for i in recipe['healthLabels']:
            # print(i)
            for diet in diets_list:
                # print(diet)
                if i.lower() == diet.lower():
                    count += 1
                    # print(count)
        if count == no_diets:
            print('---------------------------------------------------------------------------------------------------')
            print(recipe['label'])
            print(recipe['url'])
            print(recipe['healthLabels'])
            components = recipe['ingredients']
            for i in components:
                print(i['text'])
            print()
    if components == []:
        print('There is no recipe that satisfies all the dietary requirements')
# diet_requirement()

def additional_ingredient():
    ingredient = input('Enter an ingredient: ').lower()
    results = search_recipe(ingredient)
    raw_list = []
    ingredient2 = input('Enter another ingredient you would like it contain (try e.g. sugar, water, egg, lemon):').lower()
    for result in results:
        recipe = result['recipe']
        contain2 = False
        # print(recipe['label'])
        # print(recipe['url'])
        components = recipe['ingredients']
        components_list = []
        # print(components)
        for i in components:
            components_list.append(i['text'])
            if i['foodCategory'] is not None:
                if (ingredient2 in i['food'].lower()) or (ingredient2 in i['foodCategory'].lower()):
                    contain2 = True
            else:
                if ingredient2 in i['food'].lower():
                    contain2 = True
        if contain2:
            raw_list.append({'label': recipe['label'], 'url': recipe['url'], 'ingredient': components_list})
    if raw_list == []:
        print(f'There is no recipe for {ingredient} that contains {ingredient2} as well')
    else:
        for recipe in raw_list:
            print('-------------------------------------------------------------------------------------------------------')
            print(recipe['label'])
            print(recipe['url'])
            components_list = recipe['ingredient']
            for i in components_list:
                print(i)
            print()
# additional_ingredient()

def search_nutrition(text):
    app_id = '3b2a209b'
    app_key = '62455cc1a64bc259693673595262004e'
    result = requests.get('https://api.edamam.com/api/nutrition-data?app_id={}&app_key={}&nutrition-type=cooking&ingr={}'.format(app_id, app_key, text))
    data = result.json()
    return data

def cross_analysis():
    ingredient = input('Enter an ingredient: ')
    results = search_recipe(ingredient)
    raw_list = []
    for result in results:
        recipe = result['recipe']
        # print(recipe['label'])
        # print(recipe['url'])
        components = recipe['ingredients']
        components_list = []
        # print(ingredients)
        for i in components:
            components_list.append(i['text'])
        raw_list.append({'label': recipe['label'], 'url': recipe['url'], 'ingredient': components_list})
    for recipe in raw_list:
        print('--------------------------------------------------------------------------------------')
        print(recipe['label'])
        print(recipe['url'])
        components_list = recipe['ingredient']
        total_calories = 0
        for i in components_list:
            # print(search_nutrition(i))
            calories = search_nutrition(i)['calories']
            total_calories += calories
            print(i, '\t', calories, 'calories')
        print()
        print(total_calories, 'calories in total')
# cross_analysis()