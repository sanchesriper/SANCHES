import flet as ft

def main(page: ft.Page):

    A = 6

    result_a = (A % 2 == 0) or (A % 3 == 0)

    result_a_text = ft.Text(f"Результат: {result_a}", size=20)

    page.add(result_a_text)

ft.app(target=main)