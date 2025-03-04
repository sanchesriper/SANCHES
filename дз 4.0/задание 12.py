import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №12"
    
    q = 2
    b = 1.8
    
    t = b**3 + np.exp(np.sqrt(y))
    x = t**3 + b**2  
    y = np.arctan(np.abs(x))**2

    t_text = ft.Text(f't = {t:.4f}', size=20)
    x_text = ft.Text(f'x = {x:.4f}', size=20)
    y_text = ft.Text(f'y = {y:.4f}', size=20)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                t_text,
                x_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)