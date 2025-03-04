import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №17"
    
    x = 0.9
    t = 2

    b = np.log10(abs(x))**2
    a = t * x + abs(np.sqrt(b))
    y = np.cos(a + b**3)**3

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