import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №30"

    t = 3
    b = 4.2

    a = t + b**3
    x = t**2 * np.sqrt(np.abs(a + b))
    y = np.log(np.abs(x + a**2)) ** 5

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)
    a_text = ft.Text(f'a = {a:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                x_text,
                a_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)