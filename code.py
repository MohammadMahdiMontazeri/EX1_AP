from abc import ABC, abstractmethod


class Transport(ABC):

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
    '''

    def color(self):
        return self.__color
        
    def change_color(self,new_color):
        self.__color = new_color
        print('The color changed...')

    
    @abstractmethod
    def place(self):
        pass
    pass

class Car(Ground):
    
    pass

class Motorcycle(Ground):
    
    pass

class Bicycle(Ground):
    
    pass
    
    
    
class Air(Transport):
    '''
    '''
    
    def color(self):
        return self.__color
        
    def change_color(self,new_color):
        self.__color = new_color
        print('The color changed...')

    
    @abstractmethod
    def place(self):
        pass

class Civil(Air):
    
    pass

class PrivateJet(Air):
    
    pass

class military(Air):
    
    pass

class FreightA(Air):
    
    pass