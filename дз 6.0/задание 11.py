import flet as ft

class PurchaseCalculator:
    def __init__(self):
        self.price = 0

    def calculate_discount(self):
        """Рассчитывает стоимость с учетом скидки."""
        discount = 0.0
        if 4000 < self.price < 6000:
            discount = 0.05
        elif 6000 < self.price < 10000:
            discount = 0.10
        return self.price * (1 - discount)

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    price_input = ft.TextField(label="Введите стоимость покупки", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")

    def calculate_purchase(e):
        calculator = PurchaseCalculator()
        calculator.price = float(price_input.value)

        final_price = calculator.calculate_discount()

        result_text.value = f"Стоимость с учетом скидки: {final_price:.2f} рублей"
        result_text.update()

    calculate_button = ft.ElevatedButton("Рассчитать", on_click=calculate_purchase)

    page.add(price_input, calculate_button, result_text)

ft.app(target=main)