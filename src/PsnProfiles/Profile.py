import json
from src.PsnProfiles.ProfileSummary import ProfileSummary


class Profile:
    def __init__(self, name: str, summary: ProfileSummary, recent_trophies: list, rarest_trophies: list, milestones: list, games: list, trophy_cabinet: list):
        self.name = name
        self.summary = summary
        self.recent_trophies = recent_trophies
        self.rarest_trophies = rarest_trophies
        self.milestones = milestones
        self.games = games
        self.trophy_cabinet = trophy_cabinet

    def get_name(self) -> str:
        return self.name

    def get_summary(self) -> ProfileSummary:
        return self.summary

    def get_recent_trophies(self) -> list:
        return self.recent_trophies

    def get_rarest_trophies(self) -> list:
        return self.rarest_trophies

    def get_milestones(self) -> list:
        return self.milestones

    def get_games(self) -> list:
        return self.games

    def get_trophy_cabinet(self) -> list:
        return self.trophy_cabinet

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=2)
