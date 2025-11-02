from time import sleep
import threading
from ui import autoClicker_fg as fg
from logic import autoClicker_sensor as sen, autoClicker_bg as bg
from storages import autoClicker_vars as vr
from threads import autoClicker_debugger as deb
#from logging import autoClicker_watcher as watch

deb.testModePrint('main_globalThread_work')


def run():

    threads_lock = threading.Lock()
    deb_thread = threading.Thread(target=deb.thread_deb_main_run)
    sensor_thread = threading.Thread(target=sen.thread_sen_run)
    bg_thread = threading.Thread(target=bg.thread_bg_main_run)
    fg_thread = threading.Thread(target=fg.thread_fg_main_run)


    fg_thread.start()
    deb.testModePrint('main_fgThread_start')
    sensor_thread.start()
    deb.testModePrint('main_senThread_start')
    bg_thread.start()
    deb.testModePrint('main_bgThread_start')
    deb_thread.start()
    deb.testModePrint('main_debThread_start')




run()
deb.testModePrint('main_allThread_start')

while True:
    sleep(0.5)
    if vr.stop_all:
        vr.stop_thread_with_highest_priority()



#1)завершить потоки
#2)в bg закончить с senser_combinations_buttones (строки 63 - 66)
#3)в bg создать условия работы кликера
#4)отрисовка интерфейса в autoClicker_fg
#5)сохранения ностроек на диск

