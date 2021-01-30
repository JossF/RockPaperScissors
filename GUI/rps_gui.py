import PySimpleGUI as sg


def generate_window():
    weapon_rock = sg.Button("Rock")
    weapon_scissors = sg.Button("Scissors")
    weapon_paper = sg.Button("Paper")
    end_game = sg.Button("Quit")
    return sg.Window("Play", [[sg.Text("Select your weapon!")], [weapon_rock, weapon_paper, weapon_scissors],
                              [sg.Text("Had enough?")],[end_game]])


if __name__ == '__main__':
    while True:
        rsp_gui = generate_window()
        event, values = rsp_gui.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        else:
            descs = dict(Rock="brave", Scissors="cunning", Paper="noble")
            print(f"You selected {event}, a {descs[event]} choice")
