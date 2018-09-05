import random


def single_run(run, run_num):
    """
    Single run scheme in Player's matches.

    run - 4 riders instances.
    run_num - run number(1-15).
    Rider can fall, have defect or finish run successfully.

    Function adds every rider's time to rider's instance and to the time_list then checks order, adds points,
    shows run result and updates match result.
    """
    time_max = 82.00        # Maximal time in seconds. Always the same.
    time_list = []
    run_list = []
    i = 0
    for rider in run:
        if random.randint(1, 1000) == 1:
            print(rider.name + " " + rider.surname, "upadł")
            rider.match_points += 0
            rider.match_falls += 1
            rider.match_runs += 1
            rider.run_time = 120
            time_list.append(rider.run_time)
            rider.match_stats.append("u")
            run_list.append(rider)
        elif random.randint(1, 1000) == 2:
            print(rider.name + " " + rider.surname, "miał defekt.")
            rider.match_points += 0
            rider.match_defects += 1
            rider.match_runs += 1
            rider.run_time = 120
            time_list.append(rider.run_time)
            rider.match_stats.append("d")
            run_list.append(rider)
        else:
            time = random.randint((rider.total_skills - 20), (rider.total_skills + 15))*0.001
            if rider.home:
                # In speedway knowledge of the track is crucial.
                # If rider rides at home has better time and bigger chance to win run.
                total_time = time_max - (time_max * time) - 0.3
                rider.run_time = round(total_time, 3)
                time_list.append(rider.run_time)
                rider.match_runs += 1
                run_list.append(rider)
            else:
                total_time = time_max - (time_max * time)
                rider.run_time = round(total_time, 3)
                time_list.append(rider.run_time)
                rider.match_runs += 1
                run_list.append(rider)
        i += 1
        if i % 4 == 0:      # In single run compete 4 riders
            input("Naciśnij ENTER by rozpocząć kolejny bieg \n")

            print("\nBieg nr: ", str(run_num))
            time_list, run_list, run_list_sorted = sort_run_results(time_list, run_list)
            assign_run_points(time_list, run_list, run_list_sorted)
            time_list, run_list = remove_riders_and_times()

            input("\nNaciśnij ENTER by zobaczyć listę startową kolejnego biegu \n")


def single_run_comp(run):
    """
    Single run scheme in Computer's matches.
    Opposite to Player's scheme doesn't show result of single run. Checks order and adds points and update match
    result only.
    """
    time_max = 82.00        # Maximal time in seconds. The same in all tracks.
    time_list = []
    run_list = []
    i = 0
    for rider in run:
        if random.randint(1, 1000) == 1:
            rider.match_points += 0
            rider.match_falls += 1
            rider.match_runs += 1
            rider.run_time = 120
            time_list.append(rider.run_time)
            rider.match_stats.append("u")
            run_list.append(rider)
        elif random.randint(1, 1000) == 2:
            rider.match_points += 0
            rider.match_defects += 1
            rider.match_runs += 1
            rider.run_time = 120
            time_list.append(rider.run_time)
            rider.match_stats.append("d")
            run_list.append(rider)
        else:
            time = random.randint((rider.total_skills - 20), (rider.total_skills + 15))*0.001
            if rider.home:
                total_time = time_max - (time_max * time) - 0.3
                rider.run_time = round(total_time, 3)
                time_list.append(rider.run_time)
                rider.match_runs += 1
                run_list.append(rider)
            else:
                total_time = time_max - (time_max * time)
                rider.run_time = round(total_time, 3)
                time_list.append(rider.run_time)
                rider.match_runs += 1
                run_list.append(rider)
        i += 1
        if i % 4 == 0:
            time_list, run_list, run_list_sorted = sort_run_results(time_list, run_list)
            comp_assign_run_points(time_list, run_list, run_list_sorted)
            time_list, run_list = remove_riders_and_times()


def remove_riders_and_times():
    """ Function resets data after single run."""
    time_list = []
    run_list = []
    return time_list, run_list


def eliminate_4_ties(time_list, riders_tie4):
    """ Function decides about the order in case of 4 exactly the same times. (In speedway there are no ties)."""
    riders_tie4[0].run_time += 0.004
    time_list[0] += 0.004
    riders_tie4[1].run_time += 0.003
    time_list[1] += 0.003
    riders_tie4[2].run_time += 0.002
    time_list[2] += 0.002
    riders_tie4[3].run_time += 0.001
    time_list[3] += 0.001
    time_list.sort()
    return time_list


def eliminate_3_ties(time_list, riders_tie3):
    """ Function decides about the order in case of 3 exactly the same times. """
    new_time_list = []
    riders_tie3[0].run_time += 0.004
    new_time_list.append(riders_tie3[0].run_time)
    riders_tie3[1].run_time += 0.003
    new_time_list.append(riders_tie3[1].run_time)
    riders_tie3[2].run_time += 0.002
    new_time_list.append(riders_tie3[2].run_time)
    for time in time_list:
        if time not in new_time_list:
            new_time_list.append(time)
    time_list = new_time_list
    time_list.sort()
    return time_list


