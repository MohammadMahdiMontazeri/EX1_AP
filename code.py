from abc import ABC, abstractmethod
import time


class Transport(ABC): #Abstraction

    def __init__(self):
        self.fuel = 'Petrol, diesel and gas'
        self.price_of_ticket = 'It depends on the type of vehicle'
        self.vehicleـage = 'It can be old or new'
        self.accessibility = 'It depends on the amenities of the area'
        self.material = 'Iron, aluminum, plastic and...'
 
    @abstractmethod
    def color(self):
        pass
        
    @abstractmethod
    def change_color(self):
        pass

    def specify_the_fuel(self,specified_fuel:str):
        self.fuel = specified_fuel
        
    def specify_the_material(self,specified_material:str):
        self.material = specified_material
        
    def specify_the_price_of_ticket(self,specified_price_of_ticket:int):
        self.price_of_ticket = specified_price_of_ticket       
        


class Marine(Transport):
    '''
    Weight is based on tons.
    '''
    
    def __init__(self,color:str,weight:float,num_of_passenger:int,maxspeed:float):
        super().__init__()
        self.__color = color #Encapsulation
        self.weight = f'{round(num_of_passenger*0.1 + weight,2)} ton(s)'
        self.num_of_passenger = num_of_passenger
        self._maxspeed = maxspeed #Encapsulation
        self.place = 'Sea'
    
    def color(self):
        return self.__color
        
    def change_color(self,new_color):
        self.__color = new_color
        print('The color changed...')

    def start(self):
        return 'Start'
    
    @abstractmethod
    def type_of_ship(self):
        pass

class Recreational(Marine):
    # Class attributes:
        
    num_of_crew = 250
    num_of_engine = 8
    power_of_engine = '110k Hp'
    
    def type_of_ship(self): #Polymorphism
        print('This is a recreational ship.')

    def crewـsalary(self,salary:float):
        return self.num_of_crew * salary
    
    def trip_time(self,start:str,end:str):
        '''
        Parameters
        ----------
        start : str
            Like '2010/12/11'.
        end : str
            Like '2013/04/21'.

        Returns
        -------
        length_of_trip (day) : int .

        '''
        if int(end[0:4])-int(start[0:4]) < 0:
            return 'The end date of the journey cannot be before the beginning'
        
        elif int(end[0:4])-int(start[0:4]) == 0 and int(end[5:7])-int(start[5:7]) < 0:
            return 'The end date of the journey cannot be before the beginning'

        elif int(end[0:4])-int(start[0:4]) == 0 and int(end[5:7])-int(start[5:7]) == 0 and int(end[8:10])-int(start[8:10]) < 0:
            return 'The end date of the journey cannot be before the beginning'
        
        return int(end[8:10])-int(start[8:10]) + (int(end[5:7])-int(start[5:7]))*30 + (int(end[0:4])-int(start[0:4]))*360
            
class FreightM(Marine):
    
    travelـdistance = 0
    type_of_ship_cargo = 'fuel , clothing or food'
    fuel_in_the_tank = '10000 tons'
    
    def specify_travelـdistance (self,specifyed_travelـdistance:int):
        '''

        Parameters
        ----------
        travelـdistance : int
            Km.

        Returns
        -------
        None.

        '''
        self.travelـdistance = specifyed_travelـdistance
        
    def trip_time(self):
        if self.travelـdistance != 0:
            return f'{self.travelـdistance // 100 } hour(s)'
        else:
            print('Please specify the travel distance.')
    
    def type_of_ship(self): #Polymorphism
        print('This is a freigh ship.')



class Ground(Transport):
    '''
    The engine size for the Bicycle is zero
    '''
    
    def __init__(self,color:str,num_of_passenger:int,maxspeed:float,number_of_wheels:int,engine_size:float):
        super().__init__()
        self.__color = color #Encapsulation
        self.num_of_passenger = num_of_passenger
        self._maxspeed = maxspeed #Encapsulation
        self.number_of_wheels = number_of_wheels
        self.engine_size = engine_size
        self.place = 'On the ground'
        
    def color(self):
        return self.__color
        
    def change_color(self,new_color):
        self.__color = new_color
        print('The color changed...')
    
    def wash(self):
        print('Washing was done successfully.')
    
    def park(self):
        print('Your vehicle is parked')
    
    @abstractmethod
    def start(self):
        pass

