class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"Vehicle type is '{self.make} {self.model}'")

my_car = Vehicle('Toyota', 'camry')

print(my_car.make)
print(my_car.model)
my_car.moves()

my_car.get_make_model()
print('------------------------------')

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        # self.make = make
        # self.model = model
        super().__init__(make, model) # inherit these params from parent
        self.faa_id = faa_id
    def moves(self):
        #return super().moves() <-- if we want to inherit from parent class
        print('Flies along...')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

class GolfCart(Vehicle):
    pass # <-- inherit everything as-is from parent (vehicle) class


boeing = Airplane('Boeing', 'Max 737', 'N-12345')
airbus = Airplane('AirBus', 'A380', 'A-12345')
tacoma = Truck('Toyota', 'Tacoma')
clubcar = GolfCart('Club Car', 'Onward')

boeing.get_make_model()
boeing.moves()
tacoma.get_make_model()
tacoma.moves()
clubcar.get_make_model()
clubcar.moves()

print('\n---------------\n')

for v in (my_car, boeing, tacoma, clubcar):
    v.get_make_model()
    v.moves()