def eliminate_double_2_ties(time_list, riders_tie2):
    """ Function decides about the order in case of 2 pairs of exactly the same times. """
    new_time_list = []
    if riders_tie2[0] == riders_tie2[1]:
        riders_tie2[0].run_time += 0.004
        new_time_list.append(riders_tie2[0].run_time)
        new_time_list.append(riders_tie2[1].run_time)
    if riders_tie2[0] == riders_tie2[2]:
        riders_tie2[0].run_time += 0.001
        new_time_list.append(riders_tie2[0].run_time)
        new_time_list.append(riders_tie2[2].run_time)
    if riders_tie2[0] == riders_tie2[3]:
        riders_tie2[0].run_time += 0.005
        new_time_list.append(riders_tie2[0].run_time)
        new_time_list.append(riders_tie2[3].run_time)
    if riders_tie2[1] == riders_tie2[2]:
        riders_tie2[1].run_time += 0.003
        new_time_list.append(riders_tie2[1].run_time)
        new_time_list.append(riders_tie2[2].run_time)
    if riders_tie2[1] == riders_tie2[3]:
        riders_tie2[1].run_time += 0.003
        new_time_list.append(riders_tie2[1].run_time)
        new_time_list.append(riders_tie2[3].run_time)
    if riders_tie2[2] == riders_tie2[3]:
        riders_tie2[2].run_time += 0.002
        new_time_list.append(riders_tie2[2].run_time)
        new_time_list.append(riders_tie2[3].run_time)
    for time in time_list:
        if time not in new_time_list:
            new_time_list.append(time)
    time_list = new_time_list
    time_list.sort()
    return time_list


def eliminate_single_2_ties(time_list, riders_tie2):
    """ Function decides about the order in case of 2 exactly the same times. """
    new_time_list = []
    riders_tie2[0].run_time += 0.006
    new_time_list.append(riders_tie2[0].run_time)
    for time in time_list:
        if time not in new_time_list:
            new_time_list.append(time)
    time_list = new_time_list
    time_list.sort()
    return time_list


def eliminate_2_ties(time_list, riders_tie2):
    """ Function checks if there is one pair or two pairs of the same times. """
    if len(riders_tie2) == 4:
        time_list = eliminate_double_2_ties(time_list, riders_tie2)
    if len(riders_tie2) == 2:
        time_list = eliminate_single_2_ties(time_list, riders_tie2)
    return time_list


def check_if_4_ties(time_list, run_list):
    """ In case of 4 identical time results returns filled list, else returns empty list. """
    riders_tie4 = []
    for rider in run_list:
        if rider.run_time == time_list[0] == time_list[1] == time_list[2] == time_list[3]:
            riders_tie4.append(rider)
    return riders_tie4


def check_if_3_ties(time_list, run_list, riders_tie3):
    """ In case of 3 identical time results returns filled list, else returns empty list. """
    for rider in run_list:
        if rider.run_time == time_list[0] == time_list[1] == time_list[2]:
            riders_tie3.append(rider)
        if rider.run_time == time_list[0] == time_list[1] == time_list[3]:
            riders_tie3.append(rider)
        if rider.run_time == time_list[3] == time_list[1] == time_list[2]:
            riders_tie3.append(rider)
    return riders_tie3


def check_if_2_ties(time_list, run_list, riders_tie2):
    """ In case of 2 identical time results returns filled list, else returns empty list. """
    for rider in run_list:
        if rider.run_time == time_list[0] == time_list[1]:
            riders_tie2.append(rider)
        if rider.run_time == time_list[0] == time_list[2]:
            riders_tie2.append(rider)
        if rider.run_time == time_list[0] == time_list[3]:
            riders_tie2.append(rider)
        if rider.run_time == time_list[1] == time_list[2]:
            riders_tie2.append(rider)
        if rider.run_time == time_list[1] == time_list[3]:
            riders_tie2.append(rider)
        if rider.run_time == time_list[2] == time_list[3]:
            riders_tie2.append(rider)
    return riders_tie2


def sort_run_results(time_list, run_list):
    """ Function sorts results and returns sorted run list."""
    time_list.sort()
    riders_tie2 = []
    riders_tie3 = []
    riders_tie4 = check_if_4_ties(time_list, run_list)
    if not riders_tie4:
        riders_tie3 = check_if_3_ties(time_list, run_list, riders_tie3)
    if not riders_tie3:
        riders_tie2 = check_if_2_ties(time_list, run_list, riders_tie2)
    if riders_tie4:
        time_list = eliminate_4_ties(time_list, riders_tie4)
    if riders_tie3:
        time_list = eliminate_3_ties(time_list, riders_tie3)
    if riders_tie2:
        time_list = eliminate_2_ties(time_list, riders_tie2)

    run_list_sorted = []
    for time in time_list:
        for rider in run_list:
            if time == rider.run_time:
                run_list_sorted.append(rider)
    return time_list, run_list, run_list_sorted


