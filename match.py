from single_run import *



def thirteen_regular_runs(player, computer):
    """ Scheme of 13 regular runs in Player's matches."""
    RUNS = ((0, 1, 0, 1), (5, 6, 5, 6), (2, 3, 2, 3), (4, 6, 4, 6), (0, 1, 2, 3),
            (2, 3, 4, 5), (4, 5, 0, 1), (0, 1, 4, 6), (2, 3, 0, 1), (4, 6, 2, 3),
            (1, 2, 1, 4), (0, 5, 2, 5), (3, 4, 0, 3))
    # RUNS is official runs scheme from Polish speedway league.
    # First two numbers in single run represents home riders numbers, next two represents away riders numbers
    run_squads = []
    all_runs_squads = []
    for num in range(13):
        run_squads.append(computer.match_team[RUNS[num][0]])
        run_squads.append(computer.match_team[RUNS[num][1]])
        run_squads.append(player.match_team[RUNS[num][2]])
        run_squads.append(player.match_team[RUNS[num][3]])
        all_runs_squads.append(run_squads)
        run_squads = []
    run_num = 1
    for run in all_runs_squads:
        print("\n W biegu nr: ", run_num, "pojadą: \n")
        print(run[0].name + " " + run[0].surname + " (" + run[0].team_name + ") " + str(run[0].match_stats) + "\n" +
              run[1].name + " " + run[1].surname + " (" + run[1].team_name + ") " + str(run[1].match_stats) + "\n" +
              run[2].name + " " + run[2].surname + " (" + run[2].team_name + ") " + str(run[2].match_stats) + "\n" +
              run[3].name + " " + run[3].surname + " (" + run[3].team_name + ") " + str(run[3].match_stats) + "\n")
        run = single_run_menu(run, player, computer)
        single_run(run, run_num)
        run_num += 1
        if player.riders[0].home:
            # In speedway home team name is always shown on the lef side of score, away team name on the right side
            print("\t\t\t" + player.team_name + " " + str(player.match_points) + " : " + str(computer.match_points)
                  + " " + computer.team_name)
        else:
            print("\t\t\t" + computer.team_name + " " + str(computer.match_points) + " : " + str(player.match_points)
                  + " " + player.team_name)


def thirteen_regular_runs_comp(player, computer):
    """ Scheme of 13 regular runs in Computer's matches."""
    RUNS = ((0, 1, 0, 1), (5, 6, 5, 6), (2, 3, 2, 3), (4, 6, 4, 6), (0, 1, 2, 3),
            (2, 3, 4, 5), (4, 5, 0, 1), (0, 1, 4, 6), (2, 3, 0, 1), (4, 6, 2, 3),
            (1, 2, 1, 4), (0, 5, 2, 5), (3, 4, 0, 3))
    run_squads = []
    all_runs_squads = []
    for num in range(13):
        run_squads.append(computer.match_team[RUNS[num][0]])
        run_squads.append(computer.match_team[RUNS[num][1]])
        run_squads.append(player.match_team[RUNS[num][2]])
        run_squads.append(player.match_team[RUNS[num][3]])
        all_runs_squads.append(run_squads)
        run_squads = []
    for run in all_runs_squads:
        single_run_comp(run)


def show_teams_info(player, computer):
    """ Function displays detailed information about two teams. """
    print()
    for rider in computer.match_team:
        print(rider.name + " " + rider.surname + (30-rider.name_length)*" " + str(rider.match_stats) + " Razem PKT : "
              + str(rider.match_points) + " + " + str(rider.bonus))
    print(computer.team_name + " :" + str(computer.match_points) + "\n")
    for rider in player.match_team:
        print(rider.name + " " + rider.surname + (30-rider.name_length)*" " + str(rider.match_stats) + " Razem PKT : "
              + str(rider.match_points) + " + " + str(rider.bonus))
    print(player.team_name + " :" + str(player.match_points)+ "\n")


