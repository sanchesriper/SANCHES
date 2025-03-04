import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Практическая работа №4"
    page.vertical_alignment = ft.MainAxisAlignment.START


    page.add(ft.Text("Список Заданий", size=30, weight="bold"))


    nav = ft.Row(controls=[
        ft.TextButton("Главная"),
        ft.TextButton("Задания"),
    ])
    page.add(nav)

    for i in range(1, 16):
        task_card = ft.Card(
            content=ft.Column(
                controls=[
                    ft.Text(f"Задание {i}", size=20, weight="bold"),
                    ft.Text(f"Краткое описание задания {i}."),
                    ft.Row(controls=[
                        ft.Text(f"Статус: {'В процессе' if i % 3 == 0 else 'Не начато' if i % 3 == 1 else 'Выполнено'}"),
                        ft.TextButton("Подробнее", on_click=lambda e: page.add(ft.Text(f"Детали задания {i}..."))),
                    ])
                ]
            ),
            elevation=2,
        )
        page.add(task_card)

ft.app(target=main)