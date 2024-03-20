class IngredientsMenu:
    def show_grains(self):
        grains = ["Рис", "Гречка", "Пшено", "Перловка"]
        print("Список круп:")
        for index, grain in enumerate(grains, start=1):
            print(f"{index}. {grain}")

    def show_meat(self):
        meat = ["Говядина", "Свинина", "Курица", "Баранина", "Утка"]
        print("Список мяса:")
        for index, meat_type in enumerate(meat, start=1):
            print(f"{index}. {meat_type}")

    def show_vegetables(self):
        vegetables = ["Помидор", "Огурец", "Морковь", "Болгарский перец", "Лук репчатый", "Картофель", "Баклажан"]
        print("Список овощей:")
        for index, vegetable_type in enumerate(vegetables, start=1):
            print(f"{index}.{vegetable_type}")

    def choose_category_ingredients(self):
        print("Выбери категорию продуктов. Введи ссответствующее число")

    def __str__(self):
        print('Приходи, когда нужен будет совет!')


ingredients_menu = IngredientsMenu()

print("Привет, Сева! Показать список ингридиентов?(напиши 'да/нет')")
wife_answer = input()
while True:
    if wife_answer.lower().startswith("д"):
        print("1. Крупы")
        print("2. Мясо")
        print("3. Овощи")
        print("Выбери категорию для отображения списка. Напиши цифру")
        choose_category_input = int(input())
        if choose_category_input == 1:
            ingredients_menu.show_grains()
            break
        elif choose_category_input == 2:
            ingredients_menu.show_meat()
            break
        elif choose_category_input == 3:
            ingredients_menu.show_vegetables()
            break
    elif wife_answer.lower().startswith("н"):
        ingredients_menu.__str__()
        break
    else:
        print("Не понял твой ответ. Повтори, пожалуйста, 'Да или Нет'")
        wife_answer = input()