import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №16"
    
    x = 8.52
    c = 9

    b = x + c ** 2
    y = np.cos(b) ** 2 + b * np.cos(a ** 2) ** 4
    a = 3 * np.sqrt(abs(b + c))

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    a_text = ft.Text(f'a = {a:.4f}', size=20)
    b_text = ft.Text(f'b = {b:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                a_text,
                b_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)