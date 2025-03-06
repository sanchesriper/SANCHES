import flet as ft

class NumberChecker:
    def __init__(self):
        self.N = 0

    def check_n_conditions(self):
        """Проверяет условия для числа N."""
        return (
            (self.N % 2 == 0) and
            (self.N % 3 != 0) and
            (self.N % 7 == 0) and
            ((self.N % 5 != 0 and self.N % 4 != 0) or 
             (self.N % 8 == 0 and self.N % 11 == 0))
        )

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    n_input = ft.TextField(label="Введите число N", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_numbers(e):
        checker = NumberChecker()
        checker.N = int(n_input.value)

        n_conditions_met = checker.check_n_conditions()

        result_text.value = f"Условия для числа N выполнены: {n_conditions_met}"
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_numbers)

    page.add(n_input, check_button, result_text)

ft.app(target=main)