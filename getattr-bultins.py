# Файл getattr-bultins.py

class GetAttr:
    eggs = 88                                         # eggs храниться в классе, spam - в экземпляре
    def __init__(self):
        self.spam = 77
    def __len__(self):                                # Реализовать здесь len,
                                                      # иначе __getattr__ вызывается с __len__
        print('__len__: 42')
        return 42
    def __getattr__(self, attr):                      # Предоставить __str__ по запросу,
                                                      # иначе фиктивную функцию
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute(object):                           # object требуется в Python 2.X
                                                      # и подразумевается в Python 3.X
    eggs = 88                                         # В Python 2.X все автоматически
                                                      # isinstance(object)
    def __init__(self):                               # Но нужно наследовать от object,
                                                      # чтобы получить инструменты нового
        self.spam = 77                                # стиля, включая __getattibute__
                                                      # и ряд стандартных методов __X__
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None
for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))
    X = Class()
    X.eggs                                            # Атрибут класса
    X.spam                                            # Атрибут экземпляра
    X.other                                           # Отсутвующий атрибут
    len(X)                                            # __len__ определено явно
    
# Классы нового стиля обязаны поддерживать [], прямой вызов: переопределитель

    try: X[0]                                         # __getitem__?
    except: print('fail []')

    try: X + 99                                       # __add__?
    except: print('fail +')

    try: X()                                          # __call__? (неявно через встроенную операцию)
    except: print('fail ()')

    X.__call__()                                      # __call__? (явно, не наследуется)
    print(X.__str__())                                # __str__? (явно, наследуется от типа)
    print(X)                                          # __str__? (неявно через встроенную операцию
    


        
