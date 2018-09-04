import copy


class Team(object):
    """ Representation of speedway team."""
    def __init__(self, team_name, draft_number=0, wins=0, draws=0, loses=0, bonus=0, differential=0, home=False,):
        self.team_name = team_name
        self.draft_number = draft_number
        self.riders = []
        self.wins = wins
        self.draws = draws
        self.loses = loses
        self.bonus = bonus
        self.differential = differential
        self.home = home
        self.match_team = []
        self.nominee = []
        self.two_legged_tie = 0
        self.scores = []
        self.human = False
        self.deuce = False

    def __str__(self):
        rep = self.team_name
        return rep

    @property
    def match_points(self):
        """ Method counts actual team's match points."""
        total = 0
        for rider in self.match_team:
            total += rider.match_points
        return total

    @property
    def total_points(self):
        """ Method counts team overall wins/losses points."""
        total_points = ((self.wins * 2) + self.draws + self.bonus)
        return total_points

    @property
    def team_name_length(self):
        """ Method counts letters in team's name in order to align stats."""
        length = len(self.team_name)
        return length

    def show_team(self):
        """ Method shows team's squad."""
        print(" ZESPÓŁ: " + self.team_name + ". Wybierz skład meczowy!")
        num = 0
        for rider in self.riders:
            print(num, " ", rider)
            num += 1

    def pick_match_team(self):
        """ Method enables Player to pick match team from team squad. Match team has 7 riders, team squad - 8 riders."""
        team = copy.copy(self.riders)
        match_team = []
        self.show_team()
        while len(match_team) < 7:
            try:
                number = int(input("\nWybierz zawodnika, który pojedzie w meczu (łącznie siedmiu):"))
                match_team.append(team[number])
                team.pop(number)
                num1 = 0
                print("Zawodnicy wyznaczeni do meczu: ")
                for rider in match_team:
                    print(rider)

                print("\nZawodnicy do wyboru:")
                for rider in team:
                    print(num1, " ", rider)
                    num1 += 1
            except (ValueError, IndexError):
                print("Musisz wpisać CYFRĘ (0 - " + str(len(team)-1) + ")! Wybierz numer zawodnika, " +
                      "którego chcesz wybrać do zespołu")
        print("Brawo, wybrałeś skład meczowy")
        self.match_team = match_team

    def pick_nominee(self):
        """ Method enables Player to pick riders for runs 14 and 15 (nominee runs)."""
        team = copy.copy(self.match_team)
        nominee = []
        self.show_match_team()
        i = 0
        while i < 2:
            try:
                number = int(input("\nWybierz zawodnika, który pojedzie w biegu 14"))
                nominee.append(team[number])
                i += 1
                team.pop(number)
                num1 = 0
                print("Zawodnicy do wyboru:")
                for rider in team:
                    print(num1, " ", rider)
                    num1 += 1
            except (ValueError, IndexError):
                print(" Wpisz liczbę z właściego zakresu !!!")

        while i < 4:
            try:
                number = int(input("\nWybierz zawodnika, który pojedzie w biegu 15"))
                nominee.append(team[number])
                i += 1
                team.pop(number)
                num1 = 0
                print("Zawodnicy do wyboru:")
                for rider in team:
                    print(num1, " ", rider)
                    num1 += 1
            except (ValueError, IndexError):
                print(" Wpisz liczbę z właściego zakresu !!!")

        print("Brawo, wybrałeś skład do biegów nominowanych \n Bieg 14: \n"
              + nominee[0].name + " " + nominee[0].surname + "\n" + nominee[1].name + " " + nominee[1].surname +
              "\n Bieg 15: \n"
              + nominee[2].name + " " + nominee[2].surname + "\n" + nominee[3].name + " " + nominee[3].surname)
        self.nominee = nominee


    def comp_next_rider(self, player_list):
        """
        Method enables Computer to pick rider to it's team by simple rule.
        Method assigns rider to one of three lists by rider skills (world class, very good, good)
        Computer picks first rider from the list with best skills.
        """
        world_class = []
        very_good = []
        good = []
        for player in player_list:
            if player.skills() == "Klasa światowa":
                world_class.append(player)
            if player.skills() == "Bardzo dobre":
                very_good.append(player)
            else:
                good.append(player)
        if world_class:
            self.riders.append(world_class[0])
            for player in player_list:
                if player == world_class[0]:
                    player_list.remove(player)
        else:
            if very_good:
                self.riders.append(very_good[0])
                for player in player_list:
                    if player == very_good[0]:
                        player_list.remove(player)
            else:
                self.riders.append(good[0])
                for player in player_list:
                    if player == good[0]:
                        player_list.remove(player)

    def comp_pick_team(self):
        """ Method chooses computer's match team."""
        riders_sum = []
        riders_copy = copy.copy(self.riders)
        for rider in riders_copy:
            suma = rider.total_skills
            riders_sum.append(suma)
        riders_sum = sorted(riders_sum)
        riders_sum.pop(0)
        match_team = []
        for rider in riders_copy:
            if rider.total_skills in riders_sum:
                match_team.append(rider)
            else:
                continue
        self.match_team = match_team

    def comp_pick_nominee(self):
        """ Method chooses computer's squad for nominee runs."""
        best_riders = []
        riders_copy = copy.copy(self.match_team)
        for rider in riders_copy:
            suma = rider.total_skills
            best_riders.append(suma)
        very_best_riders = sorted(best_riders)
        nominee = []
        for rider in self.match_team:
            if rider.total_skills == very_best_riders[-4]:
                nominee.append(rider)
        for rider in self.match_team:
            if rider.total_skills == very_best_riders[-3]:
                nominee.append(rider)
        for rider in self.match_team:
            if rider.total_skills == very_best_riders[-2]:
                nominee.append(rider)
        for rider in self.match_team:
            if rider.total_skills == very_best_riders[-1]:
                nominee.append(rider)
        self.nominee = nominee

    def show_match_team(self):
        """ Method shows match team."""
        print("\nSkład meczowy zespołu ", self.team_name + " :\n")
        num = 0
        for rider in self.match_team:
            print(num, " ", rider)
            num += 1

    def show_team_riders_stats(self):
        """ Method shows team's riders stats."""
        print(" IMIĘ I NAZWISKO; \t B - ilość biegów\t P - Punkty Ogółem\t Śr - Średnia P/B")
        for rider in self.riders:
            rider.show_overall_stats()

    def show_team_stats(self, position):
        """ Method shows team's overall stats."""
        print(str(position) + ". " + self.team_name + (18-self.team_name_length)*" " + "Małe pkt: "
              + str(self.differential)
              + " PKT: " + str(self.total_points))

    def check_if_second_game(self, rival):
        """
        Method checks if two teams are competing for the first or second time during actual season.
        This is needed to add possible bonus point after match. Team with higher sum of small points in two-legged tie
        gets one overall bonus point.
        """
        second_game = False
        number = None
        for num in range(len(self.scores)):
            if self.scores[num][0] == rival.team_name:
                second_game = True
                number = num
        return second_game, number

    def add_match_stats(self, rival):
        """ Method adds match points to team's stats and checks possible bonus point."""
        one_score = []
        if self.scores:
            second_game, number = self.check_if_second_game(rival)
            if second_game:
                one_match_differential = self.match_points - rival.match_points
                if one_match_differential > 0:
                    self.wins += 1
                if one_match_differential == 0:
                    self.draws += 1
                if one_match_differential < 0:
                    self.loses += 1
                if one_match_differential + self.scores[number][1] > 0:
                    self.bonus += 1
                if one_match_differential + self.scores[number][1] == 0:
                    if self.differential > rival.differential:
                        self.bonus += 1
                one_score.append(rival.team_name)
                one_score.append(one_match_differential)
                self.scores.append(one_score)
                self.differential += one_match_differential
            else:
                one_match_differential = self.match_points - rival.match_points
                if one_match_differential > 0:
                    self.wins += 1
                if one_match_differential == 0:
                    self.draws += 1
                else:
                    self.loses += 1
                one_score.append(rival.team_name)
                one_score.append(one_match_differential)
                self.scores.append(one_score)
                self.differential += one_match_differential
        else:
            one_match_differential = self.match_points - rival.match_points
            if one_match_differential > 0:
                self.wins += 1
            if one_match_differential == 0:
                self.draws += 1
            else:
                self.loses += 1
            one_score.append(rival.team_name)
            one_score.append(one_match_differential)
            self.scores.append(one_score)
            self.differential += one_match_differential

    def reset_match_team(self):
        """ Method adds rider's match stats to overall stats and reset current match stats."""
        self.match_team = []
        for rider in self.riders:
            rider.add_and_remove_stats()