from storages import autoClicker_vars as vr
from tkinter import messagebox
import tkinter as tk
from time import sleep


def massagebox_1():
    messagebox.showinfo('Ошибка', 'Сan not work with spacial priorities')

def  notify_messagebox_1():
    if vr.testMode:
        answer = tk.messagebox.askokcancel(title='error warning', message='Program can crash!!! Do you want to continue?')
        print(answer)
        if answer:
            vr.stop_all = True
        return answer


# def stop_thread_with_highest_priority():
#
#     key_thread_by_priority = vr.thread_kay_with_max_and_min_priority()
#
#     print(key_thread_by_priority[3],key_thread_by_priority[2])
#
#     if key_thread_by_priority[3] < 0 and  not key_thread_by_priority[2] > 0 and vr.should_i_work_with_special_priorities:
#         if notify_messagebox_1():
#             vr.stop_thread_with_highest_priority()
#     else:
#         vr.stop_thread_with_highest_priority()



def stop_thread(item_name):  # импорт в поток который надо выключить с проверкой через if vr.stop_thread:
    thread_values = get_item_from_dictionary(item_name)
    shutdown_command = False
    if thread_values[1] == True:
        set_item_from_dictionary(item_name, actual___state = False)
        shutdown_command = True
    return shutdown_command

def get_item_from_dictionary(item_name):
    _state: bool = vr.threads[item_name]._state
    _should_stop: bool = vr.threads[item_name]._should_stop
    _order_number: int = vr.threads[item_name]._order_number
    return _state, _should_stop, _order_number

def set_item_from_dictionary(item_name, actual__state = None, actual__should_stop = None, actual__order_number = None):
    current_values = get_item_from_dictionary(item_name)

    if actual__state == None:
        vr.threads[item_name]._state = current_values[0]
    elif actual__state != None:
        vr.threads[item_name]._state = actual__state

    if actual__should_stop == None:
        vr.threads[item_name]._should_stop = current_values[1]
    elif actual__should_stop != None:
        vr.threads[item_name]._should_stop = actual__should_stop

    if actual__order_number == None:
        vr.threads[item_name]._order_number = current_values[2]
    elif actual__order_number != None:
        vr.threads[item_name]._order_number = actual__order_number

#-----------------------------------------------------------------------------------------------------------------------

def send_shutdown_command_to_thread(item_name):
    set_item_from_dictionary(item_name, actual__should_stop = True, actual__order_number = 0)

def thread_kay_with_max_and_min_priority():
    key_max_priority = max(vr.threads, key=lambda i: vr.threads[i]._order_number)
    highest_priority = get_item_from_dictionary(key_max_priority)

    key_min_priority = min(vr.threads, key=lambda i: vr.threads[i]._order_number)
    minimal_priority = get_item_from_dictionary(key_min_priority)

    return key_max_priority, key_min_priority, highest_priority[2], minimal_priority[2]

def stop_thread_with_highest_priority():

    key_thread_that_stopping = False

    key_priority = thread_kay_with_max_and_min_priority()

    if vr.threads[key_priority[0]]._order_number > 0:
        send_shutdown_command_to_thread(key_priority[0])
        key_thread_that_stopping = key_priority[0]

    elif vr.threads[key_priority[1]]._order_number < 0 and vr.should_i_work_with_special_priorities:
        if not vr.stop_all:
            if notify_messagebox_1():
                send_shutdown_command_to_thread(key_priority[1])
                key_thread_that_stopping = key_priority[1]
        else:
            send_shutdown_command_to_thread(key_priority[1])
            key_thread_that_stopping = key_priority[1]

    elif vr.threads[key_priority[1]]._order_number < 0 and not vr.should_i_work_with_special_priorities:
        print('wait')
        if vr.testMode:
            massagebox_1()
    else:
        raise Exception('неправильные приарететы')

    c = 0

    if key_thread_that_stopping != False:
        while get_item_from_dictionary(key_thread_that_stopping)[0] != False:
            sleep(0.5)

            if c > 6.5:
                print(f"Time's up for shutdown----------{key_thread_that_stopping}")
                break

            c += 0.5
