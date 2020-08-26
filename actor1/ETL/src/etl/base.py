from abc import ABCMeta, abstractmethod


def try_or(fn, default):
    try:
        return fn()
    except Exception:
        return default


class BaseCreate(object):
    """Base class for entry creation. It should be imported when
    you are creating entries through etl script."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def perform(self):
        pass


class BaseUpdate(object):
    """Base class for entry updation. It should be used when updating
     existing data as well."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def perform_update(self):
        pass
