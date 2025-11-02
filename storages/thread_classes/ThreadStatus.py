
from pubsub import pub
import traceback


class ThreadStatus(object):
    def __init__(self, a: bool, b: bool, c: int):
        self._state = a
        self._should_stop = b
        self._order_number = c

        # -----------------------------------------------------------------------------------------------------------------------

        @property
        def state(self):
            pub.sendMessage(self.event_name, arg1='state', arg2='get', arg3=self.state, arg4=0,
                            arg5=traceback.extract_stack(None, 2))
            return self.state

        @state.setter
        def state(self, new_value):
            pub.sendMessage(self.event_name, arg1='state', arg2='set', arg3=self.state, arg4=new_value,
                            arg5=traceback.extract_stack(None, 2))
            self.state = new_value

        # -----------------------------------------------------------------------------------------------------------------------

        @property
        def should_stop(self):
            pub.sendMessage(self.event_name, arg1='should_stop', arg2='get', arg3=self._should_stop, arg4=0,
                            arg5=traceback.extract_stack(None, 2))
            return self._should_stop

        @should_stop.setter
        def should_stop(self, new_value):
            pub.sendMessage(self.event_name, arg1='should_stop', arg2='set', arg3=self._should_stop, arg4=new_value,
                            arg5=traceback.extract_stack(None, 2))
            self._should_stop = new_value

        # -----------------------------------------------------------------------------------------------------------------------

        @property
        def order_number(self):
            pub.sendMessage(self.event_name, arg1='order_number', arg2='get', arg3=self._order_number, arg4=0,
                            arg5=traceback.extract_stack(None, 2))
            return self._order_number

        @order_number.setter
        def order_number(self, new_value):
            pub.sendMessage(self.event_name, arg1='order_number', arg2='set', arg3=self._should_stop, arg4=new_value,
                            arg5=traceback.extract_stack(None, 2))
            self._order_number = new_value

    # -----------------------------------------------------------------------------------------------------------------------
