import flet as ft

class ScholarshipChecker:
    def __init__(self):
        self.physics = 0
        self.math = 0
        self.informatics = 0

    def is_scholarship_awarded(self):
        """Проверяет, получит ли студент стипендию."""
        return self.physics >= 4 and self.math >= 4 and self.informatics >= 4

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    physics_input = ft.TextField(label="Введите оценку по физике", keyboard_type=ft.KeyboardType.NUMBER)
    math_input = ft.TextField(label="Введите оценку по математике", keyboard_type=ft.KeyboardType.NUMBER)
    informatics_input = ft.TextField(label="Введите оценку по информатике", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_scholarship(e):
        checker = ScholarshipChecker()
        checker.physics = int(physics_input.value)
        checker.math = int(math_input.value)
        checker.informatics = int(informatics_input.value)

        scholarship_awarded = checker.is_scholarship_awarded()

        result_text.value = (
            f"Студент {'получает' if scholarship_awarded else 'не получает'} стипендию."
        )
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=check_scholarship)

    page.add(physics_input, math_input, informatics_input, check_button, result_text)

ft.app(target=main)