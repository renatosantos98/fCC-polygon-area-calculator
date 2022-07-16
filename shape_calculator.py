class Rectangle:
    def __init__(self, width, height):
        """When a Rectangle object is created, it is initialized with `width` and `height` attributes."""
        self.width = width
        self.height = height

    def __str__(self):
        """If an instance of a Rectangle is represented as a string, it looks like: `Rectangle(width=5, height=10)`."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        """Sets the `width` attribute value of the Rectangle object."""
        self.width = width

    def set_height(self, height):
        """Sets the `height` attribute value of the rectangle object."""
        self.height = height

    def get_area(self):
        """Calculates the area of the Rectangle object by multiplying width and height: `width * height`."""
        return self.width * self.height

    def get_perimeter(self):
        """Calculates the perimeter of the Rectangle object by adding all four sides of the polygon: `2 * width + 2 * height`."""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Calculates the diagonal of the Rectangle object: `(width ** 2 + height ** 2) ** .5`."""
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        """Returns a string that represents the shape using lines of "*". The number of lines are equal to the height and the number of "*" in each line are equal to the width. If the width or height is larger than 50, it returns the string: `Too big for picture.`."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        display_string = (("*" * self.width) + "\n") * self.height
        return display_string

    def get_amount_inside(self, shape):
        """Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4."""
        # This will return only as many whole shapes that can fit across multiplied by the number of whole shapes that can fit vertically.
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    """The Square class is a subclass of Rectangle. It is able to access the Rectangle class methods, but it also contains a `set_side` method. Additionally, the `set_width` and `set_height` methods on the Square class set both the width and height simultaneously."""

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        """If an instance of a Square is represented as a string, it looks like: `Square(side=9)`."""
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        """Sets the `width` attribute value of the Rectangle object."""
        self.width = side
        self.height = side

    def set_height(self, side):
        """Sets the `height` attribute value of the rectangle object."""
        self.height = side
        self.width = side
