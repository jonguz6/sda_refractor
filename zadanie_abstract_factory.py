class Sedan:
    def who_am_i(self):
        pass


class Kombi:
    def who_am_i(self):
        pass


class Coupe:
    def who_am_i(self):
        pass


class LHDSedan(Sedan):
    def who_am_i(self):
        return "Left Hand Drive Sedan"


class RHDSedan(Sedan):
    def who_am_i(self):
        return "Right Hand Drive Sedan"


class LHDKombi(Kombi):
    def who_am_i(self):
        return "Left Hand Drive Kombi"


class RHDKombi(Kombi):
    def who_am_i(self):
        return "Right Hand Drive Kombi"


class LHDCoupe(Coupe):
    def who_am_i(self):
        return "Left Hand Drive Coupe"


class RHDCoupe(Coupe):
    def who_am_i(self):
        return "Right Hand Drive Coupe"


class CarFactory:
    def create_sedan(self):
        pass

    def create_kombi(self):
        pass

    def create_coupe(self):
        pass


class LHDCarFactory(CarFactory):
    def create_sedan(self):
        return LHDSedan()

    def create_kombi(self):
        return LHDKombi()

    def create_coupe(self):
        return LHDCoupe()


class RHDCarFactory(CarFactory):
    def create_sedan(self):
        return RHDSedan()

    def create_coupe(self):
        return RHDCoupe()

    def create_kombi(self):
        return RHDKombi()


if __name__ == "__main__":
    car_factory = LHDCarFactory()
    #    car_factory = RHDCarFactory()

    sedan = car_factory.create_sedan()
    print(sedan.who_am_i())

    station_wagon = car_factory.create_kombi()
    print(station_wagon.who_am_i())

    coupe = car_factory.create_coupe()
    print(coupe.who_am_i())