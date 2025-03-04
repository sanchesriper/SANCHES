import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №10"

    x = 2.8
    b = 1.3

    a = b**3 + np.log(np.abs(b))
    c = a**2 + np.sqrt(b)
    y = np.exp(x) + 5.8**c

    a_text = ft.Text(f'a = {a:.4f}', size=20)
    c_text = ft.Text(f'c = {c:.4f}', size=20)
    y_text = ft.Text(f'y = {y:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                a_text,
                c_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)