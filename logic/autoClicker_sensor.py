from storages import autoClicker_vars as vr
from threads import autoClicker_debugger as deb
from pynput import keyboard
from time import sleep

deb.testModePrint('sen_globalThread_work')


def thread_sen_run():

    deb.testModePrint('sen_Thread_work')

    def on_press_Return():
        vr.pressed_Return = True

    def on_press_J():
        vr.pressed_J = True

    def on_press_K():
        vr.pressed_K = True

    def on_press_Space():
        vr.pressed_Space = True


    listener = keyboard.GlobalHotKeys({
        'u+i': on_press_Return,
        'j': on_press_J,
        'k': on_press_K,
        ' ' : on_press_Space
    })
    listener.start()

    while True:
        sleep(0.5)
        if vr.stop_all:
            listener.stop()

            deb.testModePrint('sen_Thread_break')
            break
