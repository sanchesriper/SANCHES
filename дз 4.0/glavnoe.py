import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа 4"
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    
    page.add(ft.Text("Список заданий", size=30, weight="bold"))
    
    
    nav = ft.Row(controls=[
        ft.TextButton(text="Главная"),
        ft.TextButton(text="Задания"),
    ])
    page.add(nav)
    
    
    def show_details(task_number):
        def inner_function(e):
            page.add(ft.Text(f"Детали задания {task_number}..."))
        return inner_function
    
    for i in range(1, 16):
        status = 'В процессе' if i % 3 == 0 else 'Не начато' if i % 3 == 1 else 'Выполнено'

        task_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"Задание {i}", size=20, weight="bold"),
                        ft.Text(f"Краткое описание задания {i}."),
                        ft.Row(
                            controls=[
                                ft.Text(f"Статус: {status}"),
                                ft.TextButton("Подробнее", on_click=show_details(i)),
                            ]
                        )
                    ],
                ),
                padding=10,
            ),
            elevation=2,
        )
        page.add(task_card)

ft.app(target=main)