import flet as ft

class CallCostCalculator:
    def __init__(self):
        self.t = 0
        self.dt = 0
        self.s = 0.0
        self.d = 0

    def calculate_cost(self):
        base_cost = self.dt * self.s

        if self.t >= 22 or self.t < 8:
            base_cost *= 0.8

        if self.d == 6 or self.d == 7:
            base_cost *= 0.9

        return base_cost

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    time_input = ft.TextField(label="Введите время разговора (0-24)", keyboard_type=ft.KeyboardType.NUMBER)
    duration_input = ft.TextField(label="Введите продолжительность разговора (минуты)", keyboard_type=ft.KeyboardType.NUMBER)
    price_input = ft.TextField(label="Введите стоимость минуты разговора", keyboard_type=ft.KeyboardType.NUMBER)
    day_input = ft.TextField(label="Введите день недели (1-7)", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def calculate_cost(e):
        calculator = CallCostCalculator()
        calculator.t = int(time_input.value)
        calculator.dt = int(duration_input.value)
        calculator.s = float(price_input.value)
        calculator.d = int(day_input.value)

        total_cost = calculator.calculate_cost()
        result_text.value = f"Итоговая стоимость разговора: {total_cost:.2f} руб."
        result_text.update()

    calculate_button = ft.ElevatedButton("Рассчитать", on_click=calculate_cost)

    page.add(time_input, duration_input, price_input, day_input, calculate_button, result_text)

ft.app(target=main)