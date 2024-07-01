import requests
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import pandas as pd


class Controller:
    CLIENT_ID = '129494'
    CLIENT_SECRET = 'fa2cddf4f38109f29041276a50761e20c62925e9'
    REDIRECT_URI = 'http://localhost:8080'
    TOKEN_URL = 'https://www.strava.com/oauth/token'
    AUTH_URL = (
        f"https://www.strava.com/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=activity:read"
    )

    def __init__(self):
        webbrowser.open(self.AUTH_URL)
        self.server = HTTPServer(('localhost', 8080), self.RequestHandler)
        self.server.controller = self
        self.server.handle_request()

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query_components = urlparse.parse_qs(urlparse.urlparse(self.path).query)
            if 'code' in query_components:
                authorization_code = query_components['code'][0]
                self.server.controller.exchange_token(authorization_code)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Authorization complete. You can close this window.')

    def exchange_token(self, authorization_code):
        data = {
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'code': authorization_code,
            'grant_type': 'authorization_code'
        }
        response = requests.post(self.TOKEN_URL, data=data)
        if response.status_code == 200:
            token_info = response.json()
            access_token = token_info['access_token']
            refresh_token = token_info['refresh_token']
            # print(f"Access Token: {access_token}")
            # print(f"Refresh Token: {refresh_token}")
            self.get_activities(access_token)
        else:
            print(f"Fehler: {response.status_code}")
            print(response.json())

    def get_activities(self, access_token):
        BASE_URL = 'https://www.strava.com/api/v3/athlete/activities'
        params = {
            'before': int(time.time()),
            'after': 0,
            'page': 1,
            'per_page': 50
        }
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(BASE_URL, headers=headers, params=params)
        if response.status_code == 200:
            activities = response.json()
            self.save_to_dataframe(activities)
        else:
            print(f"Fehler: {response.status_code}")
            print(response.json())

    def save_to_dataframe(self, activities):
        # Speichern der Aktivitäten in ein DataFrame
        df = pd.DataFrame(activities)
        print("DataFrame:")
        print(df.shape)
        print(df.columns)

        df.to_csv('strava_activities.csv', index=False)



if __name__ == '__main__':
    controller = Controller()
