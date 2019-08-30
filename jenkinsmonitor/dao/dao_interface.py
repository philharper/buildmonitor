import abc


class Dao(abc.ABC):

    @abc.abstractmethod
    def get_monitor(self, monitor_id):
        pass

    @abc.abstractmethod
    def get_monitors(self):
        pass

    @abc.abstractmethod
    def create_monitor(self, monitor):
        pass

    @abc.abstractmethod
    def delete_monitor(self, monitor_id):
        pass

    @abc.abstractmethod
    def update_monitor(self, monitor):
        pass
