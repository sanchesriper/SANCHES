import flet as ft

class ConditionChecker:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.k = 0

    def input_values(self, n_value, m_value, k_value):
        self.n = int(n_value)
        self.m = int(m_value)
        self.k = int(k_value)

    def check_conditions(self):
        return (self.n + self.m > self.k) and not (self.n > self.k and self.m >= 1)

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    n_input = ft.TextField(label="Введите число n", keyboard_type=ft.KeyboardType.NUMBER)
    m_input = ft.TextField(label="Введите число m", keyboard_type=ft.KeyboardType.NUMBER)
    k_input = ft.TextField(label="Введите число k", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")

    def check_conditions(e):
        checker = ConditionChecker()
        checker.input_values(n_input.value, m_input.value, k_input.value)

        conditions_met = checker.check_conditions()

        result_text.value = f"Условия выполнены: {conditions_met}"
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_conditions)

    page.add(n_input, m_input, k_input, check_button, result_text)

ft.app(target=main)