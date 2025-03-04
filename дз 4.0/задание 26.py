import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №26"

    b = 8.1
    t = 2

    a = np.sqrt(b + t**2)
    x = np.cos(b)**2 + np.sin(a)**2
    y = x**2 + np.sqrt(np.abs(x))**3

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