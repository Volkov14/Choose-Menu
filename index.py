<<<<<<< HEAD
class IngredientsMenu:
    def show_menu(self):
        print("Показать список ингридиентов?(напиши 'да/нет')")
        wife_answer = input()
        while True:
            if wife_answer.lower().startswith("д"):
                print("1. Крупы")
                print("2. Мясо")
                print("3. Овощи")
                print("4. Специи")
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
                elif choose_category_input == 4:
                    ingredients_menu.show_spices()
                    ingredients_menu.get_spices()
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
        for index, meat_type in enumerate(self.meat, start=1):
            print(f"{index}. {meat_type}")

    def show_vegetables(self):
        self.vegetables = vegetables = ["Помидор", "Огурец", "Морковь", "Болгарский перец", "Лук репчатый", "Картофель", "Баклажан"]
        print("Список овощей:")
        for index, vegetable_type in enumerate(vegetables, start=1):
            print(f"{index}.{vegetable_type}")

    def show_spices(self):
        self.spices = spices = ["Прованские травы", "Зира", "Паприка", "Куркума", "Смесь перцев", "Для курицы", "Для мяса"]
        print("Список овощей:")
        for index, spices_type in enumerate(spices, start=1):
            print(f"{index}.{spices_type}")

    def choose_category_ingredients(self):
        print("Выбери категорию продуктов. Введи ссответствующее число")

    def get_vegetables(self):
        self.selected_vegetables = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                vegetable_index = int(user_input) - 1
                if 0 <= vegetable_index <=len(self.vegetables):
                    self.selected_vegetables.append(self.vegetables[vegetable_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список овощей: {self.selected_vegetables}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбрать другие ингредиенты?")
            answer = input().lower()
            if answer.startswith("д"):
                self.show_menu()
            else:
                print("Завершить выбор продуктов?")
                answer = input().lower()
                if answer.startswith("д"):
                    print("Твой набор продуктов:")
                    ingredients_menu.show_selected_ingredients()

    def get_meat(self):
        self.selected_meat = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                meat_index = int(user_input) - 1
                if 0 <= meat_index <=len(self.meat):
                    self.selected_meat.append(self.meat[meat_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список мяса: {self.selected_meat}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбрать другие ингредиенты?")
            answer = input().lower()
            if answer.startswith("д"):
                self.show_menu()
            else:
                print("Твой набор продуктов:")
                ingredients_menu.show_selected_ingredients()

    def get_grains(self):
        self.selected_grains = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                grains_index = int(user_input) - 1
                if 0 <= grains_index <=len(self.grains):
                    self.selected_grains.append(self.grains[grains_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список круп: {self.selected_grains}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбрать другие ингредиенты?")
            answer = input().lower()
            if answer.startswith("д"):
                self.show_menu()
            else:
                print("Твой набор продуктов:")
                ingredients_menu.show_selected_ingredients()


    def get_spices(self):
        self.selected_spices = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                spices_index = int(user_input) - 1
                if 0 <= spices_index <=len(self.spices):
                    self.selected_spices.append(self.spices[spices_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список круп: {self.selected_spices}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбрать другие ингредиенты?")
            answer = input().lower()
            if answer.startswith("д"):
                self.show_menu()
            else:
                print("Твой набор продуктов:")
                ingredients_menu.show_selected_ingredients()

    def show_selected_ingredients(self):
        self.summury_ingredietns = []
        if hasattr(self, 'selected_meat'):
            for i in self.selected_meat:
                self.summury_ingredietns.append(i)
            print("Мясо:", self.selected_meat)
        if hasattr(self, 'selected_vegetables'):
            for i in self.selected_vegetables:
                self.summury_ingredietns.append(i)
            print("Овощи:", self.selected_vegetables)
        if hasattr(self, 'selected_grains'):
            for i in self.selected_grains:
                self.summury_ingredietns.append(i)
            print("Крупы:", self.selected_grains)
        if hasattr(self, 'selected_spices'):
            for i in self.selected_spices:
                self.summury_ingredietns.append(i)
            print("Специи:", self.selected_spices)


    def __str__(self):
        print('Приходи, когда нужен будет совет!')

    def __str__(self):
        print("")



ingredients_menu = IngredientsMenu()
ingredients_menu.show_menu()
=======
class IngredientsMenu:
    def show_menu(self):
        print("Показать список ингридиентов?(напиши 'да/нет')")
        wife_answer = input()
        while True:
            if wife_answer.lower().startswith("д"):
                print("1. Крупы")
                print("2. Мясо")
                print("3. Овощи")
                print("4. Специи")
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
                elif choose_category_input == 4:
                    ingredients_menu.show_spices()
                    ingredients_menu.get_spices()
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
        for index, meat_type in enumerate(self.meat, start=1):
            print(f"{index}. {meat_type}")

    def show_vegetables(self):
        self.vegetables = vegetables = ["Помидор", "Огурец", "Морковь", "Болгарский перец", "Лук репчатый", "Картофель", "Баклажан"]
        print("Список овощей:")
        for index, vegetable_type in enumerate(vegetables, start=1):
            print(f"{index}.{vegetable_type}")

    def show_spices(self):
        self.spices = spices = ["Прованские травы", "Зира", "Паприка", "Куркума", "Смесь перцев", "Для курицы", "Для мяса"]
        print("Список овощей:")
        for index, spices_type in enumerate(spices, start=1):
            print(f"{index}.{spices_type}")

    def choose_category_ingredients(self):
        print("Выбери категорию продуктов. Введи ссответствующее число")

    def get_vegetables(self):
        self.selected_vegetables = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                vegetable_index = int(user_input) - 1
                if 0 <= vegetable_index <=len(self.vegetables):
                    self.selected_vegetables.append(self.vegetables[vegetable_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список овощей: {self.selected_vegetables}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбрать другие ингредиенты?")
            answer = input().lower()
            if answer.startswith("д"):
                self.show_menu()
            else:
                print("Завершить выбор продуктов?")
                answer = input().lower()
                if answer.startswith("д"):
                    print("Твой набор продуктов:")
                    ingredients_menu.show_selected_ingredients()

    def get_meat(self):
        self.selected_meat = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                meat_index = int(user_input) - 1
                if 0 <= meat_index <=len(self.meat):
                    self.selected_meat.append(self.meat[meat_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список мяса: {self.selected_meat}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбрать другие ингредиенты?")
            answer = input().lower()
            if answer.startswith("д"):
                self.show_menu()
            else:
                print("Твой набор продуктов:")
                ingredients_menu.show_selected_ingredients()

    def get_grains(self):
        self.selected_grains = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                grains_index = int(user_input) - 1
                if 0 <= grains_index <=len(self.grains):
                    self.selected_grains.append(self.grains[grains_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список круп: {self.selected_grains}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбрать другие ингредиенты?")
            answer = input().lower()
            if answer.startswith("д"):
                self.show_menu()
            else:
                print("Твой набор продуктов:")
                ingredients_menu.show_selected_ingredients()


    def get_spices(self):
        self.selected_spices = []
        print("Введите номер продукта, который необходимо использовать. Для завершения выбора нажми enter")
        while True:
            user_input = input()
            if user_input == "":
                break
            try:
                spices_index = int(user_input) - 1
                if 0 <= spices_index <=len(self.spices):
                    self.selected_spices.append(self.spices[spices_index])
                else:
                    print("Выбери продукт из списка")
            except ValueError:
                print("Выбери продукт из списка, введи число")
        print(f"твой список круп: {self.selected_spices}.Всё верно?")
        answer = input().lower()
        if answer.startswith("д"):
            print("Выбрать другие ингредиенты?")
            answer = input().lower()
            if answer.startswith("д"):
                self.show_menu()
            else:
                print("Твой набор продуктов:")
                ingredients_menu.show_selected_ingredients()

    def show_selected_ingredients(self):
        self.summury_ingredietns = []
        if hasattr(self, 'selected_meat'):
            for i in self.selected_meat:
                self.summury_ingredietns.append(i)
            print("Мясо:", self.selected_meat)
        if hasattr(self, 'selected_vegetables'):
            print("Овощи:", self.selected_vegetables)
        if hasattr(self, 'selected_grains'):
            print("Крупы:", self.selected_grains)
        if hasattr(self, 'selected_spices'):
            print("Специи:", self.selected_spices)


    def __str__(self):
        print('Приходи, когда нужен будет совет!')

    def __str__(self):
        print("")



ingredients_menu = IngredientsMenu()
ingredients_menu.show_menu()
>>>>>>> origin/main
