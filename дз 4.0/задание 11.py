import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №11"
    
    x = 2
    b = 7
    
    a = (b + x)**3
    c = np.log10(np.abs(b))
    y = c**2 + np.sqrt(np.abs(a))
    
    a_text = ft.Text(f'a = {a:.4f}', size=20)
    c_text = ft.Text(f'c = {c:.4f}', size=20)
    y_text = ft.Text(f'y = {y:.4f}', size=20)
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                a_text,
                c_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)