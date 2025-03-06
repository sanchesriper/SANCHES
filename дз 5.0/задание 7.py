import flet as ft
import math

def main(page: ft.Page):

    x = 1.5

    result_y1 = 2 * math.tan(x)
    result_y2 = 3 / (x - 1)

    result_text_a = ft.Text(f"Результат у1: {result_y1}", size=20)
    result_text_b = ft.Text(f"Результат у2: {result_y2}", size=20)

    page.add(result_text_a, result_text_b)

ft.app(target=main)