from abc import ABC,abstractmethod 

class abst_Game(ABC):
    
    @abstractmethod
    def game_intro():
        ...

class abst_Mode(ABC):
    
    @abstractmethod
    def mode_intro():
        ...

    @abstractmethod
    def grading_system():
        ...

    @abstractmethod
    def hangman_output():
        ...


class abst_Data(ABC):

    @abstractmethod
    def game_table():
        ... 

class abst_Results_Table(ABC):

    @abstractmethod
    def show_results():
        ...
    
    @abstractmethod
    def save_results():
        ...

    @abstractmethod
    def add_new_row():
        ...

    @abstractmethod
    def add_new_row():
        ...

    @abstractmethod
    def load_results():
        ...

