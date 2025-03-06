import flet as ft

class EvenChecker:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
    
    def count_even_numbers(self):
        """Подсчитывает количество четных чисел из A, B, C и D."""
        even_count = 0
        numbers = [self.A, self.B, self.C, self.D]
        for number in numbers:
            if number % 2 == 0:
                even_count += 1
        return even_count

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    a_input = ft.TextField(label="Введите число A", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите число B", keyboard_type=ft.KeyboardType.NUMBER)
    c_input = ft.TextField(label="Введите число C", keyboard_type=ft.KeyboardType.NUMBER)
    d_input = ft.TextField(label="Введите число D", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_even_numbers(e):
        checker = EvenChecker()
        checker.A = int(a_input.value)
        checker.B = int(b_input.value)
        checker.C = int(c_input.value)
        checker.D = int(d_input.value)

        even_count = checker.count_even_numbers()
        is_two_even = (even_count == 2)

        result_text.value = (
            f"Количество четных чисел: {even_count}\n"
            f"Два числа являются четными: {is_two_even}"
        )
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_even_numbers)

    page.add(a_input, b_input, c_input, d_input, check_button, result_text)

ft.app(target=main)