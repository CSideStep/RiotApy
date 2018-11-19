from requests import get
from riot_dataclasses import *
class RiotAccess:

    def __init__(self, key:str, server:str):
        self.key=key
        self.server=server
        self.riot_champion:RiotChampion=RiotChampion(key, server)
        self.riot_league:RiotLeague=RiotLeague(key, server)
        self.riot_status:RiotStatus=RiotStatus(key, server)
        self.riot_match:RiotMatch=RiotMatch(key, server)
        self.riot_spectator:RiotSpectator=RiotSpectator(key, server)
        self.riot_summoner:RiotSummoner=RiotSummoner(key, server)
        self.riot_third_party_code:RiotThirdPartyCode=RiotThirdPartyCode(key, server)

class RiotApi:

    def __init__(self, key:int, server:str):
        self.key=key
        self.server=server
   
class RiotChampion(RiotApi):

    def champ_rotation(self, server:str=None):
        server=(server or self.server)
        response = get(f"https://{server}.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={self.key}").json()
        return ChampionRotationResponse(response["freeChampionIds"], response["freeChampionIdsForNewPlayers"], response["maxNewPlayerLevel"])

class RiotLeague(RiotApi):

    def challenger_league_by_queue(self, queue:str, server:str=None):
        server=(server or self.server)
        response = get(f"https://{server}.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/{queue}?api_key={self.key}").json()
        players = [ChallengerByQueuePlayerResponse(player["playerOrTeamId"],
                                                   player["playerOrTeamName"],
                                                   player["leaguePoints"],
                                                   player["rank"],
                                                   player["wins"],
                                                   player["losses"],
                                                   player["veteran"],
                                                   player["inactive"],
                                                   player["freshBlood"],
                                                   player["hotStreak"])
                                                   for player in response["entries"]]
        return ChallengerByQueueResponse(response["name"], response["tier"], response["queue"], response["leagueId"], players)

    def league_by_league_id(self, id:str, server:str=None):
        server = (server or self.server)
        response = get(f"https://{self.server}.api.riotgames.com/lol/league/v3/leagues/{id}?api_key={self.key}").json()
        players = [LeagueByLeagueIdPlayerResponse(player["playerOrTeamId"],
                                                   player["playerOrTeamName"],
                                                   player["leaguePoints"],
                                                   player["rank"],
                                                   player["wins"],
                                                   player["losses"],
                                                   player["veteran"],
                                                   player["inactive"],
                                                   player["freshBlood"],
                                                   player["hotStreak"],
                                                   mini_series_helper(player))
                                                   for player in response["entries"]]
        return LeagueByLeagueIdResponse(response["name"], response["tier"], response["queue"], response["leagueId"], players)

    def master_league_by_queue(self, queue, server:str=None):
        server = (server or self.server)
        

    def position_by_summoner_id(self, summoner_id:int):
        pass

class RiotStatus(RiotApi):

    def shard_data(self):
        pass

class RiotMatch(RiotApi):

    def match_by_match_id(self, match_id:int):
        pass
    
    def match_list_by_account_id(self, account_id:int):
        pass

    def timeline_by_match_id(self, match_id:int):
        pass

    #tournament stuff is locked
    #tournament stuff ist locked

class RiotSpectator(RiotApi):

    
    def active_game_by_summoner_id(self, summoner_id):
        pass

    def featured_games(self):
        pass

class RiotSummoner(RiotApi):
    
    def summoner_by_account_id(self, account_id:int):
        pass

    def summoner_by_name(self, summoner_name:str):
        pass

    def summoner_by_summoner_id(self, summoner_id:int):
        pass

class RiotThirdPartyCode(RiotApi):

    def third_party_code_by_summoner_id(self, summoner_id):
        pass
