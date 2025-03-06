import flet as ft

def main(page: ft.Page):

    A = 9
    B = 10

    result_a = (A % 3 == 0) and (B % 5 == 0)

    result_a_text = ft.Text(f"Результат: {result_a}", size=20)

    page.add(result_a_text)

ft.app(target=main)