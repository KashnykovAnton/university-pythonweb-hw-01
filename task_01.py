from abc import ABC, abstractmethod
from logger_config import logger


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec: str):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f"{self.make} {self.model} ({self.region_spec} Spec): Двигун запущено"
        )


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f"{self.make} {self.model} ({self.region_spec} Spec): Мотор заведено"
        )


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

us_vehicle1 = us_factory.create_car("Ford", "Mustang")
us_vehicle1.start_engine()
us_vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_vehicle2.start_engine()

eu_vehicle1 = eu_factory.create_car("Fiat", "Grande Panda")
eu_vehicle1.start_engine()
eu_vehicle2 = eu_factory.create_motorcycle("BMW", "R1250")
eu_vehicle2.start_engine()
