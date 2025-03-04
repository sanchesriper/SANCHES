import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №7"

    k = 8.2
    x = 5

    c = np.sqrt(np.abs(x))
    a = c**4 + k**3
    y = np.log10(a)**3 + np.cos(x)**3

    c_text = ft.Text(f'c = {c:.2f}', size=20)
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                c_text,
                a_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)