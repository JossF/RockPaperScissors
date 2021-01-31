from rps.schemas import num_vals


def determine_winner(player, computer):
    player_num = num_vals[player]
    pc_num = num_vals[computer]
    if player_num == pc_num - 1 or player_num == pc_num + 2:
        return "l"
    elif player_num == pc_num:
        return "d"
    else:
        return "w"
