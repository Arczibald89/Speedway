from Data import *
from Team import Team
from Match import *
import random


def say_hello_and_pick_team():
    """
    Function enables Player to pick his team city - One of competing this season (2018) in Polish speedway league.
    Function creates 8 team instances.
    """
    print("Witaj w grze SEZON ŻUŻOLOWY!\n Wybierz numer zespołu, którym będziesz zarządzać (0-7)")
    teams = []
    i = 0
    answer = None
    for team in team_names:
        print(str(i) + "\t" + team)
        i += 1
    while answer not in range(8):
        try:
            answer = int(input("Wybierz drużynę(0-7)"))
        except (ValueError, IndexError):
            print(" Wpisz numer 0-7 !!!")
    player1 = Team(team_names[answer])
    player1.human = True
    teams.append(player1)
    team_names.pop(answer)
    for num in range(7):
        computer = Team(team_names[num])
        teams.append(computer)
    print("Brawo! Poprowadzisz zespół : ", player1.team_name)
    input("\n Naciśnij ENTER By zobaczyć wylosowane numery Draftu na ten sezon")
    return teams


def random_draft(teams):
    """
    Draft lottery. Each team will pick riders from available (unpicked riders) to team squad. Draft lottery decides
    about picking order and season schedule. The lower draft number the better.
    """
    draft_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(draft_numbers)
    i = 0
    for team in teams:
        team.draft_number = draft_numbers[i]
        i += 1
    print("\nOto wylosowane numery draftu (Kolejność wyboru zawodników do drużyny) :")
    teams = show_sorted_draft(teams)
    return teams


def show_sorted_draft(teams):
    """ Function shows and returns teams sorted by draft numbers. """
    draft_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    teams_copy = []
    num = 0
    for i in range(7):
        for team in teams:
            try:
                if team.draft_number == draft_numbers[num]:
                    teams_copy.append(team)
                    num += 1
            except IndexError:
                break
    teams = teams_copy
    for team in teams:
        print(team.team_name + "\t" + str(team.draft_number))
    return teams


def show_available_riders():
    """ Function shows unpicked riders (without teams)."""
    print()
    i = 0
    for rider in riders_list:
        print(str(i) + ". " + str(rider))
        i += 1


def next_rider(teams):
    """ Function enables choosing riders to Player's Team and Computer's Teams."""
    random.shuffle(riders_list)
    input("\n Naciśnij ENTER by zobaczyć listę zawodników dostępnych do wyboru!")
    while riders_list:
        for team in teams:
            pick_rider(team)
    assign_riders(teams)


def pick_rider(team):
    max_riders = 8
    if len(team.riders) < max_riders:
        if team.human:
            human_rider(team)

        else:
            team.comp_next_rider(riders_list)


def human_rider(team):
    good_choice = False
    while not good_choice:
        try:
            show_available_riders()
            number = int(input("Wprowadź numer zawodnika, którego chcesz wybrać do zespołu (0 - " +
                               str(len(riders_list) - 1) + ") \n"))
            team.riders.append(riders_list[number])
            riders_list.pop(number)
            team.show_team()
            print()
            good_choice = True
        except (ValueError, IndexError):
            pass


def assign_riders(teams):
    """Function assigns team name to riders and shows Player's Team and accurate stats of Player's riders"""
    for team in teams:
        for rider in team.riders:
            rider.team_name = team.team_name
        if team.human:
            print("\nOto pełen skład, prowadzonej przez Ciebie drużyny - " + team.team_name + " :\n")
            for rider in team.riders:
                rider.is_visible()
                print(rider)


def schedule_set(teams):
    """ Function sets league schedule according to draft numbers."""
    for day in league:
        for num in day:
            num[0] = teams[num[0]]
            num[1] = teams[num[1]]
    show_schedule()
    return league


def show_schedule():
    """ Function shows league schedule."""
    answer = input("\nWciśnij 1 by zobaczyć terminarz na cały sezon lub wciśnij ENTER by przejść do pierwszej kolejki")
    if answer == "1":
        num = 1
        for day in league:
            print("\n" + str(num) + ".  Kolejka")
            num += 1
            for game in day:
                print(str(game[0]) + " - " + str(game[1]))



def show_season_table(teams):
    """
    Function establishes actual order and shows season table. In case of tie in 'overall points' goes to
    'little points' differential.
    """
    all_points_list = []
    all_differential_points = []
    for team in teams:
        all_points_list.append(team.total_points)
        all_differential_points.append(int(team.differential))
    all_points_list = list(set(all_points_list))
    all_points_list.sort()
    all_differential_points = list(set(all_differential_points))
    all_differential_points.sort()
    all_differential_points.reverse()
    all_teams_sorted = []
    print("\n\t \t \t TABELA LIGOWA ")
    for a in range(len(all_points_list)):
        equal_points = []
        for team in teams:
            if team.total_points == all_points_list[a]:
                equal_points.append(team)
        if len(equal_points) == 1:
            all_teams_sorted.append(equal_points[0])
        if len(equal_points) > 1:
            sorted_list = []
            for num in range(len(all_differential_points)):
                for i in range(len(equal_points)):
                    if equal_points[i].differential == all_differential_points[num]:
                        sorted_list.append(equal_points[i])
            sorted_list = sorted_list[:: -1]
            for team in sorted_list:
                all_teams_sorted.append(team)
    teams_in_proper_position = all_teams_sorted[::-1]

    position = 1
    for team in teams_in_proper_position:
        team.show_team_stats(position)
        position += 1


