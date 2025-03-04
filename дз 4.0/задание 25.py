import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №25"

    a = 2
    p = 2.6

    t = p**3 + a**3
    x = np.exp(np.sqrt(p + a))
    y = x**3 / t**2

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)
    t_text = ft.Text(f't = {t:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                x_text,
                t_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)