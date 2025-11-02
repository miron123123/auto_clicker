import enum



class ThreadsNames(enum.Enum):

    thread_main = "THREAD_MAIN"
    thread_deb_main = "THREAD_DEB_MAIN"
    thread_deb_debHellper = "THREAD_DEB_DEBhELLPER"
    thread_sen = "THREAD_SEN_DESTROY"
    thread_logger = "THREAD_LOGGER"
    thread_watcher = "THREAD_WATCHER"
    thread_bg_main = "THREAD_BG_MAIN"
    thread_bg_autoClicker = "THREAD_DG_AUTOcLICKER"
    thread_fg_main = "THREAD_FG_MAIN"
    thread_fg_sensorWindow = "THREAD_FG_SENSORwindow"