import flet as ft

class LogicalExpressionChecker:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Z = 0

    def evaluate_expression(self):
        """Вычисляет значение логического выражения X AND NOT (NOT Y OR Z) OR Y."""
        return (self.X and not (not self.Y or self.Z)) or self.Y

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    x_input = ft.TextField(label="Введите значение X (0 или 1)", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение Y (0 или 1)", keyboard_type=ft.KeyboardType.NUMBER)
    z_input = ft.TextField(label="Введите значение Z (0 или 1)", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_expression(e):
        checker = LogicalExpressionChecker()
        checker.X = int(x_input.value)
        checker.Y = int(y_input.value)
        checker.Z = int(z_input.value)

        result_value = checker.evaluate_expression()

        result_text.value = f"Значение логического выражения: {result_value}"
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_expression)

    page.add(x_input, y_input, z_input, check_button, result_text)

ft.app(target=main)