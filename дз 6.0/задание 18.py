import flet as ft

class PurchaseCalculator:
    def __init__(self):
        self.total_amount = 0

    def calculate_discount(self):
        """Вычисляет скидку в зависимости от суммы покупки."""
        if 10000 < self.total_amount < 20000:
            discount = 0.05
        elif 20000 <= self.total_amount < 50000:
            discount = 0.10
        else:
            discount = 0.0
        return discount

    def final_price(self):
        """Возвращает окончательную цену с учетом скидки."""
        discount = self.calculate_discount()
        return self.total_amount * (1 - discount)

def main(page: ft.Page):
    page.title = "Практическая работа №6"

    amount_input = ft.TextField(label="Введите общую стоимость покупки (в рублях)", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def calculate(e):
        calculator = PurchaseCalculator()
        calculator.total_amount = float(amount_input.value)

        final_price = calculator.final_price()
        discount = calculator.calculate_discount() * 100
        
        result_text.value = (
            f"Сумма скидки: {discount}%\n"
            f"Окончательная цена: {final_price:.2f} руб."
        )
        result_text.update()

    calculate_button = ft.ElevatedButton("Рассчитать", on_click=calculate)

    page.add(amount_input, calculate_button, result_text)

ft.app(target=main)