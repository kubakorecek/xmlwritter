"""
    This module is to provide setting the new config file.
"""
from abc import ABCMeta, abstractmethod


class CnfWASettInterface(metaclass=ABCMeta):
    """
        This class is blue print for setting the all needed configs.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'set_config') and
                hasattr(subclass, 'input_cnf') and
                hasattr(subclass, 'output_cnf') or
                NotImplemented
                )

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set_config(self):
        pass

    @property
    @abstractmethod
    def input_cnf(self):
        pass

    @input_cnf.setter
    @abstractmethod
    def input_cnf(self, path):
        pass

    @property
    @abstractmethod
    def output_cnf(self):
        pass

    @output_cnf.setter
    @abstractmethod
    def output_cnf(self, path):
        pass


class SetWebAreal(CnfWASettInterface):

    def __init__(self):
        super(SetWebAreal, self).__init__()
        self.__input_cnf = ""
        self.__output_cnf = ""
        self._config = object()

    @property
    def config_object(self):
        if issubclass(self._config, object):
            raise TypeError("You did not set config!")
        return self._config

    @config_object.setter
    def config_object(self, path):
        from configparser import ConfigParser
        if issubclass(path, str):
            self._config = ConfigParser().read(path)
        else:
            raise TypeError("Given path: {} is not a STRING".format(path))

    def set_config(self):
        pass

    @property
    def input_cnf(self):
        if self.__input_cnf == "":
            raise ValueError("Path to input config was not set!")
        return self.__input_cnf

    @input_cnf.setter
    def input_cnf(self, path):
        from os.path import exists
        if exists(path):
            self.__input_cnf = path
            return
        raise FileNotFoundError("The file at {} was not found!".format(path))

    @property
    def output_cnf(self):
        if self.__output_cnf == "":
            raise ValueError("Path to output config was not set!")
        return self.__output_cnf

    @output_cnf.setter
    def output_cnf(self, path):
        self.__output_cnf = path


if __name__ == '__main__':
    WB = SetWebAreal()
    WB.input_cnf = 'test_config.ini'
    WB.output_cnf = 'output_cnf'
