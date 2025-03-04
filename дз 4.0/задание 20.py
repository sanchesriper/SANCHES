import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №20"

    x = 1.4
    p = 1.6

    a = np.log(abs(x))
    b = x**4 + np.log10(p**3)
    y = np.sin(a * x)**3 + np.sqrt(b) * np.cos(x**2)

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