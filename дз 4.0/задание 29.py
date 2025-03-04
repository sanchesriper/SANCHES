import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №29"

    a = 6
    b = 4.3

    x = np.exp(2 * a) + np.sqrt(b)
    p = x * (a ** 3)
    y = np.log(np.abs(p)) ** 3 + x

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    p_text = ft.Text(f'p = {p:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                p_text,
                x_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)