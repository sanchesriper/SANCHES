import flet as ft

def main(page: ft.Page):

    A = True
    B = False
    C = False

    result_a = (A or (not A and B)) or C
    result_b = (not A) or (A and (B or C))
    result_c = (A or (B and not C)) and C

    result_a_text = ft.Text(f"Результат а: {result_a}", size=20)
    result_b_text = ft. Text(f"Результат 6: {result_b}", size=20)
    result_c_text = ft.Text(f"Результат в: {result_c}", size=20)


    page.add(result_a_text, result_b_text, result_c_text)

ft.app(target=main)