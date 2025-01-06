class Car :
    def __init__(self, brand : str , wheels : int)->None:
        self.brand = brand
        self.wheels = wheels

    def turn_on (self)-> None :
        print(f'Turning On {self.brand}')
    def turn_off(self)->None:
        print(f'Turning OFF {self.brand} ')

    def drive (self , klm:float)->None :
        print(f'Driving : {self.brand} for {klm} Km')


def main() ->None :

    bmw : Car = Car('BMW',4)
    bmw.turn_on()
    bmw.turn_off()
    bmw.drive(10)

if __name__ == '__main__':
    main()