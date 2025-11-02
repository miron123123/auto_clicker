print('bg_work_global')
from time import sleep
from pynput import mouse
from storages import autoClicker_vars as vr
from threads import autoClicker_debugger as deb
import threading

deb.testModePrint('bg_globalThread_work')

mouse1 = mouse.Controller()
Button1 = mouse.Button

def thread_bg_main_run():

    deb.testModePrint('bg_Thread_work')

    pressed_Space = False

    def thread_bg_autoClicker_run():
        thread = threading.Thread(target=autoClicking)
        thread.start()

    def autoClicking():
        while True:
            sleep(vr.wait_time)

            mouse1.position = (vr.first_click_position_x, vr.first_click_position_y)
            mouse1.press(Button1.left)
            sleep(0.1)
            mouse1.release(Button1.left)
            print('1')

            mouse1.position = (vr.second_click_position_x, vr.second_click_position_y)
            mouse1.press(Button1.left)
            sleep(0.1)
            mouse1.release(Button1.left)
            print('2')

            if vr.stop_all or vr.autoClicking_destroy:
                vr.threads_destroy[vr.ThreadsNames.thread_bg_autoClicker_destroy] = True
                deb.testModePrint('bg_clickeringThread_break')
                break


    while True:
        sleep(0.5)

        #region pressedButton

        if vr.pressed_K:
            (vr.first_click_position_x, vr.first_click_position_y) = mouse1.position
            vr.pressed_K = False

        if vr.pressed_J:
            (vr.second_click_position_x, vr.second_click_position_y) = mouse1.position
            vr.pressed_J = False

        if vr.pressed_Space:
            pressed_Space = not pressed_Space
            vr.pressed_Space = False

        #endregion

        if vr.stop_all:

            deb.testModePrint('bg_Thread_break')
            break

        if not pressed_Space:
            vr.threads_destroy[vr.ThreadsNames.thread_bg_autoClicker_destroy] = True
            vr.autoClicking_destroy = True
            vr.bg_is_clicking = False




        if pressed_Space:
            vr.threads_destroy[vr.ThreadsNames.thread_bg_autoClicker_destroy] = False
            deb.testModePrint('bg_clickerThread_start')
            vr.autoClicking_destroy = False
            vr.bg_is_clicking = True
            thread_bg_autoClicker_run()
