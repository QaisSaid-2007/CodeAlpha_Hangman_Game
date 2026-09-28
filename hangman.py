from blueprint import abst_Mode, abst_Game, abst_Data
from Results import Results_Table
import pandas as pd 
import random
import time

class Data(abst_Data):
    
    def game_table(self) -> pd.DataFrame:
        """ The game_table method thats in the Data class accepts no arguments, but it returns a pandas dataFrame
            that contains the following columns (word, hint1, hint2, hint3 and game_mode), the game_table function
            is the main database for the hangman game."""

        data = {
        "word": ["WHALE", "CLOUD", "APPLE","STAR","DOGS","JAVA","MONKEY","PENCIL","CINEMA"],
        "hint1": [
            "I am a very large animal.",
            "I float in the sky.",
            "I am a fruit.",
            "You can find me in the sky",
            "I am an animal",
            "I am a type of drink",
            "I am an animal",
            "I am used for writing",
            "I am a place"
        ],
        "hint2": [
            "I live in the ocean.",
            "I can bring rain.",
            "I can be red, green, or yellow.",
            "I can shine very brightly",
            "I am known for being very loyal",
            "I am associated with coffee",
            "I can climb trees",
            "I usually contain graphite",
            "Many people go here to watch movies"
        ],
        "hint3": [
            "I breathe air despite living in water.",
            "I can be white, gray, or dark.",
            "I can be used to make pie.",
            "I appear at night",
            "I can bark",
            "I am also the name of a programming language",
            "I am often associated with bananas",
            "You can sharpen me",
            "I have a large screen"
        ]
        }
        df = pd.DataFrame(data)

        def g_m(data: pd.DataFrame) -> str:
            word_len = len(data['word'])
            if word_len == 6:
                return 'Hard' 
            elif word_len == 5:
                return 'Medium'
            else:
                return "Easy"
        df['game_mode'] = df.apply(lambda x: g_m(x),axis=1) 

        return df

