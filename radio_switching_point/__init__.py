from otree.api import *

doc = """
Table where each row has a left/right choice,
like the strategy method.
This app enforces a single switching point
"""


class Constants(BaseConstants):
    name_in_url = 'radio_switching_point'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_side_amount = models.IntegerField(initial=10)
    switching_point = models.IntegerField()


# PAGES
class Decide(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    @staticmethod
    def vars_for_template(player):
        return dict(right_side_amounts=range(10, 21, 1))


class Results(Page):
    pass


page_sequence = [Decide, Results]
