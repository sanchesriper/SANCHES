import flet as ft

class DepositCalculator:
    def __init__(self):
        self.amount = 0
        
    def input_amount(self, amount_value):
        self.amount = float(amount_value)
        
    def calculate_payout(self):
        if self.amount <= 50000:
            annual_rate = 0.16
        elif self.amount <= 100000:
            annual_rate = 0.18
        else:
            annual_rate = 0
         
        payout = self.amount * (1 + annual_rate)
        return payout

def main(page: ft.Page):
    page.title = "Практическая работа №6"
    
    amount_input = ft.TextField(label="Введите сумму вклада (руб.)", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")
    
    def calculate(e):
        calculator = DepositCalculator()
        calculator.input_amount(amount_input.value)

        payout = calculator.calculate_payout()
        result_text.value = f"Сумма выплаты по депозиту: {payout:.2f} руб."
        
        result_text.update()

    calculate_button = ft.ElevatedButton("Рассчитать", on_click=calculate)
    
    page.add(amount_input, calculate_button, result_text)

ft.app(target=main)