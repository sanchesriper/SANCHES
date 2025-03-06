import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 24"
    
    # Создаем текстовые поля для ввода k и y
    k_input = ft.TextField(label="Введите значение для переменной k", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить U", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("U= ", size=20)
    
    def calculate():
        try:
            k = float(k_input.value)
            y = float(y_input.value)
            # Проверяем значение y для того, чтобы избежать ошибки при вычислении корня и логарифма
            if y < 0:
                raise ValueError("y должно быть неотрицательным для вычисления квадратного корня.")
            if 2*k + 4.3 <= 0:
                raise ValueError("Аргумент логарифма должен быть больше нуля.")
            
            U = np.log(2 * k + 4.3) / (np.exp(k) + y) + np.sqrt(y)
            result_text.value = f"U = {U}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(k_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)