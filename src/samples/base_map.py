from abc import ABC, abstractmethod
from typing import Iterable, Tuple


class BaseMap(ABC):
    """Abstract class with interface for all Maps"""
    @abstractmethod
    def __setitem__(self, key, value) -> None:
        pass

    @abstractmethod
    def __getitem__(self, item) -> int:
        pass

    @abstractmethod
    def __delitem__(self, key) -> None:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __iter__(self) -> Iterable[Tuple[str, int]]:
        pass

    def write(self, path: str) -> None:
        """A method to write Map into file"""
        with open(path, 'w', encoding='utf-8') as write_file:
            for key, value in self:
                write_file.write(f'{key}    {value}\n')

    @classmethod
    def read(cls, path: str) -> 'BaseMap':
        """A method to read keys and its values and write it into Map"""
        my_obj = cls()

        with open(path, 'r', encoding='utf-8') as file:
            line = file.readline()
            while line:
                key_value = line.split()
                my_obj[key_value[0]] = int(key_value[1])
                line = file.readline()
            file.close()

