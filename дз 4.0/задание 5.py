import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №5"

    t = 4.1
    p = 3

    k = np.sqrt(p * t)
    x = p * t**2 + np.sqrt(k)
    y = np.tan(x**2)**3 + k * t

    k_text = ft.Text(f'k = {k:.2f}', size=20)
    x_text = ft.Text(f'x = {x:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                k_text,
                x_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)