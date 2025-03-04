import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №14"

    b = 6
    k = 3.4

    t = b**2 + k**3
    a = np.sqrt(b + t) 
    y = np.sin(a**2 + b**2)**4

    t_text = ft.Text(f't = {t:.4f}', size=20)
    a_text = ft.Text(f'a = {a:.4f}', size=20)
    y_text = ft.Text(f'y = {y:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                t_text,
                a_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)