""" Урок 4, завдання 5
Створіть програму спортивного комплексу, у якій передбачене меню: 1 - перелік видів спорту, 2 -
команда тренерів, 3 - розклад тренувань, 4 - вартість тренування. Дані зберігати у словниках. Також
передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню. Якщо
ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику
виключень.
"""


class TrainerNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f'TrainerNotFoundError: {self.message}'


class SportComplex:
    def __init__(self):
        self.sport_types = {1: 'Football', 2: 'Basketball', 3: 'Volleyball'}
        self.trainers = {1: 'Ivan', 2: 'Petro', 3: 'Vasyl', 4: 'Oleh'}
        self.schedule = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                         7: 'Sunday'}
        self.price = {1: '1h = 100', 2: '2h = 200', 3: '3h = 300'}

    def search_trainer(self, trainer_name):
        try:
            if trainer_name in self.trainers.values():
                print(f'Trainer {trainer_name} is found')
            else:
                raise TrainerNotFoundError(f'Trainer {trainer_name} is not found')
        except TrainerNotFoundError as e:
            print(e)


sport_complex = SportComplex()
sport_complex.search_trainer('Ivan')
sport_complex.search_trainer('Oleg')
sport_complex.search_trainer('Oleh')
