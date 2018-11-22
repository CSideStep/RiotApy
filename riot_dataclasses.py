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
    league_points:int
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

@dataclass 
class LeagueByPlayerResponse:
    queue_type:str
    hot_streak:bool
    wins:int
    losses:int
    veteran:bool
    player_or_team_id:int
    league_name:str
    player_or_team_name:str
    inactive:bool
    rank:str
    fresh_blood:bool
    league_id:str
    tier:str
    league_points:int

@dataclass
class LeaguesByPlayerResponse:
    leagues:List[LeagueByPlayerResponse]

@dataclass
class TranslationResponse:
    locale:str
    content:str
    updated_at:str

@dataclass
class MessageResponse:
    severity:str
    author:str
    created_at:str
    translation:List[TranslationResponse]
    updated_at:str
    content:str
    id:str

@dataclass
class IncidentResponse:
    active:bool
    created_at:str
    id:int
    updates:List[MessageResponse]

@dataclass
class ServiceResponse:
    status:str
    incidents:List[IncidentResponse]
    name:str
    slug:str

@dataclass
class ShardStatusResponse:
    name:str
    region_tag:str
    hostname:str
    services:List[ServiceResponse]
    slug:str
    locales:List[str]