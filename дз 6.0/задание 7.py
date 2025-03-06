import flet as ft

class NumberChecker:
    def __init__(self):
        self.N = 0

    def input_number(self, n_value):
        self.N = int(n_value)

    def check_conditions(self):
        is_even = (self.N % 2 == 0)
        divisible_by_7 = (self.N % 7 == 0)
        not_divisible_by_11 = (self.N % 11 != 0)
        not_divisible_by_13 = (self.N % 13 != 0)

        return is_even and divisible_by_7 and not_divisible_by_11 and not_divisible_by_13

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    n_input = ft.TextField(label="Введите число N", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")

    def check_n(e):
        checker = NumberChecker()
        checker.input_number(n_input.value)

        conditions_met = checker.check_conditions()
        result_text.value = f"Число {checker.N} " + ("удовлетворяет условиям." if conditions_met else "не удовлетворяет условиям.")
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_n)

    page.add(n_input, check_button, result_text)

ft.app(target=main)