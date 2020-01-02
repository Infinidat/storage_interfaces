from storage_interfaces._compat import with_metaclass  # pylint: disable=no-name-in-module
from storage_interfaces.abstracts import EndPoint
from abc import ABCMeta

class ScsiSystem(with_metaclass(ABCMeta)):

    def get_name(self):
        raise NotImplementedError()


class ScsiVolume(with_metaclass(ABCMeta)):

    def get_name(self):
        raise NotImplementedError()

    def get_system(self):
        raise NotImplementedError()

    def get_unique_key(self):
        raise NotImplementedError()


class LogicalUnit(with_metaclass(ABCMeta)):

    def get_volume(self):
        raise NotImplementedError()

    def get_system(self):
        raise NotImplementedError()

    def get_host(self):
        raise NotImplementedError()

    def get_hctl(self):
        raise NotImplementedError()

    get_identifier = get_hctl

    def get_type(self):
        raise NotImplementedError()

    def register_to_before_phaseout(self, callback):
        raise NotImplementedError()

    def register_to_after_phasein(self, callback):
        raise NotImplementedError()

EndPoint.register(LogicalUnit)
