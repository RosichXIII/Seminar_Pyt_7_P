# Задание 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
# speed, color, name, is_police (булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        return f'{self.name} повернула {direction}.'

    def show_speed(self):
        return f'Скорость автомобиля {self.name}: {self.speed}.'

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed}.')
        if self.speed > 60:
            return f'Допустимая скорость для городского автомобиля превышена!'
        else:
            return f'Скорость допустима для городского автомобиля.'

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed}.')

    def sport(self):
        if self.is_police:
            return f'Автомобиль {self.name} - спортивный.'
        else:
            return f'Автомобиль {self.name} - полицейский.'

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed}.')
        if self.speed > 40:
            return f'Допустимая скорость для рабочего автомобиля превышена!'
        else:
            return f'Скорость допустима для рабочего автомобиля.'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed}.')

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} - полицейский.'
        else:
            return f'Автомобиль {self.name} - спортивный.'

Audi = TownCar(70, 'Серая', 'Ауди', False)
Mitsubishi = PoliceCar(65, 'Чёрная', 'Митсубиши', True)
Ford = SportCar(90, ':`Красная', 'Форд', False)
Honda = WorkCar(45, 'Зелёная', 'Хонда', True)

Ford.show_speed()
print(Ford.turn('влево'))
Mitsubishi.show_speed()
Mitsubishi.police()