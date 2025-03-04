import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №13"
    
    x = 1.9
    a = -0.9
    
    w = x**2 * np.sqrt(np.abs(a + x))
    z = np.cos(a)**2 + w**2     
    y = a * z**7 + np.sin(w)**2
    
    w_text = ft.Text(f'w = {w:.4f}', size=20)
    z_text = ft.Text(f'z = {z:.4f}', size=20)
    y_text = ft.Text(f'y = {y:.4f}', size=20)
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Результаты вычислений", size=24, weight="bold"),
                w_text,
                z_text,
                y_text,
            ],
            spacing=20,
        )
    )

ft.app(target=main)