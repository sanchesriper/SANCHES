import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №3"

    x = 2.1
    p = 1

    a = np.exp(np.sqrt(np.abs(x))) 
    b = np.sin(p**2) + x**3
    y = a**3 / b**2  

    y_text = ft.Text(f'y = {y:.2f}', size=20)
    a_text = ft.Text(f'a = {a:.2f}', size=20)
    b_text = ft.Text(f'b = {b:.2f}', size=20)

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