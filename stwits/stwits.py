import json
import requests
from datetime import date


class StocktwitsAPI:
    '''
    Python client package for Stocktwits API - https://api.stocktwits.com/developers/docs/api \n
    Author: `Mark Yosef Joseph` \n
    GitHub: https://github.com/mark1yo/stwits \n
    License: `MIT` \n
    \----- \n
    Supported APIs: \n
    - Sync
    - Streams 
    - WatchLists
    - Trending

    Unsupported APIs: \n
    - Search, Messages, Graph, Friendships, Blocks, Mutes, Account, Deletions
    \----- \n
    1 - This python package is NOT an official package of www.stocktwits.com
    2 - Only NON-partner level APIs are supported
    3 - Authentication is required to use this API due to rate and functioanality limits
    How to get an access token and use this API tutorial:
    4 - Visit the official API site for more information about: \n
    API Methods, Authentication, Rate Limiting, Parameters, Responses, Error Codes, etc \n
    https://api.stocktwits.com/developers/docs/api
    '''

    def __init__(self, access_token: str):
        self.api_url = 'https://api.stocktwits.com/api/2/'
        self.access_token = access_token

    def __get_req__(self, path: str, **kwargs: dict):
        kwargs.update({'access_token': self.access_token})
        url: str = f'{self.api_url}{path}.json'
        res = requests.get(url, kwargs).json()
        if 200 != int(res['response']['status']):
            raise BaseException(f'Error with request: {url}, response: {res}')
        return res

    def __post_req__(self, path: str, **kwargs: dict):
        kwargs.update({'access_token': self.access_token})
        url: str = f'{self.api_url}{path}.json'
        res = requests.post(url, kwargs).json()
        if 200 != int(res['response']['status']):
            raise BaseException(f'Error with request: {url}, response: {res}')
        return res

    # Sync
    def sync_sectores_and_industries(self, csv_file_path: str):
        '''Download and save a .csv file with all the sectors and industries'''
        res = requests.get('https://api.stocktwits.com/sectors/StockTwits-sectors-industries.csv')
        with open(csv_file_path, 'w') as file:
            file.write(res.content)

    
    def sync_symbols(self, csv_file_path: str):
        '''Download and save a .csv file with all stocktwits symbols/tickers (Updated daily).'''
        today = date.today().strftime('%Y-%m-%d') 
        res = requests.get(f'https://api.stocktwits.com/symbol-sync/{today}.csv')
        with open(csv_file_path, 'w') as file:
            file.write(res.content)

    # Streams
    def stream_user(self, user: str, since: int = 0, maximum: int = 0, limit: int = 30) -> list:
        '''Returns the most recent 30 messages for the specified user (id or name).'''
        res = self.__get_req__(
            f'streams/user/{user}', since=since, max=maximum, limit=limit)
        return res['messages']

    def stream_symbol(self, symbol: str, since: int = 0, maximum: int = 0, limit: int = 30) -> list:
        '''Returns the most recent 30 messages for the specified symbol.'''
        res = self.__get_req__(
            f'streams/symbol/{symbol}', since=since, max=maximum, limit=limit)
        return res['messages']

    def stream_watchlist(self, watchlist: int, since: int = 0, maximum: int = 0, limit: int = 30) -> list:
        '''Returns the most recent 30 messages for the specified watch list for the authenticating user.'''
        res = self.__get_req__(
            f'streams/watchlist/{watchlist}', since=since, max=maximum, limit=limit)
        return res['messages']

    def stream_trending(self, since: int = 0, maximum: int = 0, limit: int = 30) -> list:
        '''Returns the most recent 30 messages with trending symbols in the last 5 minutes.'''
        res = self.__get_req__(
            f'streams/trending', since=since, max=maximum, limit=limit)
        return res['messages']

    # WatchLists
    def watchlists(self) -> list[tuple]:
        '''Returns a list of private watch lists for the authenticating user.'''
        res = self.__get_req__(f'watchlists')
        return [(int(x['id']), x['name']) for x in res['watchlists']]

    def watchlist_create(self, name: str) -> int:
        '''Create a private watch list for the authenticating user.'''
        res = self.__post_req__(f'watchlists/create', name=name)
        return int(res['watchlist']['id'])

    def watchlist_update(self, watchlist_id: int, new_name: str) -> list[tuple]:
        '''Update the name of the specified watch list.'''
        res = self.__post_req__(
            f'watchlists/update/{watchlist_id}', name=new_name)
        return (int(res['watchlist']['id']), res['watchlist']['name'])

    def watchlist_delete(self, watchlist_id: int) -> int:
        '''Delete the specified watch list.'''
        res = self.__post_req__(f'watchlists/destroy/{watchlist_id}')
        return int(res['watchlist']['id'])

    def watchlist_show_symbols(self, watchlist_id: int) -> list[str]:
        '''Returns the the list of ticker symbols in a specified watch list for the authenticating user.'''
        res = self.__get_req__(f'watchlists/show/{watchlist_id}')
        return [str(x['symbol']) for x in res['watchlist']['symbols']]

    def watchlist_add_symbols(self, watchlist_id: int, symbols: str):
        '''Add a ticker symbol or list of symbols to a specified watch list.'''
        self.__post_req__(
            f'watchlists/{watchlist_id}/symbols/create', symbols=symbols)

    def watchlist_remove_symbols(self, watchlist_id: int, symbols: str):
        '''Remove a symbol or list of symbols from the specified watch list.'''
        self.__post_req__(
            f'watchlists/{watchlist_id}/symbols/destroy', symbols=symbols)

    # Trending
    def trending_symbols(self) -> list[tuple]:
        '''Returns a list of all the trending symbols at the moment requested. 
        Trending symbols include equties and non-equities like futures and forex. 
        These are updated in 5-minute intervals.'''
        res = self.__get_req__(f'trending/symbols')
        return [(x['symbol'], x['title']) for x in res['symbols']]

    def trending_equities(self) -> list[tuple]:
        '''Returns a list of all the trending equity symbols at the moment requested. 
        Trending equities have to have a price over $5. 
        These are updated in 5 minute intervals.'''
        res = self.__get_req__(f'trending/symbols/equities')
        return [(x['symbol'], x['title']) for x in res['symbols']]
