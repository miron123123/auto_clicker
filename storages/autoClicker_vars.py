from thread_classes.ThreadsNames import *
from thread_classes.ThreadStatus import *
from threads.thredBuildear import *
print('vars_work_global')



threads = {}


#-----------------------------------------------------------------------------------------------------------------------
#region filles_threades_with_initial_values

threads[ThreadsNames.thread_main] = ThreadStatus(a = False, b = False, c = -1)

threads[ThreadsNames.thread_watcher] = ThreadStatus(a = False, b = False, c = -2)

threads[ThreadsNames.thread_logger] = ThreadStatus(a = False, b = False, c = -3)

threads[ThreadsNames.thread_deb_main] = ThreadStatus(a = False, b = False, c = -4)

threads[ThreadsNames.thread_deb_debHellper] = ThreadStatus(a = False, b = False, c = -5)

threads[ThreadsNames.thread_sen] = ThreadStatus(a = False, b = False, c = 1)

threads[ThreadsNames.thread_bg_main] = ThreadStatus(a = False, b = False, c = 2)

threads[ThreadsNames.thread_bg_autoClicker] = ThreadStatus(a = False, b = False, c = 3)

threads[ThreadsNames.thread_fg_main] = ThreadStatus(a = False, b = False, c = 4)

threads[ThreadsNames.thread_fg_sensorWindow] = ThreadStatus(a = False, b = False, c = 5)
#endregion
#-----------------------------------------------------------------------------------------------------------------------
#region is__state

get_time_from_Entry = False #TODO: лог?

wait_time: float = 0.1 #TODO: лог?

stop_all = False #TODO: лог

bg_is_clicking = False

testMode = True #TODO: лог

should_i_work_with_special_priorities = True #TODO: лог
#endregion
#-----------------------------------------------------------------------------------------------------------------------
#region pressedButton

pressed_Return = False #TODO: лог

pressed_J = False #TODO: лог

pressed_K = False #TODO: лог

pressed_Space = False #TODO: лог

#endregion
#-----------------------------------------------------------------------------------------------------------------------
#region BG
# TODO: лог?

autoClicking_destroy = False

first_click_position_x = 0
first_click_position_y = 0

second_click_position_x = 0
second_click_position_y = 0

#endregion

print(wait_time)

