import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №19"
    
    x = 4
    a = 3.7
    
    p = x**2 - np.sqrt(abs(x))
    t = x**2 + a**2
    y = x * p**2 + t**5

    y_text = ft.Text(f'y = {y:.4f}', size=20)
    p_text = ft.Text(f'p = {p:.4f}', size=20)
    t_text = ft.Text(f't = {t:.4f}', size=20)
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                p_text,
                t_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)