class Car(Ground):
    
    travelـdistance = 0
    oil = '5 liters'
    fuel = '60 liters'

    def specify_travelـdistance (self,specifyed_travelـdistance:int):
        '''

        Parameters
        ----------
        travelـdistance : int
            Km.

        Returns
        -------
        None.

        '''
        self.travelـdistance = specifyed_travelـdistance
    
    def start(self): #Polymorphism
        print('Your car is ready...')
        
    def check_the_oil(self):
        print('You must first run «specify_travelـdistance» ,If you did this is the result: ')
        if self.travelـdistance <= 5000 :
            print('No need to change the oil')
        else:
            print('Change the oil')
        self.travelـdistance = 0
    
    def fuel_in_tank(self,distance):
        if distance/100*7 < 60:
            print(f'The fuel in tank is : {60 - distance/100*7}')
        else:
            print('The tank is empty...')

class Motorcycle(Ground):
    
    weight = '113 KG'
    fuel = '10 liters'
    
    def honking(self):
        print('Beeb')
    
    def braking(self):
        print('It stoped')
        
    def start(self): #Polymorphism
        print('Your motorcycle is ready...')

class Bicycle(Ground):
    
    weight = '8.8 KG'
    bicycle_size = 'It depends on the age of the user'

    def specify_bicycle_size(self,inch:float):
        self.bicycle_size = inch
        
    def pedaling(self):
        print('Your speed is increasing')
    
    def start(self): #Polymorphism
        print('Your bicycle is ready...')
    
    
    
class Air(Transport):
    '''
    Weight is based on tons. 
    '''
    
    def __init__(self,color:str,weight:float,num_of_passenger:int,maxspeed:float):
        super().__init__()
        self.__color = color #Encapsulation
        self.weight = weight
        self.num_of_passenger = num_of_passenger
        self._maxspeed = maxspeed #Encapsulation
        self.place = 'Oin the sky'
    
    def take_off(self):
        print('The plane took off successfully.')
        
    def Landing(self):
        print('The plane landed successfully.')
        
    def changing_the_altitude(self,first_altitude:float,delta:float,direction:str):
        '''
        Parameters
        ----------
        first_altitude : float
        delta : float
        direction : str
            'up' or 'down'.

        Returns
        -------
        None.

        '''
        
        print('Now the plane is at an altitude of ',end='')
        if direction == 'up' :
            print(first_altitude + delta)
        elif direction == 'down' :
            print(first_altitude - delta)
        else:
            print('...!')
            print('Check the direction argument')

    def color(self):
        return self.__color
        
    def change_color(self,new_color):
        self.__color = new_color
        print('The color changed...')

class Civil(Air):

    number_of_pilots = 2
    number_of_engines = 4
    length = '73 m'
   
    def flightـcrew(self):
        print('The flight crew is ready.')    
   
    def boarding(self):
        print('Passengers boarded and the plane is ready to take off.')
    
    def AirـTrafficـControlـTower(self):
        print('Permission to take off was issued.')

class PrivateJet(Air):
    
    price = '2 - 125 million dollars'
    number_of_pilots = 2
    propulsion = 'engine or propeller'

    def start(self):
        print('Your jet is ready')

    def refueling(self):
        print('Please wait a moment')
        for i in range(1,11):
            print(i*'.')
            time.sleep(1)
        time.sleep(1)
        print('Refueling was done')
    
    def wash(self):
        print('Your jet has been cleaned')

class Military(Air):
     
    tankـcapacity = '280 Liters'
    bomb = 50
    maximum_flight_height = '85000 ft'

    def shoot(self):
        print('The bomb was thrown.')
    
    def Changing_Direction(self):
        print('Please wait a moment...')
        for i in range(3):
            print('|')
            time.sleep(1)
            
        print(' ',end='')
        for i in range(8):
            print('-',end='')
            time.sleep(1)
        print('')    
        time.sleep(1)
        print('Changing direction was done.')
    
    def eject(self):
        print('The pilot ejected successfully.')
    
class FreightA(Air):
    
    load_capacity = '250 tons'
    number_of_engines = 6
    length = '84 m'
   
    def Loading(self):
        print('Loading done.')
    
    def unloading(self):
        print('Unloading done.')
    
    def start(self):
        print('Everything is ok , ready to take off')
    