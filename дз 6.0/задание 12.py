import flet as ft

class ConditionChecker:
    def __init__(self):
        self.k = 0
        self.l = 0
        self.n = 0
        self.m = 0
    
    def check_conditions(self):
        """Проверяет заданные условия."""
        condition1 = (self.k + 1 + self.m + self.n) > 0
        
        if self.k > 0:
            condition2 = (2 * self.m) > 1
            return condition1 and condition2
        elif self.k < 0:
            condition3 = self.n > (3 * self.l)
            return condition1 and condition3
        
        return condition1

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    k_input = ft.TextField(label="Введите число k", keyboard_type=ft.KeyboardType.NUMBER)
    l_input = ft.TextField(label="Введите число l", keyboard_type=ft.KeyboardType.NUMBER)
    n_input = ft.TextField(label="Введите число n", keyboard_type=ft.KeyboardType.NUMBER)
    m_input = ft.TextField(label="Введите число m", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_conditions(e):
        checker = ConditionChecker()
        checker.k = int(k_input.value)
        checker.l = int(l_input.value)
        checker.n = int(n_input.value)
        checker.m = int(m_input.value)

        result = checker.check_conditions()

        result_text.value = f"Условия выполняются: {result}"
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_conditions)

    page.add(k_input, l_input, n_input, m_input, check_button, result_text)

ft.app(target=main)