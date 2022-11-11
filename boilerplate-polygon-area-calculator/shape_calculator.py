class Rectangle:
    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        st = ""
        if (self.height < 50) and (self.width < 50):
            for i in range(self.height):
                st += "*" * self.width + '\n'
        else:
            st = "Too big for picture."
        return st

    def get_amount_inside(self, another):
        heights = self.height // another.height
        widths = self.width // another.width
        amount = heights * widths
        return amount

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)
        self.length = length
        self.width = self.length
        self.height = self.length

    def set_side(self, length):
        self.length = length
        self.width = self.length
        self.height = self.length

    def set_width(self, width):
        self.length = width

    def set_height(self, height):
        self.length = height

    def __str__(self):
        return f'Square(side={self.length})'


