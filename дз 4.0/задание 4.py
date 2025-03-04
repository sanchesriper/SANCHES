import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №4"
    
    x = 2.7
    t = -6

    a = np.log10(x)
    b = np.sqrt(x**2 + t**2)
    y = 5 * np.sqrt(abs(a - b * x))

    y_text = ft.Text(f'y = {y:.2f}', size=20)
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    b_text = ft.Text(f'b = {b:.2f}', size=20)

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