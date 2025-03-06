import flet as ft

class NumberChecker:
    def __init__(self):
        self.N = 0

    def input_number(self, n_value):
        self.N = int(n_value)

    def is_multiple_of_four_or_seven(self):
        """Проверяет, кратно ли N четырем или семи."""
        return self.N % 4 == 0 or self.N % 7 == 0

    def is_multiple_of_five_and_not_ending_in_zero(self):
        """Проверяет, кратно ли N пяти и не оканчивается ли на ноль."""
        return self.N % 5 == 0 and self.N % 10 != 0

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    n_input = ft.TextField(label="Введите число N", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")

    def check_numbers(e):
        checker = NumberChecker()
        checker.input_number(n_input.value)

        multiple_of_four_or_seven = checker.is_multiple_of_four_or_seven()
        multiple_of_five_not_zero = checker.is_multiple_of_five_and_not_ending_in_zero()

        result_text.value = (
            f"Число N кратно 4 или 7: {multiple_of_four_or_seven}\n"
            f"Число N кратно 5 и не оканчивается на ноль: {multiple_of_five_not_zero}"
        )
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_numbers)

    page.add(n_input, check_button, result_text)

ft.app(target=main)