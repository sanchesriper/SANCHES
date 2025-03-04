import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №9"

    k = 1
    m = 1.8

    c = np.cos(m)**2 + k**2
    x = np.exp(m * k)
    y = 3 * np.sqrt(x**2 + c**2)

    c_text = ft.Text(f'c = {c:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)
    y_text = ft.Text(f'y = {y:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                c_text,
                x_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)