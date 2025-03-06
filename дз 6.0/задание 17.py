import flet as ft

class DivisibilityChecker:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
    
    def is_one_divisible_by_3_and_another_by_5(self):
        """Проверяет, что одно число делится на 3, а другое на 5."""
        divisible_by_3 = [self.A, self.B, self.C, self.D].count(0)
        divisible_by_5 = [self.A, self.B, self.C, self.D].count(0)
        return (divisible_by_3 >= 1) and (divisible_by_5 >= 1)

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    a_input = ft.TextField(label="Введите число A", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите число B", keyboard_type=ft.KeyboardType.NUMBER)
    c_input = ft.TextField(label="Введите число C", keyboard_type=ft.KeyboardType.NUMBER)
    d_input = ft.TextField(label="Введите число D", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_numbers(e):
        checker = DivisibilityChecker()
        checker.A = int(a_input.value)
        checker.B = int(b_input.value)
        checker.C = int(c_input.value)
        checker.D = int(d_input.value)

        condition_met = checker.is_one_divisible_by_3_and_another_by_5()

        result_text.value = (
            f"Одно число делится на 3, а другое делится на 5: {condition_met}"
        )
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_numbers)

    page.add(a_input, b_input, c_input, d_input, check_button, result_text)

ft.app(target=main)