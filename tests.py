import main
import unittest


class TestChooseMethods(unittest.TestCase):

    def test_choose_unit_class_should_return_right_unit_class(self):
        conv = main.Converter()
        ans = conv.choose_unit_class(2)
        self.assertEqual("Объем", ans)

    def test_choose_unit_class_should_return_error_message(self):
        conv = main.Converter()
        ans = conv.choose_unit_class(8)
        self.assertEqual("Wrong input", ans)

    #
    #

    def test_choose_unit_should_return_right_unit_class(self):
        conv = main.Converter()
        ans = conv.choose_unit("Расстояние", 3)
        self.assertEqual("миля", ans)

    def test_choose_unit_should_return_error_message(self):
        conv = main.Converter()
        ans = conv.choose_unit("Площадь", 6)
        self.assertEqual("Wrong input", ans)

    #
    #

    def test_process_unit_should_return_correct_dict(self):
        check_dict = {"килограмм": 2, "карат": 10000,
                       "грамм": 2000, "тонна": 0.002,
                       "фунт": 4.410, "унция": 70.54,
                       "драхма": 1128.8, "гран": 30864,
                       }

        conv = main.Converter()
        ans = conv.process_unit("Вес", "фунт", 4.410)
        self.assertEqual(check_dict, ans)