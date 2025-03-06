import flet as ft

def main(page: ft.Page):

    X = False
    Y = True
    Z = False

    result_x = X and not (Z or Y) or not Z
    result_y = not X or X and (Y or Z)
    result_z = (X or Y and not Z) and Z

    result_x_text = ft.Text(f"Результат икс: {result_x}", size=20)
    result_y_text = ft. Text(f"Результат у: {result_y}", size=20)
    result_z_text = ft.Text(f"Результат з: {result_z}", size=20)


    page.add(result_x_text, result_y_text, result_z_text)

ft.app(target=main)