class Game(abst_Game):

    def __init__(self) -> None:
        self.__DataBase : pd.DataFrame = Data().game_table()

    @property
    def get_Database(self) -> pd.DataFrame:
        return self.__DataBase

    def game_intro(self) -> None:
        """ The game_intro method thats inside the Game class, takes no arguments and aims to give the user a breifly explained description about the Game and its rules."""

        print("*************** Hangman Game ***************")
        print("** Hello and welcome to the Hangman Game please read the game instructions carfully **\n")
        print("Hangman is a word-guessing game where you have to guess a hidden word one letter at a time")
        print("How to play:")
        print("1: A secret word is chosen.\n2: You guess one letter at a time.\n3: If the letter is in the word, it will be revealed.\n4: If the letter is incorrect, you lose one attempt.\n5: Use the available hints if you get stuck.\n6: Guess the complete word before you run out of attempts!")

    class Mode(abst_Mode):
        """ 
        The Mode class is the parent class for the Easy,Medium, and Hard classes.
        The purpose of the Mode class is to resuse the following methods:
        1. word_letter_tracker() -> tracking the secret word letters
        2. get_hint() -> give the user a hint that will help guess the word
        3. get_word() -> picks the secret word randomly
        4. hangman_output() -> show the current hangman development depending on the attempts left for the user to guess the secret word 
        """
        def __init__(self,database,mode) -> None:
            self.database = database[database['game_mode'] == mode].reset_index(drop=True)

        def word_letter_tracker(self, word: str, letters_guessed: set[str]) -> None:
            for letter in word:
                if letter in letters_guessed:
                    print(letter, end=' ')
                else:
                    print('_', end=" ")
            print("")

        def get_hint(self, row_x: int, hint_x: int) -> str | None:
            match hint_x:
                case 1:
                    return '\n' + self.database.iloc[row_x]['hint1']
                case 2:
                    return '\n' + self.database.iloc[row_x]['hint2']
                case 3:
                    return '\n' + self.database.iloc[row_x]['hint3']
            return None

        def get_word(self, row_x: int) -> str:
            return self.database.iloc[row_x]['word']

        def hangman_stages(self,stage) -> str:
            def stage_1() -> str:
                return f"{'o':^9}"

            def stage_2() -> str:
                return f"{stage_1()} \n {'--':<5}"

            def stage_3() -> str:
                return f"{stage_2()}{'--':>1}"

            def stage_4() -> str:
                return f"{stage_3()} \n {'|':>4}"

            def stage_5() -> str:
                return f"{stage_4()} \n {'/':>3}"

            def stage_6() -> str:
                return f"{stage_5()} {'\\':>0}"

            match stage:
                case 1:
                    return stage_1()
                case 2:
                    return stage_2()
                case 3:
                    return stage_3()
                case 4:
                    return stage_4()
                case 5:
                    return stage_5()
                case 6:
                    return stage_6()
    
    class Easy(Mode):
        def __init__(self,database: pd.DataFrame, mode: str = 'Easy') -> None:
            super().__init__(database,'Easy')
            self.mode = mode

        def mode_intro(self) -> None:
            print("\n********** Easy Mode **********")
            print("attempts: 6")
            print("Hints: 3")

        @staticmethod
        def grading_system(hints_used: int , attempts_used: int , is_word_guessed: bool, username:str) -> float:
            print("\n*************** SCORE REPORT & CALCULATIONS ***************")
            print("Step 1: grade is out of 10")
            print("Step 2: final_grade = 10 - (attempts_used x 0.25) - (hints_used x 1) - (5 if you failed to guess the word)")
            
            grade: float = 10.00
            grade -= (attempts_used * 0.25)
            grade -= (hints_used * 1)
            grade -= (5.00 if not is_word_guessed else 0) 
            
            final_grade = round((grade / 10) * 100 , 2)
            print(f"***** Useraname: {username} *****")
            print(f"***** Hints used: {hints_used} *****")
            print(f"***** Attempts used: {attempts_used} *****")
            print(f">>>>> SCORE = {final_grade}%      status = {"PASS" if is_word_guessed else "FAIL"} <<<<<")

            return final_grade

        def game(self, username: str) -> None:
            word_row_choice: str = random.randint(0, len(self.database)-1)
            word_choice: str = self.get_word(row_x = word_row_choice)
            word_choice_letters: str = len(set(word_choice))
            hints_left: int = 3
            attempts_left: int = 6
            is_guessed: bool = False
            letters_guessed: set[str] = set()

            print("\n********** HANGMAN GAME - EASY MODE - GAME ON **********")
            while attempts_left != 0 and not is_guessed:
                user_input = input("Enter (HINT) for a hint otherwise enter your letter: ")

                if not isinstance(user_input, str) or not user_input.isalpha():
                    print("-> Invalid input data type try again !!!")
                
                elif user_input.upper() == "HINT":
                    if hints_left > 0:
                        print("->",self.get_hint(row_x = word_row_choice, hint_x = hints_left))
                        hints_left -= 1
                    else:
                        print("-> No more Hints remaning")

                else:
                    if len(user_input) == 1:
                        letter = user_input.upper()
                        if letter in word_choice and letter not in letters_guessed:
                            print("-> Correct choice WELL DONE !!!")
                            letters_guessed.add(letter)
                            self.word_letter_tracker(word=word_choice, letters_guessed=letters_guessed) 
                        else:
                            print("-> WRONG !!!")
                            print(self.hangman_output(attempts_left=attempts_left)) 
                            attempts_left -= 1
                        
                    else:
                        print("One letter at a time")

                if len(letters_guessed) == word_choice_letters:
                    is_guessed = True

                print(f"***** HINTS LEFT: {hints_left} *****")
                print(f"***** CHANCES LEFT: {attempts_left} *****")

            game_data_dict : dict[str,int|bool|float] = {"hints_used":3 - hints_left ,"attempts_used": 6 - attempts_left ,"is_word_guessed": is_guessed}
            score = self.grading_system(**game_data_dict,username=username)

            print("\n********** HANGMAN GAME - EASY MODE - GAME OFF **********")

            return {**game_data_dict, 'Username':username ,'Mode':self.mode,'grade':score}

        def word_letter_tracker(self,word: str, letters_guessed: set[str]) -> None:
            super().word_letter_tracker(word,letters_guessed)

        def hangman_output(self,attempts_left: int) -> str:
            stage = None

            match attempts_left:
                case 1:
                    stage = 6
                case 2:
                    stage = 5
                case 3:
                    stage = 4
                case 4:
                    stage = 3
                case 5:
                    stage = 2
                case 6:
                    stage = 1

            return super().hangman_stages(stage)

        def get_hint(self, row_x: int, hint_x: int) -> str:
            return super().get_hint(row_x,hint_x)

        def get_word(self,row_x: int) -> str:
            return super().get_word(row_x)

    class Medium(Mode):
        def __init__(self, database: pd.DataFrame, mode: str = 'Medium') -> None:
            super().__init__(database,'Medium')
            self.mode = mode

        def mode_intro(self) -> None:
            print("\n********** Medium Mode **********")
            print("attempts: 4")
            print("Hints: 3")

        @staticmethod
        def grading_system(hints_used: int, attempts_used: int, is_word_guessed: bool, username: str) -> float:
            print("\n*************** SCORE REPORT & CALCULATIONS ***************")
            print("Step 1: grade is out of 10")
            print("Step 2: final_grade = 10 - (attempts_used x 0.5) - (hints_used x 1) - (5 if you failed to guess the word)")

            grade: float = 10.00
            grade -= (attempts_used * 0.5)
            grade -= (hints_used * 1)
            grade -= (5.00 if not is_word_guessed else 0)

            final_grade = round((grade / 10) * 100, 2)
            print(f"***** Useraname: {username} *****")
            print(f"***** Hints used: {hints_used} *****")
            print(f"***** Attempts used: {attempts_used} *****")
            print(f">>>>> SCORE = {final_grade}%      status = {"PASS" if is_word_guessed else "FAIL"} <<<<<")

            return final_grade

        def game(self, username: str) -> None:
            word_row_choice: str = random.randint(0, len(self.database) - 1)
            word_choice: str = self.get_word(row_x=word_row_choice)
            word_choice_letters: str = len(set(word_choice))
            hints_left: int = 3
            attempts_left: int = 4
            is_guessed: bool = False
            letters_guessed: set[str] = set()

            print("\n********** HANGMAN GAME - MEDIUM MODE - GAME ON **********")
            while attempts_left != 0 and not is_guessed:
                user_input = input("Enter (HINT) for a hint otherwise enter your letter: ")

                if not isinstance(user_input, str) or not user_input.isalpha():
                    print("-> Invalid input data type try again !!!")

                elif user_input.upper() == "HINT":
                    if hints_left > 0:
                        print("->", self.get_hint(row_x=word_row_choice, hint_x=hints_left))
                        hints_left -= 1
                    else:
                        print("-> No more Hints remaning")

                else:
                    if len(user_input) == 1:
                        letter = user_input.upper()
                        if letter in word_choice and letter not in letters_guessed:
                            print("-> Correct choice WELL DONE !!!")
                            letters_guessed.add(letter)
                            self.word_letter_tracker(word=word_choice, letters_guessed=letters_guessed)
                        else:
                            print("-> WRONG !!!")
                            print(self.hangman_output(attempts_left=attempts_left))
                            attempts_left -= 1

                    else:
                        print("One letter at a time")

                if len(letters_guessed) == word_choice_letters:
                    is_guessed = True

                print(f"***** HINTS LEFT: {hints_left} *****")
                print(f"***** CHANCES LEFT: {attempts_left} *****")

            game_data_dict: dict[str, int | bool | float] = {"hints_used": 3 - hints_left, "attempts_used": 4 - attempts_left, "is_word_guessed": is_guessed}
            score = self.grading_system(**game_data_dict, username=username)

            print("\n********** HANGMAN GAME - MEDIUM MODE - GAME OFF **********")

            return {**game_data_dict, 'Username':username ,'Mode':self.mode,'grade':score}

        def word_letter_tracker(self, word: str, letters_guessed: set[str]) -> None:
            super().word_letter_tracker(word,letters_guessed)

        def hangman_output(self, attempts_left: int) -> str:
            stage = None

            match attempts_left:
                case 1:
                    stage = 6
                case 2:
                    stage = 4
                case 3:
                    stage = 3
                case 4:
                    stage = 2

            return super().hangman_stages(stage)

        def get_hint(self, row_x: int, hint_x: int) -> str:
            return super().get_hint(row_x,hint_x)

        def get_word(self, row_x: int) -> str:
            return super().get_word(row_x)
            
    class Hard(Mode):
        def __init__(self,database: pd.DataFrame, mode: str = 'Hard') -> None:
            super().__init__(database,'Hard')
            self.mode = mode

        def mode_intro(self) -> None:
            print("\n********** Hard Mode **********")
            print("attempts: 3")
            print("Hints: 3")

        @staticmethod
        def grading_system(hints_used: int, attempts_used: int, is_word_guessed: bool, username: str) -> float:
            print("\n*************** SCORE REPORT & CALCULATIONS ***************")
            print("Step 1: grade is out of 10")
            print("Step 2: final_grade = 10 - (attempts_used x 1) - (hints_used x 1) - (4 if you failed to guess the word)")

            grade: float = 10.00
            grade -= (attempts_used * 1)
            grade -= (hints_used * 1)
            grade -= (4.00 if not is_word_guessed else 0)

            final_grade = round((grade / 10) * 100, 2)
            print(f"***** Useraname: {username} *****")
            print(f"***** Hints used: {hints_used} *****")
            print(f"***** Attempts used: {attempts_used} *****")
            print(f">>>>> SCORE = {final_grade}%      status = {"PASS" if is_word_guessed else "FAIL"} <<<<<")

            return final_grade

        def game(self, username: str) -> None:
            word_row_choice: str = random.randint(0, len(self.database) - 1)
            word_choice: str = self.get_word(row_x=word_row_choice)
            word_choice_letters: str = len(set(word_choice))
            hints_left: int = 3
            attempts_left: int = 3
            is_guessed: bool = False
            letters_guessed: set[str] = set()

            print("\n********** HANGMAN GAME - HARD MODE - GAME ON **********")
            while attempts_left != 0 and not is_guessed:
                user_input = input("Enter (HINT) for a hint otherwise enter your letter: ")

                if not isinstance(user_input, str) or not user_input.isalpha():
                    print("-> Invalid input data type try again !!!")

                elif user_input.upper() == "HINT":
                    if hints_left > 0:
                        print("->", self.get_hint(row_x=word_row_choice, hint_x=hints_left))
                        hints_left -= 1
                    else:
                        print("-> No more Hints remaning")

                else:
                    if len(user_input) == 1:
                        letter = user_input.upper()
                        if letter in word_choice and letter not in letters_guessed:
                            print("-> Correct choice WELL DONE !!!")
                            letters_guessed.add(letter)
                            self.word_letter_tracker(word=word_choice, letters_guessed=letters_guessed)
                        else:
                            print("-> WRONG !!!")
                            print(self.hangman_output(attempts_left=attempts_left))
                            attempts_left -= 1

                    else:
                        print("One letter at a time")

                if len(letters_guessed) == word_choice_letters:
                    is_guessed = True

                print(f"***** HINTS LEFT: {hints_left} *****")
                print(f"***** CHANCES LEFT: {attempts_left} *****")

            game_data_dict: dict[str, int | bool | float] = {"hints_used": 3 - hints_left, "attempts_used": 3 - attempts_left, "is_word_guessed": is_guessed}
            score = self.grading_system(**game_data_dict, username=username)

            print("\n********** HANGMAN GAME - HARD MODE - GAME OFF **********")
            return {**game_data_dict, 'Username':username ,'Mode':self.mode,'grade':score}

        def hangman_output(self, attempts_left: int) -> str:
            stage = None

            match attempts_left:
                case 1:
                    stage = 6
                case 2:
                    stage = 4
                case 3:
                    stage = 3

            return super().hangman_stages(stage)

        def word_letter_tracker(self, word: str, letters_guessed: set[str]) -> None:
            super().word_letter_tracker(word,letters_guessed)

        def get_hint(self, row_x: int, hint_x: int) -> str:
            return super().get_hint(row_x,hint_x)

        def get_word(self, row_x: int) -> str:
            return super().get_word(row_x)

