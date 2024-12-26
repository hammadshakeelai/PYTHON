#         self == this == instance == s
#          ^
#       convention
########################################################################################
########################################################################################
# CLASSES
########################################################################################
########################################################################################
class SuperHero:
    def __init__(self, name: str, power_level: int, Class: str) -> None:
        self.name = name
        self.power_level = power_level
        self.Class = Class
        self.called: bool = False
        
    def call(self) -> None:
        if self.called:
            print(f'{self.name} is already here dear citizens')
        else:
            self.called = True
            print(f'worry not {self.name} is now on its way here')

    def false_alarm(self) -> None:
        if self.called:
            self.called = False
            print(f"{self.name} is informed that this and will be returning to base")
        else:
            print(f'{self} was never called to begin with')

    def kill(self, enemy: str) -> None:
        if self.called:
            print(f'{self.name} wil kill {enemy}')
        else:
            print(f'{self.name} was not called to begin with')
            
    def __add__(self, other) -> str:
        return f'{self.name} and {other.name} Teamed up'
    
    def __mul__(self, other) -> str:
        return f'{self.name} * {other.name} are now married together'
    
    def __str__(self) -> str:#user friend
        return f'{self.name} (PowerLevel:{self.power_level}) (Class:{self.Class})'
    
    def __repr__(self) -> str:#developer friendly
        return f'SuperHero(name="{self.name}", power_level={self.power_level}, Class="{self.Class}")'


########################################################################################
########################################################################################
# OBJECTS:
wwe: SuperHero = SuperHero('john cena',88,'A')
jl: SuperHero = SuperHero('wonder woman',69,'G')
jll: SuperHero = SuperHero('woman',6,'x')

########################################################################################
#########################################################################################
# TERMINAL;
########################################################################################
#########################################################################################


# print(wwe.name,wwe.called)
# print(jl.name,'is here:',jl.called)
# jl.call()
# print(jl.name,'is here:',jl.called)
# print(wwe.name,wwe.called)
# jl.kill('bad man')
# wwe.kill('me')

# jl.call()
# wwe.call()
# print(wwe + jl)
# jl.kill("zikiriya")
# wwe.kill("wonder woman")
# print("look like a classic case of betryal")