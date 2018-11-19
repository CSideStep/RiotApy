from dataclasses import dataclass
from typing import List

def mini_series_helper(response:dict):
    if "miniSeries" in response.keys():
        r=response["miniSeries"]
        return MiniSeriesResponse(r["target"], r["wins"], r["losses"], r["progress"])
    else:
        return None

@dataclass
class ChampionRotationResponse:
    free_champion_ids:List[int]
    free_champion_ids_for_new_players:List[int]
    max_new_player_level:int

@dataclass
class ChallengerByQueuePlayerResponse:
    player_or_team_id:int
    player_or_team_name:str
    league_point:int
    rank:str
    wins:int
    losses:int
    veteran:bool
    inactive:bool
    freshBlood:bool
    hotStreak:bool

@dataclass
class ChallengerByQueueResponse:
    name:str
    tier:str
    queue:str
    leagueId:str
    entries:List[ChallengerByQueuePlayerResponse]

@dataclass
class MiniSeriesResponse:
    target:int
    wins:int
    losses:int
    progress:str

@dataclass
class LeaguePlayerResponse(ChallengerByQueuePlayerResponse):
    miniSeries:MiniSeriesResponse #or None

@dataclass
class LeagueResponse:
    name:str
    tier:str
    queue:str
    leagueId:str
    entires:List[LeaguePlayerResponse]
    