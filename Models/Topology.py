from abc import ABC, abstractmethod


class Topology(ABC):

    @abstractmethod
    def createTopology(cls):
        pass
