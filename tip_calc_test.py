import io
from unittest import mock, TestCase

from tip_calculator import bill, tip_input, num_people, tax, total_bill, payment_per_person,tip_calc, total_bill_float, tip_amount_float, tip_and_total

class TestTipCalcStrings(TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_ingredients(self, mock_stdout):
        bill()

        self.assertEqual(
            "How Much is the total bill?: ",
            mock_stdout.getvalue()
        )

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_ingredients(self, mock_stdout):
        tip_input()

        self.assertEqual(
            "What Percentage tip would you like to give?: %  ",
            mock_stdout.getvalue()
        )
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_ingredients(self, mock_stdout):
        tip_input(input())

        self.assertEqual(
        if tip_input >= 10 < 20:
            print("You are a great tipper!")
        else:
         if tip_input > 20:
        print("You are the world's greatest tipper!")
        else:
            if tip_input>0<10:
            print("You are so damn cheap!")
            cheap=int(input("One Last Try for A REAL TIP!:%  "))
        else:
            if tip_input<=0:
                print("You should be ashamed of yourself. I never met anyone so cheap. I am going to call your mamma!")
        )