from pubsub import pub

event_creation_name = ''  #ToDo
event_name = '1'  #ToDo


class IntEmitOver(int):
    def __new__(cls, value: int):
        pub.sendMessage(self.event_creation_name, f"IntEmitOver: создают со значением {value}")
        return super().__new__(cls, value)

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)

        if name in {
            "__add__", "__sub__", "__mul__", "__floordiv__",
            "__truediv__", "__mod__", "__pow__", "__and__",
            "__or__", "__xor__", "__lshift__", "__rshift__"
        }:
            def wrapper(other):
                old_value = int(self)
                new_value = attr(other)
                if isinstance(new_value, int) and not isinstance(new_value, IntEmitOver):
                    new_value = IntEmitOver(new_value)
                pub.sendMessage(self.event_name, f"IntEmitOver: меняют значение {old_value, new_value} пересозданием")
                return new_value

            return wrapper

        return attr