from other_functions import *


def main():
    teams = say_hello_and_pick_team()
    teams = random_draft(teams)
    next_rider(teams)
    schedule_set(teams)
    regular_season(teams)


if __name__ == '__main__':
  main()
