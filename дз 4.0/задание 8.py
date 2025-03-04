import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №8"

    b = 2.2
    c = 3.7

    a = np.sin(b)
    x = a + (b + c)**3 
    y = 7 * np.exp(np.sqrt(np.abs(x))) + np.cos(x)**4

    a_text = ft.Text(f'a = {a:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)
    y_text = ft.Text(f'y = {y:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                a_text,
                x_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)