def nominee_runs(player, computer, day_results):
    """
    Scheme of 2 nominee runs in Player's matches.
    In speedway each team picks best riders for two last runs (14 and 15 run).
    """
    run_squads = []
    all_runs_squads = []
    for num in range(2):
        run_squads.append(computer.nominee[0])
        computer.nominee.pop(0)
        run_squads.append(computer.nominee[0])
        computer.nominee.pop(0)
        run_squads.append(player.nominee[0])
        player.nominee.pop(0)
        run_squads.append(player.nominee[0])
        player.nominee.pop(0)
        all_runs_squads.append(run_squads)
        run_squads = []
    run_num = 14
    results = None
    for run in all_runs_squads:
        print("\n W biegu nr: ", run_num, "pojadą: \n")
        print(run[0].name + " " + run[0].surname + " (" + run[0].team_name + ") " + str(run[0].match_stats) + "\n" +
              run[1].name + " " + run[1].surname + " (" + run[1].team_name + ") " + str(run[1].match_stats) + "\n" +
              run[2].name + " " + run[2].surname + " (" + run[2].team_name + ") " + str(run[2].match_stats) + "\n" +
              run[3].name + " " + run[3].surname + " (" + run[3].team_name + ") " + str(run[3].match_stats) + "\n")
        run = single_run_menu(run, player, computer)
        single_run(run, run_num)
        run_num += 1
        if player.riders[0].home:
            print(player.team_name + " " + str(player.match_points) + " : " + str(computer.match_points) + " " +
                  computer.team_name)
            results = player.team_name + " " + str(player.match_points) + " : " + str(computer.match_points) + \
                " " + computer.team_name
        else:
            print(computer.team_name + " " + str(computer.match_points) + " : " + str(player.match_points) +
                  " " + player.team_name)
            results = computer.team_name + " " + str(computer.match_points) + " : " + str(player.match_points) + \
                " " + player.team_name
    day_results.append(results)


def nominee_runs_comp(player, computer, day_results):
    """ Scheme of 2 nominee runs in Computers's matches."""
    run_squads = []
    all_runs_squads = []
    for num in range(2):
        run_squads.append(computer.nominee[0])
        computer.nominee.pop(0)
        run_squads.append(computer.nominee[0])
        computer.nominee.pop(0)
        run_squads.append(player.nominee[0])
        player.nominee.pop(0)
        run_squads.append(player.nominee[0])
        player.nominee.pop(0)
        all_runs_squads.append(run_squads)
        run_squads = []
    run_num = 14
    for run in all_runs_squads:
        single_run_comp(run)
    print(player.team_name + " " + str(player.match_points) + " : " + str(computer.match_points) + " "
          + computer.team_name)
    results = player.team_name + " " + str(player.match_points) + " : " + str(computer.match_points) + " " + computer.team_name
    day_results.append(results)


def reset_stats_after_game(player, computer):
    """ Function resets stats after match."""
    teams = [player, computer]
    for team in teams:
        team.reset_match_team()


def match(home_team, away_team, day_results):
    """
    Function makes riders.home attribute proper and checks if it's Player's match or Computer's match, then chooses
    adequate scheme.
    """
    for rider in home_team.riders:
        rider.home = True
    for rider in away_team.riders:
        rider.home = False
    if home_team.human:
        match_player(home_team, away_team, day_results)
    elif away_team.human:
        match_player(away_team, home_team, day_results)
    else:
        match_comp(home_team, away_team, day_results)


def match_player(player, computer, day_results):
    """ Match scheme in Player's matches."""
    player.pick_match_team()
    computer.comp_pick_team()
    player.show_match_team()
    computer.show_match_team()
    thirteen_regular_runs(player, computer)
    show_teams_info(player, computer)
    player.pick_nominee()
    computer.comp_pick_nominee()
    nominee_runs(player, computer, day_results)
    show_teams_info(player, computer)
    player.add_match_stats(computer)
    computer.add_match_stats(player)
    player.reset_match_team()
    computer.reset_match_team()
    input("Naciśnij ENTER by przejść dalej")


def match_comp(computer1, computer2, day_results):
    """ Match scheme in Computer's matches."""
    teams = [computer1, computer2]
    for team in teams:
        team.comp_pick_team()
    thirteen_regular_runs_comp(computer1, computer2)
    for team in teams:
        team.comp_pick_nominee()
    nominee_runs_comp(computer1, computer2, day_results)
    show_teams_info(computer1, computer2)
    computer1.add_match_stats(computer2)
    computer2.add_match_stats(computer1)
    computer1.reset_match_team()
    computer2.reset_match_team()
    input("\nNaciśnij Enter, by przejść do następnego meczu!!! \n")
