import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №18"
    
    x = 8
    b = 9.5
    
    a = np.sqrt(abs(x)) + np.exp(np.sqrt(b))
    c = np.log10(a) + b**2
    y = a**3 / np.cos(c)
    
    y_text = ft.Text(f'y = {y:.4f}', size=20)
    a_text = ft.Text(f'a = {a:.4f}', size=20)
    c_text = ft.Text(f'c = {c:.4f}', size=20)
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                y_text,
                a_text,
                c_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)