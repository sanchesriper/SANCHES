import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №23"

    b = 0.3
    x = 5.2

    t = x * b**2 + np.sqrt(x)
    a = np.log10(abs(t * x + b**2))
    y = (np.log(a + b))**2 + (a**2) / (a + t)

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