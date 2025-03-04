import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №2"

    x = 1.3
    b = 0.4

    a = np.log(np.abs(x))
    y = x * (a ** 3) + b ** 2
    b = np.exp(2 * x) + a * x

    y_text = ft.Text(f'y = {y:.2f}', size=20)
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    b_text = ft.Text(f'b = {b:.2f}', size=20)

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