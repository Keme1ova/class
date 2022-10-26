class Iphone:
    def __init__(self, model, color, memory, status, year, size):
        self.m=model
        self.c=color
        self.mem=memory
        self.s=status
        self.y=year
        self.size=size


qwerty

    def take_photo(self, yes):
    def can_call(self, yes):
        return f'Photo - {yes}\n'\
               f'Call - {yes}\n'

    def __str__(self):
        return f'{self.m}\n' \
               f'{self.c}\n' \
               f'{self.mem}\n' \
               f'{self.s}]\n' \
               f'{self.y}\n' \
               f'{self.size}'

iphone11 = class Iphone(True, True, True, True, True, True)
print(iphone11.take_photo(True))
print(iphone11.can_call(True))



class IphoneX(Iphone):
    def __init__(self, model, color, memory, status, year, size, new, ovalcamera):
        super().__init__(model, color, memory, status, year, size)
        self.n = new
        self.o=ovalcamera

    def __str__(self):
        return super(IphoneX, self).__str__()+f'{self.n}\n' \
                                              f'{self.o}'

iphone12 = IphoneX(model=True, color=True, memory=True, status=True, year=True, size=True, new=True, ovalcamera=False)

print(iphone12.take_photo(True))
print(iphone12.can_call(True))
print(iphone12)



