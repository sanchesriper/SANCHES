import flet as ft

class NumberChecker:
    def __init__(self):
       self.A = 0
       self.B = 0
       self.C = 0
    
    def is_one_even(self):
        """Проверяет, только одно из чисел А и В четное."""
        return (self.A % 2 == 0) != (self.B % 2 == 0)

    def are_all_multiples_of_three(self):
        """Проверяет, каждое из чисел А, В, С кратно трем."""
        return (self.A % 3 == 0) and (self.B % 3 == 0) and (self.C % 3 == 0)

def main(page: ft.Page):
    page.title = "Практическая работа №6"


    
    a_input = ft.TextField(label="Введите число А", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите число В", keyboard_type=ft.KeyboardType.NUMBER)
    c_input = ft.TextField(label="Введите число с", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_numbers(e):

        checker = NumberChecker()
        checker.A = int(a_input.value)
        checker.B = int(b_input.value)
        checker.C = int(c_input.value)

        one_even = checker.is_one_even()
        all_multiples_of_three = checker.are_all_multiples_of_three()


        result_text.value = (
            f"Только одно из чисел А и В четное: {one_even}\n"
            f"Каждое из чисел А, В, С кратно трем: {all_multiples_of_three}"
        )
        result_text.update()

    
    check_button = ft. ElevatedButton("Проверить", on_click=check_numbers)


    page.add(a_input, b_input, c_input, check_button, result_text)


ft.app(target=main)