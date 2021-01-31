import PySimpleGUI as sg
import pandas as pd
from rps.computer_engine import Computer
from rps.schemas import outcome_to_full_str
from rps.blackboard import Blackboard


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


def update_gui_tally(window, tally: pd.DataFrame):
    window['w'].update(tally.iloc[0])
    window['d'].update(tally.iloc[1])
    window['l'].update(tally.iloc[2])


if __name__ == '__main__':
    bb = Blackboard()
    pc = Computer(bb)
    rsp_gui = generate_window()
    tally = [0, 0, 0]
    while True:
        event, values = rsp_gui.read()
        update_gui_tally(rsp_gui, bb.player_cumulative_results())
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        else:
            descs = dict(Rock="brave", Scissors="cunning", Paper="noble")
            rsp_gui['Decision'].update(f"You selected {event}, a {descs[event]} choice")
            pc_choice = pc.make_choice()
            player_choice = event
            outcome = bb.record_game(player_choice, pc_choice)
            update_gui_tally(rsp_gui, bb.player_cumulative_results())
            rsp_gui['Computer'].update(f"The computer has selected {pc_choice}, how random.")
            rsp_gui['Result'].update(f"The results? {outcome_to_full_str[outcome]}")
    rsp_gui.close()
