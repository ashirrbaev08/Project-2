import flet as ft
from datetime import datetime


def main(page:ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.DARK

    text_hello = ft.Text("Hello world!",text_align=ft.TextAlign.CENTER)

    lovely_names = []
    lovely_text = ft.Text(value="Добавить в изобранное:")

    greeting_history = []
    history_text = ft.Text(value="История приветсвий:")



    def on_button_click(_):
        name = name_input.value

        if name:
            now = datetime.now()
            greeting_history.append((name, now))
            now2 = now.strftime("%Y:%m:%d - %H:%M:%S")
            text_hello.value = f"Hello {name} \nВремя ввода: {now}"
            name_input.value = None
            text_hello.color = None

            history_text.value = "История приветствий:\n" + "\n".join(
                f"{name} — {time.strftime('%H:%M:%S')}" for name, time in greeting_history)


        else:
            text_hello.value = "Введите корректное имя!"
            text_hello.color = ft.Colors.RED


    elevated_button = ft.ElevatedButton("send",icon=ft.Icons.SEND,
                            color=ft.Colors.YELLOW,icon_color=ft.Colors.ORANGE,on_click=on_button_click)


    elevated_button.icon = ft.Icons.ADD


    def clear_button(_):
        if greeting_history:
            greeting_history.pop()


            history_text.value = "История приветсвий:\n" + "\n".join(
                f"{name} — {time.strftime('%H:%M:%S')}" for name, time in greeting_history)

        else:

            history_text.value = "История пуста:\n" + "\n".join(
                f"{name} — {time.strftime('%H:%M:%S')}" for name, time in greeting_history)

        



    clear_button = ft.ElevatedButton("Удалить последнее",on_click=clear_button)



    def add_favorites(_):
        if greeting_history:
            last_name = greeting_history[-1][0]

        if last_name not in lovely_names:
            lovely_names.append(last_name)

        lovely_text.value = "Добавить в изобранное:\n" + "\n".join(lovely_names)


    lovely_button = ft.IconButton(icon=ft.Icons.STAR,on_click=add_favorites)




    name_input = ft.TextField(label="Введите что нибудь",on_submit=on_button_click)



    def theme_change(_):

        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT

        else:
            page.theme_mode = ft.ThemeMode.DARK


    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_5_OUTLINED,on_click=theme_change)



    def clear_history(_):
        greeting_history.clear()
        print(greeting_history)
        history_text.value = "История приветсвий: "


    clear_all_button = ft.IconButton(icon=ft.Icons.DELETE,on_click=clear_history)


    def filter_morning(_):
        morning = [name for name, time in greeting_history if 6 <= time.hour < 12]
        history_text.value = "Утренние приветсвия:\n"+"\n".join(morning)
       

    def filter_evening(_):
        evening = [name for name, time in greeting_history if 18 <= time.hour <= 23]
        history_text.value = "Вечерние приветсвия:\n"+"\n".join(evening)
       
    def filter_day(_):
        day = [name for name, time in greeting_history if  12 <= time.hour < 18]
        history_text.value = "Дневные приветсвия:\n"+"\n".join(day)

    def filter_night(_):
        night = [name for name, time in greeting_history if 0 <= time.hour < 6]
        history_text.value = "Ночные приветсвия:\n"+"\n".join(night)



    morning_button = ft.ElevatedButton('Утренние', on_click=filter_morning)
    evening_button = ft.ElevatedButton('Вечерние', on_click=filter_evening)
    day_button = ft.ElevatedButton('Дневные', on_click=filter_day)
    night_button = ft.ElevatedButton('Ночные', on_click=filter_night)


    main_button = ft.Row([name_input,elevated_button,theme_button,clear_all_button,
                    lovely_button,morning_button,evening_button,clear_button,day_button,night_button]
                                ,alignment=ft.MainAxisAlignment.CENTER)

            

    page.add(text_hello,main_button,history_text,lovely_text)

    

ft.run(main)