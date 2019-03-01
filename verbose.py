import logging

logger = logging.getLogger(__name__)


class Verbose:
    def __init__(self, val, levels=1):
        if levels == 1:
            self._val = val
        else:
            self._val = self.__class__(val, levels-1)

        logger.info(f"Verbosified value {self._val}")

    def get_value(self, *args_, **kwargs_):
        """
        Gets the value
        :return: the value
        """

        del args_, kwargs_

        val = object.__getattribute__(self, '_val')

        logger.info(f"Returned value {val}")

        return val

    __getitem__ = get_value
    __getattr__ = get_value
    __call__ = get_value

    def __repr__(self):
        return f"{type(self).__name__}({repr(self.get_value())})"

    def __len__(self):
        logger.info("Calculating length")

        if isinstance(self.get_value(), type(self)):
            return len(self.get_value()) + 1
        return 1
