import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
import requests

class SpotifyPlaylistWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Spotify Playlist")
        self.setGeometry(0, 0, 800, 600)

        layout = QVBoxLayout(self)

        # Replace with your Spotify API credentials
        client_id = "2ab51ce805e346e4918ac807944f83d6"
        client_secret = "3d49a513971c43878190bf27e3dcc433"

        # Set up Spotify API authentication
        token_url = "https://accounts.spotify.com/api/token"
        data = {"grant_type": "client_credentials"}
        auth = (client_id, client_secret)

        response = requests.post(token_url, data=data, auth=auth)
        access_token = response.json().get("access_token")

        # Replace with the actual Spotify playlist ID
