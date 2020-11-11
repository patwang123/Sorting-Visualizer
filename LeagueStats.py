from RiotAccessConstants import *
import requests
class LeagueStats:
	def __init__(self,api_key,region='North America',account_region = 'Americas'):
		self.api_key = api_key
		self.region = REGION[region]
		self.account_region = ACCOUNT_REGION[account_region]
	def request(self, url, params = {}, region=0):
		if not region:
			region = self.region
		for k,v in params:
			args[key] = v
		response = requests.get(
					URL['base'].format(
						region=region,
						url=url,
						api_key=self.api_key))
		return response.json()

	#account-v1
	def get_account_by_riot_id(self,game_name,tagline):
		url = URL['account_by_riot_id'].format(
				game_name = game_name,
				tagline = tagline)
		return self.request(url,region=self.account_region)
	def get_account_by_puuid(self,puuid):
		url = URL['account_by_puuid'].format(
				puuid = puuid)
		return self.request(url,region=self.account_region)
	def get_account_active_shard(self,game,puuid):
		url = URL['account_active_shard'].format(
				game=game,
				puuid=puuid)
		return self.request(url,region=self.account_region)

	#champion-v3
	def get_champion_rotations(self):
		url = URL['champion_rotations']
		return self.request(url)

	#summoner-v4 api
	def get_summoner_by_name(self,summonerName):
		url = URL['summoner_by_name'].format(
				summonerName=summonerName)
		return self.request(url)
	def get_summoner_by_puuid(self,puuid):
		url = URL['summoner_by_puuid'].format(
				encryptedPUUID=puuid)
		return self.request(url)
	def get_summoner_by_summonerID(self,summonerID):
		url = URL['summoner_by_summoner_ID'].format(
				encryptedSummonerId = summonerID)
		return self.request(url)
	def get_summoner_by_account(self,accountID):
		url = URL['summoner_by_summoner_ID'].format(
				encryptedAccountId = accountID)
		return self.request(url)

