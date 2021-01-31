import pandas as pd
from rps.mechanics import determine_winner


class Blackboard:

    def __init__(self):
        super(Blackboard, self).__init__()
        self.tally = pd.DataFrame(columns=["w", "d", "l"], data=[[0, 0, 0]])
        self.player_moves = pd.DataFrame(columns=["Rock", "Paper", "Scissors"], data=[[0, 0, 0]])
        self.games_played = 0

    def record_game(self, player_choice, pc_choice):
        outcome = determine_winner(player_choice, pc_choice)
        self.tally.loc[self.games_played] = [0, 0, 0]
        self.tally.loc[self.games_played, outcome] = 1
        self.player_moves.loc[self.games_played] = [0, 0, 0]
        self.player_moves.loc[self.games_played, player_choice] = 1
        self.games_played += 1
        return outcome

    def player_cumulative_results(self):
        return self.tally.sum(axis=0)

    def player_averages(self):
        return self.player_cumulative_results() / self.games_played

    def move_averages(self, from_last: int = None):
        df = self.player_moves
        if from_last:
            df = df.iloc[-1 * from_last:, :]
        return df.mean(axis=0)
