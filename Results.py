from blueprint import abst_Results_Table
import pandas as pd
import matplotlib.pyplot as plt

class Results_Table(abst_Results_Table):
    """ 
    The Results_Table is a class in the Results.py file, which deals with the Hangman game results.
    The Results_Table initializes a pandas dataframe that stores the games (username, mode, grade, hints_used, attempts_used, and is_word_guessed).
    The Results_Table also includes the following functions:
        1. show_table -> return the results of the users results
        2. add_new_row -> adds a new entity to the results_table
        3. load_results -> loads the previous results table back the self.table
        4. save_results -> sends the current results table the an csv file
    """
    def __init__(self) -> None:
        self.table = pd.DataFrame(columns=["Username","Mode","grade","hints_used","attempts_used","is_word_guessed"])
        self.load_results()

    def show_table(self) -> pd.DataFrame:
        return self.table

    def add_new_row(self, row: dict[str|float|int|bool]) -> None:
        self.table.loc[len(self.table)] = row
        self.save_results()

    def load_results(self) -> None:
        try:
            self.table = pd.read_csv("Hangman_Results_table.csv")
        except FileNotFoundError:
            pass

    def save_results(self) -> None:
        self.table.to_csv("Hangman_Results_table.csv",index=False)

    def show_results(self, username: str) -> None:

        user_df = self.table[
            self.table["Username"] == username
        ].reset_index(drop=True)

        plt.style.use("Solarize_Light2")
        figure, axes = plt.subplots(1, 2, figsize=(12, 5))
        figure.suptitle(f"{username} Results",fontsize=22,fontweight='bold',color='black')

        # ---------------- BAR CHART ----------------

        values = user_df["grade"]
        categories = [f"Test {x + 1}" for x in range(len(values))]

        axes[0].bar(
            categories,
            values,
            edgecolor="black",
            linewidth=2
        )

        axes[0].set_title(
            "Tests Results",
            fontsize=18,
            color="brown",
            fontweight="bold"
        )

        axes[0].set_ylabel(
            "Score in %",
            fontsize=18,
            color="#181694"
        )

        # ---------------- PIE CHART ----------------

        user_df = (
            user_df
            .groupby("Mode", as_index=False)
            .agg(attempts=("Mode", "count"))
        )

        axes[1].pie(
            user_df["attempts"],
            labels=user_df["Mode"],
            shadow=True,
            autopct="%1.1f%%",
            textprops={
                "fontsize": 18,
                "fontweight": "bold",
                "color": "#3c0c54"
            }
        )

        axes[1].set_title(
            "Test Mode",
            fontsize=18,
            color="brown",
            fontweight="bold"
        )


        axes[1].legend(
            user_df["attempts"],
            loc="best",
            title="Attempts",
            framealpha=0.5
        )

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    pass