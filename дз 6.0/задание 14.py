import flet as ft

class LogicExpressionEvaluator:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Z = 0

    def evaluate_expression(self):
        """Вычисляет логическое выражение (X AND Y) OR (X AND NOT Z)."""
        return (self.X and self.Y) or (self.X and not self.Z)

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    x_input = ft.TextField(label="Введите значение X (0 или 1)", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение Y (0 или 1)", keyboard_type=ft.KeyboardType.NUMBER)
    z_input = ft.TextField(label="Введите значение Z (0 или 1)", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_logic_expression(e):
        evaluator = LogicExpressionEvaluator()
        evaluator.X = int(x_input.value)
        evaluator.Y = int(y_input.value)
        evaluator.Z = int(z_input.value)

        result = evaluator.evaluate_expression()

        result_text.value = f"Результат выражения (X AND Y) OR (X AND NOT Z): {result}"
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_logic_expression)

    page.add(x_input, y_input, z_input, check_button, result_text)

ft.app(target=main)