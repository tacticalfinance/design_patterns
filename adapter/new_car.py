from abc import ABC, abstractmethod
from original_car import IOrigianlCar, OriginalCar


class INewCar(ABC):
    @property
    @abstractmethod
    def color(self) -> str:
        pass

    @color.setter
    @abstractmethod
    def color(self, car_color: str) -> None:
        pass


class NewCarAdapter(INewCar):
    def __init__(self, adaptee: IOrigianlCar) -> None:
        self.__adaptee__: IOrigianlCar = adaptee

    @property
    def color(self) -> str:
        return self.__adaptee__.car_color

    @color.setter
    def color(self, car_color: str) -> None:
        self.__adaptee__.car_color = car_color


if __name__ == "__main__":
    car = OriginalCar(car_color="yellow")
    adapter: INewCar = NewCarAdapter(car)
    adapter.color = "white"
    print(adapter.color)