def show_player_rider_stats(teams):
    """ Function establishes actual order and shows Player's riders sorted by points per run average."""
    all_riders_list = []
    all_averages_list = []
    for team in teams:
        if team.human:
            for rider in team.riders:
                all_riders_list.append(rider)
    for rider in all_riders_list:
        all_averages_list.append(rider.average)
    all_averages_list = list(set(all_averages_list))
    all_averages_list.sort()
    all_averages_list.reverse()
    for i in range(len(all_averages_list)):
        for rider in all_riders_list:
            if rider.average == all_averages_list[i]:
                rider.show_overall_stats()


def show_all_rider_stats(teams):
    """ Function establishes actual order and shows all riders sorted by points per run average."""
    all_riders_list = []
    all_averages_list = []
    for team in teams:
        for rider in team.riders:
            all_riders_list.append(rider)
    for rider in all_riders_list:
        all_averages_list.append(rider.average)
    all_averages_list = list(set(all_averages_list))
    # print(all_averages_list)
    all_averages_list.sort()
    all_averages_list.reverse()
    # print(all_averages_list)
    for i in range(len(all_averages_list)):
        for rider in all_riders_list:
            if rider.average == all_averages_list[i]:
                rider.show_overall_stats()


def menu_player_choice(teams):
    """ Function fulfills Player's menu choice."""
    choice = input("Naciśnij numer od 1-4, by wybrać, co chcesz zrobić \n")
    if choice == "1":
        return 1
    if choice == "2":
        show_season_table(teams)
    if choice == "3":
        show_player_rider_stats(teams)
    if choice == "4":
        show_all_rider_stats(teams)


def menu(day_num, teams):
    """ Function shows possible menu options."""
    choice = None
    while choice != 1:
        if day_num < 15:
            print("\n\t \t \t MENU Ligi Żużlowej")
            print("1 - Przejdź do kolejki nr. " + str(day_num) + "\n"
                  "2 - Pokaż tabelę ligową \n" +
                  "3 - Pokaż statystyki Twoich zawodników \n" +
                  "4 - Poakż statystyki wszystkich zawodników \n")
            choice = menu_player_choice(teams)
        else:
            print("\n\t \t \t MENU Ligi Żużlowej")
            print("1 - KONIEC SEZONU \n"
                  "2 - Pokaż tabelę ligową \n" +
                  "3 - Pokaż statystyki Twoich zawodników \n" +
                  "4 - Poakż statystyki wszystkich zawodników \n")
            choice = menu_player_choice(teams)


def regular_season(teams):
    """ Regular season - 14 days, 56 speedway matches - 4 matches each day. """
    day_num = 1
    all_results = []
    for day in league:
        day_results = []
        input("\n Naciśnij ENTER by przejść do kolejki nr. " + str(day_num))
        print("\t\t\tKOLEJKA NR. " + str(day_num))
        for one_match in day:
            print(one_match[0].team_name + " - " + one_match[1].team_name)
        input("\n Naciśnij ENTER by przejść do następnego meczu.\n")
        for one_match in day:
            match(one_match[0], one_match[1], day_results)
        print("\nWyniki KOLEJKI NR. " + str(day_num) + "\n")
        all_results.append(day_results)
        day_num += 1
        for result in all_results[day_num - 2]:
            print(result)
        input("\n Naciśnij ENTER by przejść dalej \n")
        menu(day_num, teams)
    end_of_game(teams)


def end_of_game(teams):
    """ Function shows a big heart for Player's patience :) and shows final standings."""
    print("\t\t\t\t\t GRATULACJE  - UKOŃCZYŁEŚ SEZON !!!")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
          "░░░░░░░░░░░░▄████▄▄░░░░▄████▄░░░░░░░░░\n"
          "░░░░░░░░░▄▄████████▄░▄█████████▄▄░░░░░░\n"
          "░░░░░░▄████████████████████████████▄░░░\n"
          "░░░░▄████████████████████████████████▄▄\n"
          "░░▄██████████▀░░░▀▀████▀░░░▀▀███████████\n"
          "▄███████████░░░░░░░░▀▀░░░░░░░░█████████\n"
          "████████████░░░░   DZIĘKUJĘ   ░░░░░██████████\n"
          "█████████████░░░░░░░░░░░░░░░▄██████████\n"
          "███████████████▄▄▄░░░░░░▄▄██████████████\n"
          "████████████████████▄░▄█████████████████\n"
          "███▀▀▀▀▀▀░░░░▀▀▀█████████▀▀░░░░░░░░░░░░\n"
          "▀▀░░░░░░░░░░░░░░░░▀▀██▀▀░░░░░░░░░░░░░\n")
    show_season_table(teams)