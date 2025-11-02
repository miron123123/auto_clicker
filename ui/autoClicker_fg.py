import tkinter as tk
from tkinter import messagebox
from storages import autoClicker_vars as vr
from threads import autoClicker_debugger as deb
from time import sleep
import threading

deb.testModePrint('fg_globalThread_work')

#region all


def thread_fg_main_run():
    deb.testModePrint('fg_Thread_work ➖')
#region def 1

    _should_stop_fg = False

    def user_clicked_on_button():
        vr.get_time_from_Entry = True

    def all_naemes_from_dictioary(a):
        b = False
        if len(list(set(list(a.values())))) == 1 and list(set(list(a.values()))) == [True]:

            b = True
        return b

    def window_destroy():
        global _should_stop_fg
        vr.stop_all = True
        while True:
            sleep(0.5)
            if all_naemes_from_dictioary(vr.threads_destroy):
                sleep(1)  #ToDo сохранение в память вместо задержки
                _should_stop_fg = True

    def thread_fg_senserWindow_run():  #создаём отдельный поток для функции senserWindow
        thread = threading.Thread(target=senserWindow)
        thread.start()

    def label_bg_work_value(bg_is_clicking):
        if bg_is_clicking == False:
            label_bg_work.config(text='программа не кликает')
        else:
            label_bg_work.config(text='программа кликает')

    def messagebox_1_error():
        messagebox.showinfo('Ошибка', 'программа кликает (изменение невозможно)')

    def messagebox_2_error():
        messagebox.showinfo('Ошибка', 'в поле ввода некоректное значение')

#endregion

#--------------------------------------------------------------------------------------------------------


    def senserWindow():# функция считывающия значения с txt
        deb.testModePrint('fg_senserThread_work')

        while True:
            sleep(0.5)

            wait_time = txt.get()
            if len(wait_time) != 0 and vr.pressed_Return:
                vr.get_time_from_Entry = True
                vr.pressed_Return = False

            if vr.get_time_from_Entry:
                if not vr.bg_is_clicking:
                    try:
                        vr.wait_time = float(wait_time)
                        label_wait_time_value.config(text='текущяя задержка-{}'.format(vr.wait_time))
                    except ValueError:
                        messagebox_2_error()
                        sleep(0.1)
                else:
                    messagebox_1_error()
                vr.get_time_from_Entry = False
                txt.delete(0,'end')
            if vr.stop_all:
                vr.threads_destroy[vr.ThreadsNames.thread_fg_sensorWindow_destroy] = True
                deb.testModePrint('fg_senserThread_break')
                break
            label_bg_work_value(vr.bg_is_clicking)







    deb.testModePrint('fg_window_work')

    thread_fg_senserWindow_run()
    deb.testModePrint('main_senserThread_start')

    window = tk.Tk()
    window.title('Окно')
    window.geometry('750x750')

    label_bg_work = tk.Label(window, text='')
    label_bg_work.grid(column=0, row=0)

    label_wait_time_value = tk.Label(window, text='')
    label_wait_time_value.grid(column=0, row=1)

    txt = tk.Entry(window, width=10, )
    txt.grid(column=0, row=2)

    btn = tk.Button(window, text="Не нажимать!", bg="black", fg="red", command=user_clicked_on_button)
    btn.grid(column=2, row=2)

    window.protocol("WM_DELETE_WINDOW", window_destroy)
    window.mainloop()

    while True:
        sleep(0.5)
        if _should_stop_fg:
            deb.testModePrint('fg_Thread_break')
            break






#endregion