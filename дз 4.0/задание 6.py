import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №6"

    m = 2
    x = 1.1

    a = np.sqrt(np.abs(x))
    b = x**4 + m**2
    y = np.sin(a + np.tan(b)**3)**2

    a_text = ft.Text(f'a = {a:.2f}', size=20)
    b_text = ft.Text(f'b = {b:.2f}', size=20)
    y_text = ft.Text(f'y = {y:.2f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                a_text,
                b_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)