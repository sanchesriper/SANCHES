import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №28"

    b = 2.19
    k = 1.7

    t = k**2 + np.sqrt(b)
    a = b + t**2 * np.exp(t)
    y = np.cos(a**3 + b)**4

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    a_text = ft.Text(f'a = {a:.4f}', size=20)
    t_text = ft.Text(f't = {t:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                a_text,
                t_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)