import flet as ft

def main(page: ft.Page):

    x = False
    y = False
    z = True

    result_x = x or y and not z 
    result_y = not x and not y  
    result_z = not (x and z) or y 

    result_x_text = ft.Text(f"Результат икс: {result_x}", size=20)
    result_y_text = ft. Text(f"Результат у: {result_y}", size=20)
    result_z_text = ft.Text(f"Результат з: {result_z}", size=20)


    page.add(result_x_text, result_y_text, result_z_text)

ft.app(target=main)