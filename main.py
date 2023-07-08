import json


class Raf9:

    def __init__(self):
        self.ingredients = ['lemon', 'mint', 'ice', 'soda', 'orange', 'tomat']
        self.get_coctails_from_db()

    # Если какой-то интерфейс реализуется через класс, то класс должен быть колэйбл
    # Нужно дать пользователю управлять кодом. Это делается через какое-нибудь интерактивное меню
    def __call__(self, *args, **kwargs):
        while True:
            self.__help_text()
            command = input('Введите команду:')
            if command == '0':
                print('Всего доброго!')
                break
            elif command == '1':
                current_ings = self.chose_ingredients()
                chose_coctail = self.find_coctail(current_ings)
                if chose_coctail is None:
                    self.save_coctail(current_ings)
                else:
                    print(f'Your choose {chose_coctail} coctail')
            else:
                print('Неправильная команда')

    def __help_text(self):
        print('Доступны команды:')
        print('1 - выбрать ингредиенты')
        print('0 - выход')

    def save_coctail(self, current_ings):
        self.coctails.append({
            "name": "NewCoctail",
            "ingredients": current_ings
        })

        with open('coctails.json', 'w') as json_file:
            json.dump(self.coctails, json_file)

    def get_coctails_from_db(self):
        with open('coctails.json') as json_file:
            self.coctails = json.load(json_file)

    def find_coctail(self, current_ings):
        for c in self.coctails:  # проходим по всем коктейлям
            if c.get('ingredients') == current_ings:
                return c.get('name')
        return None

    def chose_ingredients(self):
        chose_ings = []
        print('Список ингредиентов:')

        i = 0
        for ing in self.ingredients:
            i += 1
            print(f'{i}. {ing}')

        print('0 для выхода')

        while True:
            command = input('Введите команду:')
            if command == '0':
                return chose_ings
            else:
                if command.isdigit():
                    number = int(command)
                    if number > len(self.ingredients):
                        print('Такого ингредиента нет в списке')
                    else:
                        chose_ings.append(self.ingredients[number - 1])
                else:
                    print('Введите номер ингредиента')



if __name__ == '__main__':
    raf9 = Raf9()
    raf9()

    # assert 'mojito' == raf9.find_coctail(['ice', 'soda', 'mint'])
