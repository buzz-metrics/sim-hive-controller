import math
import time


class Signals:
    def sin(self, now, t0):
        return math.sin(2 * math.pi * (now - t0) / 10)

    def square(self, now, t0):
        return 1 if (now - t0) % 10 < 5 else 0


class Signal_Generator(Signals):
    def __init__(self, fn):
        self.fn = fn
        self.t0 = time.time()

        allowed_signals = [fn for fn in dir(Signals) if not fn.startswith("__")]
        if fn not in allowed_signals:
            raise ValueError(
                f"Signal not allowed. Allowed signals are {allowed_signals}"
            )

        self.signal = getattr(Signals, fn)

    def get(self, now, t0):
        return self.signal(self, now, t0)

    def curr(self):
        return self.signal(self, time.time(), self.t0)


if __name__ == "__main__":
    sg = Signal_Generator("square")
    while True:
        print(sg.curr())
        time.sleep(1)
