import flet as ft

def main(page: ft.Page):

    x = 2
    y = 1
    result_a = (not (x * y < 0)) and (y > x)

    x = 2
    y = -2
    result_b = (x >= 2) or (y ** 2 != 5)

    result_a_text = ft.Text(f"Результат а: {result_a}", size=20)
    result_b_text = ft.Text(f"Результат б: {result_b}", size=20)

    page.add(result_a_text, result_b_text)

ft.app(target=main)