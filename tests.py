import main

import unittest


class TestChooseMethods(unittest.TestCase):

    def test_choose_unit_class_should_return_right_unit_class(self):
        ans = main.Converter.choose_unit_class(3)
        self.assertEqual("Температура", ans)

    def test_choose_unit_class_should_return_error_message(self):
        ans = main.choose_unit_class(3)
        self.assertEqual("none", ans)

    #
    #

    def test_choose_unit_weight_should_return_right_unit(self):
        ans = main.choose_unit_weight(3)
        self.assertEqual("килограмм", ans)

    def test_choose_unit_weight_should_return_error_message(self):
        ans = main.choose_unit_weight(30)
        self.assertEqual("none", ans)

    #

    def test_choose_unit_distance_should_return_right_unit(self):
        ans = main.choose_unit_distance(3)
        self.assertEqual("метр", ans)

    def test_choose_unit_distance_should_return_error_message(self):
        ans = main.choose_unit_distance(30)
        self.assertEqual("none", ans)

    #

    def test_choose_unit_volume_should_return_right_unit(self):
        ans = main.choose_unit_volume(3)
        self.assertEqual("галлон", ans)

    def test_choose_unit_volume_should_return_error_message(self):
        ans = main.choose_unit_volume(30)
        self.assertEqual("none", ans)

    #

    def test_choose_unit_area_should_return_right_unit(self):
        ans = main.choose_unit_area(3)
        self.assertEqual("гектар", ans)

    def test_choose_unit_area_should_return_error_message(self):
        ans = main.choose_unit_area(30)
        self.assertEqual("none", ans)

    #

    def test_choose_unit_temperature_should_return_right_unit(self):
        ans = main.choose_unit_temperature(3)
        self.assertEqual("кельвин", ans)

    def test_choose_unit_temperature_should_return_error_message(self):
        ans = main.choose_unit_temperature(30)
        self.assertEqual("none", ans)

    #

    def test_choose_unit_speed_should_return_right_unit(self):
        ans = main.choose_unit_speed(3)
        self.assertEqual("километр в час", ans)

    def test_choose_unit_speed_should_return_error_message(self):
        ans = main.choose_unit_speed(30)
        self.assertEqual("none", ans)


class TestConvertation(unittest.TestCase):

    def test_convert_weight_to_default_value(self):
        pass

    # ...

    def test_convert_distance_to_miles(self):
        pass