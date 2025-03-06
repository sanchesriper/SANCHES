import flet as ft


class NumberChecker:
    def __init__(self):
        self.N = 0

    def input_number(self, n_value):
        self.N = int(n_value)

    def check_conditions(self):
        condition1 = (self.N % 3 == 0 and self.N % 9 != 0)
        condition2 = (self.N % 4 == 0 and self.N % 5 == 0 and self.N % 24 == 0)
        return condition1, condition2


def main(page: ft.Page):
    page.title = "Практическая работа №6"

    n_input = ft.TextField(label="Введите число N", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")

    def check_numbers(e):
        checker = NumberChecker()
        checker.input_number(n_input.value)

        conditions_met = checker.check_conditions()
        result_text.value = (
            f"Условие 1 (N делится на 3, не делится на 9): {conditions_met[0]}\n"
            f"Условие 2 (N делится на 4, 5 и 24): {conditions_met[1]}"
        )
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_numbers)

    page.add(n_input, check_button, result_text)

ft.app(target=main)