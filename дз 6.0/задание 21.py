import flet as ft

class ExperienceCoefficient:
    def __init__(self):
        self.experience_years = 0
    
    def get_coefficient(self):
        """Определяет коэффициент в зависимости от стажа работы."""
        if self.experience_years < 2:
            return 11
        elif 2 <= self.experience_years < 5:
            return 12
        else:
            return 13

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    experience_input = ft.TextField(label="Введите стаж работы в годах", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")

    def calculate_coefficient(e):
        coeff_checker = ExperienceCoefficient()
        coeff_checker.experience_years = int(experience_input.value)
        
        coefficient = coeff_checker.get_coefficient()

        result_text.value = f"Коэффициент учета стажа: {coefficient}"
        result_text.update()

    check_button = ft.ElevatedButton("Проверить", on_click=calculate_coefficient)

    page.add(experience_input, check_button, result_text)

ft.app(target=main)