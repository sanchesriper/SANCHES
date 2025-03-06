import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 20"
    
    # Создаем текстовые поля для ввода t, l и y
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)
    l_input = ft.TextField(label="Введите значение для переменной l", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить K", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("K= ", size=20)
    
    def calculate():
        try:
            t = float(t_input.value)
            l = float(l_input.value)
            y = float(y_input.value)
            
            # Проверка на допустимость логарифма
            if y <= 0:
                raise ValueError("y должно быть больше нуля для вычисления логарифма.")
            
            # Вычисление формулы
            K = (2 * np.power(t, 2) + 3 * l + 7.2) / (np.log(y) + np.exp(2 * t))
            result_text.value = f"K = {K}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(t_input, l_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)