def check_bonus_points(run_list_sorted):
    """
    Function checks if rider gets bonus point.
    Rider gets one bonus point when he finished second or third and rider from his team finished one place higher
    then him.
    """
    home_sum = 0
    away_sum = 0
    home_team = None
    away_team = None
    for rider in run_list_sorted:
        if rider.run_time == run_list_sorted[1].run_time:
            if rider.team_name == run_list_sorted[0].team_name:
                rider.match_points += 2
                rider.run_bonus += 1
                rider.match_stats.append("2*")
                if rider.home:
                    home_sum += 2
                    home_team = rider.team_name
                else:
                    away_sum += 2
                    away_team = rider.team_name
        if rider.run_time == run_list_sorted[2].run_time:
            if rider.team_name == run_list_sorted[1].team_name:
                rider.match_points += 1
                rider.run_bonus += 1
                rider.match_stats.append("1*")
                if rider.home:
                    home_sum += 1
                    home_team = rider.team_name
                else:
                    away_sum += 1
                    away_team = rider.team_name
    return home_team, away_team, home_sum, away_sum


def check_regular_points(time_list, run_list, home_team, away_team, home_sum, away_sum):
    """
    Function adds regular points to riders. (3 points for 1st place, 2 points for 2nd place, 1 point for 3rd,
    0 points for 4 place).
    """
    for rider in run_list:
        try:
            if rider.run_time > 100:
                rider.match_points += 0
                if rider.bonus:
                    rider.match_stats.pop(-1)
                    if rider.match_points == 2:
                        rider.match_points -= 2
                    if rider.match_points == 1:
                        rider.match_points -= 1
            else:
                if not rider.run_bonus:
                    if rider.run_time == time_list[0] and rider.home:
                        rider.match_stats.append(3)
                        rider.match_points += 3
                        home_sum += 3
                        home_team = rider.team_name
                    if rider.run_time == time_list[0] and not rider.home:
                        rider.match_stats.append(3)
                        rider.match_points += 3
                        away_sum += 3
                        away_team = rider.team_name
                    if rider.run_time == time_list[1] and rider.home:
                        rider.match_stats.append(2)
                        rider.match_points += 2
                        home_sum += 2
                        home_team = rider.team_name
                    if rider.run_time == time_list[1] and not rider.home:
                        rider.match_stats.append(2)
                        rider.match_points += 2
                        away_sum += 2
                        away_team = rider.team_name
                    if rider.run_time == time_list[2] and rider.home:
                        rider.match_stats.append(1)
                        rider.match_points += 1
                        home_sum += 1
                        home_team = rider.team_name
                    if rider.run_time == time_list[2] and not rider.home:
                        rider.match_stats.append(1)
                        rider.match_points += 1
                        away_sum += 1
                        away_team = rider.team_name
                    if rider.run_time == time_list[3]:
                        rider.match_stats.append(0)
                        rider.match_points += 0
                else:
                    pass
        except IndexError:
            continue
    return home_team, away_team, home_sum, away_sum, time_list, run_list


def display_run_results_and_reset_run_bonuses(home_team, home_sum, away_sum, away_team, run_list_sorted):
    """ Function displays single run results and resets bonus points."""
    i = 1
    print("\t\t\t" + home_team + " " + str(home_sum) + " : " + str(away_sum) + " " + away_team + "\n")
    for rider in run_list_sorted:
        rider.bonus += rider.run_bonus
        rider.run_bonus = 0
        print(str(i) + "\t" + rider.name + " " + rider.surname + " (" + rider.team_name + ") - "
              + str(rider.run_time))
        i += 1


def assign_run_points(time_list, run_list, run_list_sorted):
    """ Function assigns run points to riders and teams in Player's matches."""
    home_team, away_team, home_sum, away_sum = check_bonus_points(run_list_sorted)
    home_team, away_team, home_sum, away_sum, time_list, run_list = check_regular_points(time_list, run_list, home_team,
                                                                                         away_team, home_sum, away_sum)
    display_run_results_and_reset_run_bonuses(home_team, home_sum, away_sum, away_team, run_list_sorted)
    return time_list, run_list


def reset_run_bonuses(run_list_sorted):
    """ Function resets run bonuses in Computer's matches."""
    for rider in run_list_sorted:
        rider.bonus += rider.run_bonus
        rider.run_bonus = 0


