import unittest
import math
from polygon_area_calc.polygon_area_calc import Rectangle, Square  # make sure polygon_area_calc.py defines both classes


class TestShapes(unittest.TestCase):

    # 1–3: class relationships / instances
    def test_square_is_subclass(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_distinct_classes(self):
        self.assertNotEqual(Rectangle, Square)

    def test_instance_types(self):
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Rectangle)

    # 4–5: string representations
    def test_rectangle_repr(self):
        self.assertEqual(repr(Rectangle(3, 6)), "Rectangle(width=3, height=6)")

    def test_square_repr(self):
        self.assertEqual(repr(Square(5)), "Square(side=5)")

    # 6–7: area
    def test_rectangle_area(self):
        self.assertEqual(Rectangle(3, 6).get_area(), 18)

    def test_square_area(self):
        self.assertEqual(Square(5).get_area(), 25)

    # 8–9: perimeter
    def test_rectangle_perimeter(self):
        self.assertEqual(Rectangle(3, 6).get_perimeter(), 18)

    def test_square_perimeter(self):
        self.assertEqual(Square(5).get_perimeter(), 20)

    # 10–11: diagonal
    def test_rectangle_diagonal(self):
        self.assertTrue(math.isclose(Rectangle(3, 6).get_diagonal(), 6.708203932499369))

    def test_square_diagonal(self):
        self.assertTrue(math.isclose(Square(5).get_diagonal(), 7.0710678118654755))

    # 12–14: mutation changes repr
    def test_rectangle_repr_changes_after_setters(self):
        r = Rectangle(3, 6)
        r.set_width(7)
        r.set_height(8)
        self.assertEqual(repr(r), "Rectangle(width=7, height=8)")

    def test_square_repr_changes_after_set_side(self):
        s = Square(5)
        s.set_side(9)
        self.assertEqual(repr(s), "Square(side=9)")

    def test_square_repr_changes_after_set_width_height(self):
        s = Square(5)
        s.set_width(12)   # should set both
        self.assertEqual(repr(s), "Square(side=12)")
        s.set_height(4)   # should set both
        self.assertEqual(repr(s), "Square(side=4)")

    # 15–17: get_picture
    def test_rectangle_picture(self):
        r = Rectangle(3, 2)
        expected = "***\n***\n"
        self.assertEqual(r.get_picture(), expected)

    def test_square_picture(self):
        s = Square(3)
        expected = "***\n***\n***\n"
        self.assertEqual(s.get_picture(), expected)

    def test_picture_too_big(self):
        r = Rectangle(51, 2)  # width > 50
        self.assertEqual(r.get_picture(), "Too big for picture.")
        s = Square(60)
        self.assertEqual(s.get_picture(), "Too big for picture.")

    # 18–20: get_amount_inside
    def test_amount_inside_rect_square(self):
        self.assertEqual(Rectangle(15, 10).get_amount_inside(Square(5)), 6)

    def test_amount_inside_rect_rect_one(self):
        self.assertEqual(Rectangle(4, 8).get_amount_inside(Rectangle(3, 6)), 1)

    def test_amount_inside_rect_rect_zero(self):
        self.assertEqual(Rectangle(2, 3).get_amount_inside(Rectangle(3, 6)), 0)


if __name__ == '__main__':
    unittest.main()