def main() -> None:
    Main_Game: Game = Game()
    Database: pd.DataFrame = Main_Game.get_Database
    Results: pd.DataFrame = Results_Table()
    easy_game: Easy = Main_Game.Easy(Database)
    medium_game: Medium = Main_Game.Medium(Database)
    hard_game: Hard = Main_Game.Hard(Database)
    
    Main_Game.game_intro()
    game_running: bool = True

    while game_running:
        # getting the players username
        username : str | None = None
        user_name_running: bool = True
        while user_name_running:
            print("\nBefore starting the game please enter your name to save your game results")
            username = input("Username: ").title()
            
            if username.isalpha():
                print(f"Welcome {username}")
                user_name_running = False
            else:
                print("Invalid username !")
        
        # getting the game mode
        mode: int | None = None
        mode_running: bool = True
        while mode_running:
            print("Enter 1 -> Easy or 2 -> Medium or 3 -> Hard")
            mode = input("Game Mode: ")

            if mode in {'1','2','3'}:
                mode = int(mode)
                mode_running = False
            else:
                print("Invalid game mode !")

        # starting the game
        user_mode: Easy | Medium | Hard | None = None
        match mode:
            case 1:
                user_mode = easy_game
            case 2:
                user_mode = medium_game
            case 3:
                user_mode = hard_game
        
        user_mode.mode_intro()

        for i in range(5,0,-1):
            print(f"Game starts on {i}...")
            time.sleep(1)

        result = user_mode.game(username=username)
        Results.add_new_row(result)

        # another game or quit the game or show results
        user_choice_running : bool = True
        while user_choice_running:
            print("\n-> 1 to QUIT")
            print("-> 2 to Play Again")
            print("-> 3 to Show Results")
            user_choice : str = input("Your choice: ")

            if user_choice in {'1','2','3'}:
                match user_choice:
                    case '1':
                        user_choice_running = False
                        game_running = False
                    
                    case '2':
                        user_choice_running = False

                    case '3':
                        Results.show_results(username)
            else:
                print("Invalid answer !")        

    print("\n********** BYE !!! **********")

if __name__ == "__main__":
    main()