def comp_assign_run_points(time_list, run_list, run_list_sorted):
    """ Function assigns run points to riders and teams in Player's matches."""
    home_team, away_team, home_sum, away_sum = check_bonus_points(run_list_sorted)
    home_team, away_team, home_sum, away_sum, time_list, run_list = check_regular_points(time_list, run_list, home_team,
                                                                                         away_team, home_sum, away_sum)
    reset_run_bonuses(run_list_sorted)
    return time_list, run_list


def pick_substitute(run, substitutes, number):
    """ Function enables to pick substitute in Player's matches."""
    i = 0
    for rider1 in substitutes:
        print(str(i) + " " + str(rider1))
        i += 1
    num = int(input("\nWybierz zawodnika, który pojedzie w tym biegu (0-"
                    + str((len(substitutes) - 1)) + "):"))
    try:
        run.insert(number, substitutes[num])
        run.pop((number+1))
    except(IndexError, ValueError):
        print(" WYBIERZ NUMER Z ZAKRESU (0-" + str((len(substitutes) - 1)) + "):")
    return num, run, substitutes


def regular_substitute(run, player):
    """ Function checks if Player has any regular substitutes and enables substitution if possible."""
    substitutes = [player.match_team[5], player.match_team[6]]
    for men in run:
        try:
            if men == substitutes[0]:
                substitutes.remove(men)
            if men == substitutes[1]:
                substitutes.remove(men)
        except IndexError:
            pass
    if substitutes:
        rider = None
        print(" 1 - " + run[2].name + " " + run[2].surname + "\n 2 - "
              + run[3].name + " " + run[3].surname + "\n 3 -  Zrezygnuj ze zmiany\n")
        while rider not in [1, 2, 3]:
            rider = int(input(" Wybierz zawodnika, którego chcesz zmienić (nr 1-3)\n"))
            try:
                if rider == 1:
                    num = None
                    while num not in range(len(substitutes)):
                        num, run, substitutes = pick_substitute(run, substitutes, 2)
                if rider == 2:
                    num = None
                    while num not in range(len(substitutes)):
                        num, run, substitutes = pick_substitute(run, substitutes, 3)
                if rider == 3:
                    pass
            except(ValueError, IndexError):
                print("WYBIERZ NUMER Z ZAKRESU 1-3 !!!")
    if not substitutes:
        print("Nie ma dostępnych rezerwowych!")


def pick_tactical_substitute(run, match_list, number):
    """ Function does a tactical substitution in Player's matches."""
    i = 0
    for rider1 in match_list:
        print(str(i) + " " + str(rider1))
        i += 1
    num = int(input("Wybierz zawodnika, który pojedzie w tym biegu (0-6):"))
    try:
        run.insert(number, match_list[num])
        run.pop((number+1))
    except(IndexError, ValueError):
        print("WYBIERZ NUMER Z ZAKRESU (0-" + str(len(match_list)-1) + "):")
    return num, run, match_list


def tactical_substitute(run, player, computer):
    """
    Function checks if tactical substitution is available and if so, does it. (In speedway tactical substitute is
    possible when team is loosing by minimum 6 points).
    """
    if (player.match_points - computer.match_points) < -5:
        match_list = player.match_team[:]
        match_list.remove(run[2])
        match_list.remove(run[3])
        rider = None
        while rider not in [1, 2, 3]:
            print(" 1 - " + run[2].name + " " + run[2].surname + "\n 2 - "
                  + run[3].name + " " + run[3].surname + "\n 3 -  Zrezygnuj ze zmiany")
            rider = int(input(" Wybierz, zawodnika, którego chcesz zmienić. (1-3)\n"))
            if rider == 1:
                num = None
                while num not in range(len(match_list)):
                    num, run, match_list = pick_tactical_substitute(run, match_list, 2)
            if rider == 2:
                num = None
                while num not in range(len(match_list)):
                    num, run, match_list = pick_tactical_substitute(run, match_list, 3)
            if rider == 3:
                pass
    else:
        print(
            "Zmianę taktyczną można przeprowadzić tylko, gdy drużyna przegrywa minimum 6-cioma punktami!!!")


def single_run_menu(run, player, computer):
    """ Function displays single run menu in Player's matches."""
    choice = None
    while choice != 1:
        try:
            print("\n\t\t\t MENU BIEGU\n"
                  "1 - Jedź Bieg \n"
                  "2 - Zmiana zwykła\n"
                  "3 - Zmiana taktyczna\n")
            choice = int(input("Wybierz opcję z powyższego MENU (1-3)\n"))
            if choice == 1:
                pass
            if choice == 2:
                regular_substitute(run, player)
            if choice == 3:
                tactical_substitute(run, player, computer)
        except(ValueError, IndexError):
            print(" WYBIERZ NUMER Z ZAKRESU (1-3)!!!")
    return run
