import flet as ft

class SalaryCalculator:
    def __init__(self):
        self.experience = 0

    def calculate_bonus_percentage(self):
        """Вычисляет надбавку к зарплате в зависимости от стажа."""
        if 5 <= self.experience < 10:
            return 0.02
        elif 10 <= self.experience < 20:
            return 0.10
        else:
            return 0.0

    def calculate_final_salary(self, base_salary):
        """Вычисляет окончательную зарплату с учетом надбавки."""
        bonus_percentage = self.calculate_bonus_percentage()
        return base_salary * (1 + bonus_percentage)

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    experience_input = ft.TextField(label="Введите стаж работы (в годах)", keyboard_type=ft.KeyboardType.NUMBER)
    salary_input = ft.TextField(label="Введите базовую зарплату (в рублях)", keyboard_type=ft.KeyboardType.NUMBER)
    
    result_text = ft.Text("")

    def calculate(e):
        calculator = SalaryCalculator()
        calculator.experience = int(experience_input.value)
        base_salary = float(salary_input.value)

        final_salary = calculator.calculate_final_salary(base_salary)
        bonus_percentage = calculator.calculate_bonus_percentage() * 100

        result_text.value = (
            f"Надбавка к зарплате: {bonus_percentage:.2f}%\n"
            f"Окончательная зарплата: {final_salary:.2f} руб."
        )
        result_text.update()

    calculate_button = ft.ElevatedButton("Рассчитать", on_click=calculate)

    page.add(experience_input, salary_input, calculate_button, result_text)

ft.app(target=main)