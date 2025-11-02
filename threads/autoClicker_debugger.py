from time import sleep
import tkinter as tk
from tkinter import ttk
import threading
from datetime import datetime
from storages import autoClicker_vars as vr


def runer():
    thread = threading.Thread(target=thread_deb_main_run())
    thread.start()


def on_btn3_prest():
    vr.stop_all = True


def testModePrint(message):
    if vr.testMode:
        print(f"{datetime.now().time()} ▶ {message}")

def change_should_i_work_with_special_priorities():
    vr.should_i_work_with_special_priorities = not vr.should_i_work_with_special_priorities



#❗️
debugger_interval = 2
#❗️




def thread_deb_main_run():

    vr.set_item_from_dictionary(vr.ThreadsNames.thread_deb_main, actual__state = True)

    def run():
        vr.set_item_from_dictionary(vr.ThreadsNames.thread_deb_debHellper, actual__state=True)
        thread = threading.Thread(target=debhellper)
        thread.start()

    def debhellper():

        iteration_counter = 0

        while True:
            sleep(0.5)

            if  vr.should_i_work_with_special_priorities:
                btn1.config(bg='#4ff774')
                l2.config(bg='#00ff1a')

            else:
                btn1.config(bg='#fc3a3a')
                l2.config(bg='#f00')

            table.delete(*table.get_children())
            for t in vr.ThreadsNames:
                current_tag = 2
                values = vr.get_item_from_dictionary(t)
                a = values[0]
                b = values[1]
                c = values[2]

                if not a:
                    current_tag = 2
                else:
                    current_tag = 1

                table.insert("", tk.END, text=t.name, values=(t.name, a, b, c), tag=current_tag)

            l1.config(text=f"wait_time----------{vr.wait_time}")

            l2.config(text=f"should_i_work_with_special_priorities----------{vr.should_i_work_with_special_priorities}")

            l3.config(text=f"stop_all----------{vr.stop_all}")

            l4.config(text=f"first_click_position_x----------_{vr.first_click_position_x}")
            l5.config(text=f"first_click_position_y----------_{vr.first_click_position_y}")

            l6.config(text=f"second_click_position_x----------_{vr.second_click_position_x}")
            l7.config(text=f"second_click_position_y----------_{vr.second_click_position_y}")

            if iteration_counter == debugger_interval:

                print('-----------------------------------------------------------------------------------------------')

                testModePrint(f"wait_time----------{vr.wait_time}")

                testModePrint(f"should_i_work_with_special_priorities----------{vr.should_i_work_with_special_priorities}")

                testModePrint(f"stop_all----------{vr.stop_all}")

                print('-----------------------------------------------------------------------------------------------')

                iteration_counter = 0

            if vr.stop_thread(vr.ThreadsNames.thread_deb_debHellper):
                break
            iteration_counter += 0.5


    run()

    testModeWindow = tk.Tk()
    testModeWindow.title("TastModeWindow")

    btn1 = tk.Button(testModeWindow, text="Should work with special priorities",command=change_should_i_work_with_special_priorities)
    btn1.pack(expand=True, fill=tk.BOTH)

    btn2 = tk.Button(testModeWindow, text="Stop thread with highest priority",command=vr.stop_thread_with_highest_priority)
    btn2.pack(expand=True, fill=tk.BOTH)
    btn2.config(bg='#6b6b6b')

    btn3 = tk.Button(testModeWindow, text="Stop all",command=on_btn3_prest)
    btn3.pack(expand=True, fill=tk.BOTH)
    btn3.config(bg='#60021a')


    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=20)

    table = ttk.Treeview(testModeWindow, height = len(vr.ThreadsNames))

    table.tag_configure('1', background='#068c23')
    table.tag_configure('2', background='#8c0606')

    table['columns'] = ('Thread_Name', '_state', 'Shutdown_command', 'Thread_priority')

    table.column('#0', width = 0, stretch = tk.NO)
    table.column('Thread_Name', anchor = 'w', width = 200)
    table.column('_state', anchor = 'w', width = 150)
    table.column('Shutdown_command', anchor= 'w', width=150)
    table.column('Thread_priority', anchor = 'w', width=150)

    table.heading('#0', text='', anchor = 'w')
    table.heading('Thread_Name', text='Thread_Name', anchor = 'w')
    table.heading('_state', text='_state', anchor = 'w')
    table.heading('Shutdown_command', text='Shutdown_command', anchor = 'w')
    table.heading('Thread_priority', text='Thread_priority', anchor = 'w')

    for t in vr.ThreadsNames:
        table.insert("", tk.END, text=t.name, values=(t.name, "Value 1", "Value 2", "Value 3"))

    table.pack(expand=True, fill=tk.BOTH)

    l1 = tk.Label(testModeWindow, text=f"wait_time----------{1}")
    l1.pack(expand=True, fill=tk.BOTH)

    l2 = tk.Label(testModeWindow, text=f"should_i_work_with_special_priorities----------{1}")
    l2.pack(expand=True, fill=tk.BOTH)

    l3 = tk.Label(testModeWindow, text=f"stop_all----------{1}")
    l3.pack(expand=True, fill=tk.BOTH)

    #------------------------------------------------

    l4 = tk.Label(testModeWindow, text=f"first_click_position_x----------{1}")
    l4.pack(expand=True, fill=tk.BOTH)

    l5 = tk.Label(testModeWindow, text=f"first_click_position_y----------{1}")
    l5.pack(expand=True, fill=tk.BOTH)

    #------------------------------------------------

    l6 = tk.Label(testModeWindow, text=f"second_click_position_x----------{1}")
    l6.pack(expand=True, fill=tk.BOTH)

    l7 = tk.Label(testModeWindow, text=f"second_click_position_y----------{1}")
    l7.pack(expand=True, fill=tk.BOTH)

    testModeWindow.mainloop()


    print('------------')

    # while True:
    #     sleep(0.5)
    #     vr.send_shutdown_command_to_thread(vr.Threads_Names.thread_deb_debHellper)
    #     if vr.get_item_from_dictionary(vr.Threads_Names.thread_deb_debHellper)[0]  == False:
    #         break


    vr.stop_thread(vr.ThreadsNames.thread_deb_main)


runer()