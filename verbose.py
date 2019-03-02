import logging

logger = logging.getLogger(__name__)


class Verbose:
    def __init__(self, val, levels=1):
        if levels == 1:
            self.v = val
        else:
            self.v = type(self)(val, levels-1)

        logger.info(f"Verbosified value {self.v}")

    def __getattribute__(self, *_, **__):
        val = object.__getattribute__(self, '_val')

        logger.info(f"Returned value {val}")

        return val

    def __setattr__(self, _, val):
        object.__setattr__(self, '_val', val)

        logger.info(f"Set the value to {val}")

    __getitem__ = __getattribute__
    __call__ = __getattribute__

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.v)})"

    def __len__(self):
        logger.info("Calculating length")

        if isinstance(self.v, type(self)):
            return len(self.v) + 1
        return 1
