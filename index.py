class IngredientsMenu:
    def show_menu(self):
        print("Показать список ингридиентов?(напиши 'да/нет')")
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
                    ingredients_menu.get_grains()
                    break
                elif choose_category_input == 2:
                    ingredients_menu.show_meat()
                    ingredients_menu.get_meat()
                    break
                elif choose_category_input == 3:
                    ingredients_menu.show_vegetables()
                    ingredients_menu.get_vegetables()
                    break
            elif wife_answer.lower().startswith("н"):
                ingredients_menu.__str__()
                break
            else:
                print("Не понял твой ответ. Повтори, пожалуйста, 'Да или Нет'")
                wife_answer = input()
    def show_grains(self):
        self.grains = ["Рис", "Гречка", "Пшено", "Перловка"]
        print("Список круп:")
        for index, grain in enumerate(self.grains, start=1):
            print(f"{index}. {grain}")

    def show_meat(self):
        self.meat = ["Говядина", "Свинина", "Курица", "Баранина", "Утка"]
        print("Список мяса:")
        for index, meat_type in enumerate(meat, start=1):
            print(f"{index}. {meat_type}")

    def show_vegetables(self):
        self.vegetables = vegetables = ["Помидор", "Огурец", "Морковь", "Болгарский перец", "Лук репчатый", "Картофель", "Баклажан"]
        print("Список овощей:")
        for index, vegetable_type in enumerate(vegetables, start=1):
            print(f"{index}.{vegetable_type}")

    def choose_category_ingredients(self):
        print("Выбери категорию продуктов. Введи ссответствующее число")

    def get_vegetables(self):
        selected_vegetables = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                vegetable_index = int(user_input) - 1
                if 0 <= vegetable_index <=len(self.vegetables):
                    selected_vegetables.append(self.vegetables[vegetable_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список овощей: {selected_vegetables}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбери другие ингредиенты")
            ingredients_menu.show_menu()

    def get_meat(self):
        selected_meat = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                meat_index = int(user_input) - 1
                if 0 <= meat_index <=len(self.meat):
                    selected_meat.append(self.meat[meat_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список мяса: {selected_meat}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбери другие ингредиенты")
            ingredients_menu.show_menu()

    def get_grains(self):
        selected_grains = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                grains_index = int(user_input) - 1
                if 0 <= grains_index <=len(self.grains):
                    selected_grains.append(self.grains[grains_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список круп: {selected_grains}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбери другие ингредиенты")
            ingredients_menu.show_menu()

    def __str__(self):
        print('Приходи, когда нужен будет совет!')



ingredients_menu = IngredientsMenu()
ingredients_menu.show_menu()
