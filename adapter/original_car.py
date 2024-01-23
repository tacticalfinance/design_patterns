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


class OriginalCar(IOrigianlCar):
    def __init__(self, car_color: str) -> None:
        self.__car_color: str = car_color

    @property
    def car_color(self) -> str:
        return self.__car_color

    @car_color.setter
    def car_color(self, car_color: str) -> None:
        self.__car_color = car_color


if __name__ == "__main__":
    car = OriginalCar(car_color="yellow")
    car.car_color = "white"
    print(car.car_color)
