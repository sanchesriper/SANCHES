import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №15"
    
    a = 5.5
    p = 4

    x = np.exp(b)
    y = np.cos(x) ** 3 + abs(a)
    b = abs(a) + np.sqrt(a + p ** 2)

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)
    b_text = ft.Text(f'b = {b:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                x_text,
                b_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)