import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №21"

    x = 1.4
    p = 1.6

    b = x**2 + np.log(p)
    a = np.sin(x**2 + b**2)
    y = np.log(a) / (np.log(b)**3) if b > 0 else float('inf')

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