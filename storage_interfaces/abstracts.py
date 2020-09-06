from storage_interfaces._compat import with_metaclass  # pylint: disable=no-name-in-module
from abc import ABCMeta

SG_TYPE = 1
FILE_TYPE = 2
PATH_TYPE = 3
NFS_TYPE = 4
NVME_TYPE = 5


class EndPoint(with_metaclass(ABCMeta)):
    def get_host(self):
        raise NotImplementedError()

    def get_identifier(self):
        raise NotImplementedError()

    def get_type(self):
        raise NotImplementedError()

    def register_to_before_phaseout(self, callback):
        raise NotImplementedError()

    def register_to_after_phasein(self, callback):
        raise NotImplementedError()
