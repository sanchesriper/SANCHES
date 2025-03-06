import flet as ft

class ConditionsChecker:
    def __init__(self):
        self.k = 0
        self.l = 0
        self.n = 0
        self.m = 0

    def input_values(self, k_value, l_value, n_value, m_value):
        self.k = int(k_value)
        self.l = int(l_value)
        self.n = int(n_value)
        self.m = int(m_value)

    def check_conditions(self):
        condition1 = (self.n > 1) or (self.m <= 1 + self.k)
        condition2 = self.n > 2 and (self.m**2 > 1)
        return condition1, condition2

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    k_input = ft.TextField(label="Введите число k", keyboard_type=ft.KeyboardType.NUMBER)
    l_input = ft.TextField(label="Введите число l", keyboard_type=ft.KeyboardType.NUMBER)
    n_input = ft.TextField(label="Введите число n", keyboard_type=ft.KeyboardType.NUMBER)
    m_input = ft.TextField(label="Введите число m", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")

    def check_conditions(e):
        checker = ConditionsChecker()
        checker.input_values(k_input.value, l_input.value, n_input.value, m_input.value)

        conditions_met = checker.check_conditions()
        result_text.value = (
            f"Условие 1 (n > 1 или m <= 1 + k): {conditions_met[0]}\n"
            f"Условие 2 (если n > 2, то m^2 > 1): {conditions_met[1]}"
        )
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_conditions)

    page.add(k_input, l_input, n_input, m_input, check_button, result_text)

ft.app(target=main)