import pandas as pd


class Blackboard:

    def __init__(self):
        super(Blackboard, self).__init__()
        self.tally = pd.DataFrame(columns=["w", "d", "l"], data=[[0,0,0]])
        self.games_played = 0

    def record_result(self, player_result):
        self.tally.loc[self.games_played] = [0, 0, 0]
        self.tally.loc[self.games_played, player_result] = 1
        self.games_played += 1

    def player_cumulative_results(self):
        return self.tally.sum(axis=0)

    def player_averages(self):
        return self.player_cumulative_results()/self.games_played
