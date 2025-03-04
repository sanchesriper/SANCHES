import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание #27"

    t = -3
    a = 76

    c = t**2 + np.sqrt(a)
    x = np.log(np.abs(c)) + a**2
    y = np.tan(4*x) + np.sin(x)**2

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)
    c_text = ft.Text(f'c = {c:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                x_text,
                c_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)