import flet as ft

class ConditionChecker:
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
        if self.k == 0:
            return self.l > self.m 
        elif self.k < 0:
            return 2 * self.l - 3 * self.n < self.m 
        return False

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    k_input = ft.TextField(label="Введите значение k", keyboard_type=ft.KeyboardType.NUMBER)
    l_input = ft.TextField(label="Введите значение l", keyboard_type=ft.KeyboardType.NUMBER)
    n_input = ft.TextField(label="Введите значение n", keyboard_type=ft.KeyboardType.NUMBER)
    m_input = ft.TextField(label="Введите значение m", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")

    def check_conditions(e):
        checker = ConditionChecker()
        checker.input_values(k_input.value, l_input.value, n_input.value, m_input.value)

        conditions_met = checker.check_conditions()
        result_text.value = f"Условия {('выполняются.' if conditions_met else 'не выполняются.')}"
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_conditions)

    page.add(k_input, l_input, n_input, m_input, check_button, result_text)

ft.app(target=main)