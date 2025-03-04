import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №1"

    x = 3.5
    b = 0.4

    y = np.exp(2*x) + np.exp(9.7)
    a = np.log10(x)
    с = np.power(a, 2) + np.sqrt(b * x)

    y_text = ft.Text(f'y = {y:.2f}', size=20)
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    c_text = ft.Text(f'c = {с:.2f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft. Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                a_text,
                c_text,
            ],
            spacing=20,
        )
    )        

ft.app(target=main)