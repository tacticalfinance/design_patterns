from abc import ABC, abstractmethod


class IOrigianlCar(ABC):
    @property
    @abstractmethod
    def car_color(self) -> str:
        pass

    @car_color.setter
    @abstractmethod
    def car_color(self, car_color: str) -> None:
        pass

    @abstractmethod
    def get_car_color(self) -> str:
        pass

    @abstractmethod
    def set_car_color(self, car_color: str) -> None:
        pass


class OriginalCar(IOrigianlCar):
    def __init__(self, car_color: str) -> None:
        self.__car_color: str = car_color

    @property
    def car_color(self) -> str:
        return self.__car_color

    @car_color.setter
    def car_color(self, car_color: str) -> None:
        self.__car_color = car_color

    def get_car_color(self) -> str:
        return self.__car_color

    def set_car_color(self, car_color: str) -> None:
        self.__car_color = car_color


car = OriginalCar(car_color="yellow")

car.car_color = "white"
car.set_car_color("white")

print(car.car_color)
print(car.get_car_color())
