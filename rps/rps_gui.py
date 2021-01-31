import PySimpleGUI as sg
from rps.computer_engine import random_choice
from rps.mechanics import determine_winner
from rps.schemas import outcome_to_full_str


def generate_window():
    weapon_rock = sg.Button("Rock")
    weapon_scissors = sg.Button("Scissors")
    weapon_paper = sg.Button("Paper")
    end_game = sg.Button("Quit")
    return sg.Window("Play", [[sg.Text("Select your weapon!")],
                              [weapon_rock, weapon_paper, weapon_scissors],
                              [sg.Text(key="Decision", size=(50, 1))],
                              [sg.Text(key="Computer", size=(50, 1))],
                              [sg.Text(key="Result", size=(75, 1))],
                              [sg.Text("Running Tally")],
                              [sg.Text("Wins", size=(5, 1)), sg.Text("Draws", size=(5, 1)),
                               sg.Text("Losses", size=(5, 1))],
                              [sg.Text(key="w", size=(5, 1)), sg.Text(key="d", size=(5, 1)),
                               sg.Text(key="l", size=(5, 1))],
                              [sg.Text("Had enough?", text_color="red")],
                              [end_game]])


def update_gui_tally(window, tally: list):
    window['w'].update(tally[0])
    window['d'].update(tally[1])
    window['l'].update(tally[2])


def update_tally(results, tally):
    locs = dict(w=0, d=1, l=2)
    tally[locs[results]] += 1
    return tally


if __name__ == '__main__':
    rsp_gui = generate_window()
    tally = [0, 0, 0]
    while True:
        event, values = rsp_gui.read()
        update_gui_tally(rsp_gui, tally)
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event in ["Rock", "Paper", "Scissors"]:
            descs = dict(Rock="brave", Scissors="cunning", Paper="noble")
            rsp_gui['Decision'].update(f"You selected {event}, a {descs[event]} choice")
            pc_choice = random_choice()
            player_choice = event
            outcome = determine_winner(player_choice, pc_choice)
            tally = update_tally(outcome, tally)
            update_gui_tally(rsp_gui, tally)
            rsp_gui['Computer'].update(f"The computer has selected {pc_choice}, how random.")
            rsp_gui['Result'].update(f"The results? {outcome_to_full_str[outcome]}")
    rsp_gui.close()
