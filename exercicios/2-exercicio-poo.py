class Rectangle:
    def calc_area(self, width , length):
        return f'The rectangle area is {width * length}m²'

    def calc_perimeter(self, width , length):
        return f'The rectangle perimeter is {2 * (width + length)}m'

rect = Rectangle()

print(rect.calc_area(40, 30))
print(rect.calc_perimeter(100, 300))