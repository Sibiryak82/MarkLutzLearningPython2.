# Файл manage-inst-deco

# Декоратор классов для трассировки внешних опреаций,
# извлекающих атрибуты экземпляров

def Tracer(aClass):                                 # При декорировании @
    class Wrapper:
        def __init__(self, *args, **kargs):         # При создании экземпляров
            self.wrapped = aClass(*args, **kargs)   # Использование имени из
                                                    # объемлющей области видимости
        def __getattr__(self, attrname):
            print('Trace:', attrname)               # Перехват всех атрибутов кроме .wrapped
            return getattr(self.wrapped, attrname)  # делегирование внутреннему объекту
                                                    
    return Wrapper

@Tracer
class Person:                                       # Person = Tracer(Person)
    def __init__(self, name, hours, rate):          # Wrapper запоминает Person
        self.name = name
        self.hours = hours
        self.rate = rate                            # Операции доступа внутри методов не отслеживаюся
    def pay(self):
        return self.hours * self.rate

bob = Person('Bob', 40, 50)                         # bob - на самом деле экземпляр Wrapper
print(bob.name)                                     # Wrapper содежит внедренный экземпляр Person
print(bob.pay())                                    # Запускается __getattr__
