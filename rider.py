class Rider(object):
    """ Representation of speedway rider."""
    def __init__(self, name, surname, total_skills, visible=False, match_runs=0, match_points=0,
                 match_falls=0, match_defects=0):
        self.name = name
        self.surname = surname
        self.total_skills = total_skills
        self.visible = visible
        self.team_name = " "
        self.match_runs = match_runs
        self.match_points = match_points
        self.match_stats = []
        self.match_falls = match_falls
        self.match_defects = match_defects
        self.overall_runs = 0
        self.overall_points = 0
        self.overall_bonuses = 0
        self.overall_defects = 0
        self.overall_falls = 0
        self.run_time = 0
        self.home = False
        self.run_bonus = 0
        self.bonus = 0

    def skills(self):
        """ Method shows skills when rider's stats aren't visible."""
        skill = None
        if self.total_skills > 140:
            skill = "Klasa światowa"
        elif self.total_skills in range(130, 141):
            skill = "Bardzo dobre"
        elif self.total_skills in range(100, 130):
            skill = "Dobre"
        return skill

    def __str__(self):
        """ Rider's string representation."""
        if self.visible:
            rep = self.name + " " + self.surname + (23-self.name_length)*" " + " Umiejętności: " \
                  + str(self.total_skills)
        else:
            rep = self.name + " " + self.surname + (23-self.name_length)*" " + " Umiejętności: " + self.skills()
        return rep

    def is_visible(self):
        """
        Method changes rider's skills visibility. When Player picks rider to his team sees exactly how many skill points
        rider has. Player can't see another teams direct riders skills.
        """
        self.visible = not self.visible

    @property
    def average(self):
        """ Method counts rider's points average per run."""
        try:
            average = (self.overall_points + self.overall_bonuses)/self.overall_runs
        except ZeroDivisionError:
            average = 0
        return average

    @property
    def name_length(self):
        """ Method counts length of full rider's info to align stats."""
        length = len(self.name) + len(self.surname) + len(self.team_name)
        return length

    def add_and_remove_stats(self):
        """ Method transforms match stats into overall stats."""
        self.overall_runs += self.match_runs
        self.match_runs = 0
        self.overall_points += self.match_points
        self.match_points = 0
        self.overall_falls += self.match_falls
        self.match_falls = 0
        self.overall_defects += self.match_defects
        self.match_defects = 0
        self.overall_bonuses += self.bonus
        self.bonus = 0
        self.match_stats = []

    def show_overall_stats(self):
        """ Method shows rider's actual season stats."""
        print(self.name + " " + self.surname + " (" + self.team_name + ")" + (33-self.name_length)*" " + " Biegów: "
              + str(self.overall_runs)
              + " Pkt: " + str(self.overall_points) + " Bonus: " + str(self.overall_bonuses) + " Śr: "
              + str(round(self.average, 2)))
