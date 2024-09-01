class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return str(f"{self.__class__.__name__}(width={self.width}, height={self.height})")

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture = ""
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        for i in range(self.height):
            picture += ("*" * self.width) + "\n" 
        return picture

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_amount_inside(self, shape):
        fit_in_height = self.get_height() // shape.get_height()
        fit_in_width = self.get_width() // shape.get_width()
        fit_in_shape = fit_in_height * fit_in_width
        return fit_in_shape




 
Rectangle(2,3).get_amount_inside(Rectangle(3, 6))
print(Rectangle(20,4))

class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"{__class__.__name__}(side={self.height})"

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height

    def set_side(self, side):
        self.set_width(side)

s1 = Square(2)
s1.set_height(4)
print(s1)
