#         self == this == instance == s
#          ^
#       convention
class SuperHero:
    def __init__(self,name: str,power_level: int,Class: str) -> None:
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

    def false_alarm(self):
        if self.called:
            self.called = False
            print(f"{self.name} is informed that this was a false alarm")
        else:
            print(f'{self} was never called to begin with')

    def kill(self,enemy: str) -> None:
        if self.called:
            print(f'{self.name} wil kill {enemy}')
        else:
            print(f'{self.name} was not called to begin with')
# OBJECTS:
wwe: SuperHero = SuperHero('john cena',88,'A')
jl: SuperHero = SuperHero('wonder woman',69,'X')
print(wwe.name,wwe.called)
print(jl.name,jl.called)
jl.call()
print(jl.name,jl.called)
print(wwe.name,wwe.called)
jl.kill('sexy man')
wwe.kill('me')