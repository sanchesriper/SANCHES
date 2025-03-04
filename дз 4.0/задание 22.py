import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №22"

    m = 5.7
    p = 4

    t = np.sin(m)**3
    x = p**2 + t
    y = np.log10(abs(x + t))**4

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)
    t_text = ft.Text(f't = {t:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                x_text,
                t_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)