from typing import Union

from ._signal_generator import Signal_Generator


class PV:
    def __init__(
        self,
        name: str,
        v0: Union[int, float, str, Signal_Generator],
        getable: bool,
        setable: bool,
    ):
        self.name = name
        self.value = v0
        self.getable = getable
        self.setable = setable

    @staticmethod
    def is_getable(PV):
        return PV.getable

    @staticmethod
    def is_setable(PV):
        return PV.setable

    def curr(self):
        if isinstance(self.value, Signal_Generator):
            return self.value.curr()
        else:
            return self.value

    def set_value(self, value: float):
        if isinstance(self.value, Signal_Generator):
            raise ValueError("Cannot set value of signal generator")
        else:
            self.value = value
