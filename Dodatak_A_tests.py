import unittest
from unittest.mock import patch
from Dodatak_A import OperationsManager, login_success, main


class Dodatak_A_tests(unittest.TestCase):

    def test_perform_division(self):
        manager = OperationsManager(10, 2)
        result = manager.perform_division()
        self.assertEqual(result, 5)

    def test_perform_division_by_zero(self):
        manager = OperationsManager(10, 0)
        result = manager.perform_division()
        self.assertEqual(result, float('nan'))

    def test_perform_division_with_string(self):
        manager = OperationsManager("Ivan", 2)
        self.assertRaises(TypeError, manager.perform_division)

    # def test_login_success(self):
    #     user_input = ["root", "123", "10", "2", "2+2"]
    #     expected_output = "Login success!\n"
    #     with patch('builtins.input', side_effect=user_input):
    #         with patch('getpass.getpass', return_value=user_input[1]):
    #             with patch('builtins.print') as mock_print:
    #                 main()
    #                 self.assertEqual(mock_print.getvalue(), expected_output) #TODO

if __name__ == '__main__':
    unittest.main()

