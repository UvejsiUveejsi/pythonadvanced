class Rectangle:
    def __init__(self, length:float, width:float):
        self.length=length
        self.width=width

    def __getattr__(self, item)->float|None:
        if item=="length":
            return self.length
        elif item =="width":
            return self.width
        else:
            print("no attributes correspond")

    def calculate(self)->float:
        return self.width*self.length

    def perimeter(self)->float:
        return (self.length+self.width)*2

def main():
    r1=Rectangle(9.5, 12)
    print(r1.calculate())

if __name__=="__main__":
    main()