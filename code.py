from abc import ABC, abstractmethod


class Transport(ABC):

    pass     
        


class Marine(Transport):
    
    pass

class Recreational(Marine):
    
    pass
    
class FreightM(Marine):
    
    pass



class Ground(Transport):
    
    pass

class Car(Ground):
    
    pass

class Motorcycle(Ground):
    
    pass

class Bicycle(Ground):
    
    pass
    
    
    
class Air(Transport):
    
    pass

class Civil(Air):
    
    pass

class PrivateJet(Air):
    
    pass

class military(Air):
    
    pass

class FreightA(Air):
    
    pass