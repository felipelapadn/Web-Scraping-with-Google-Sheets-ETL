import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import logging
from dotenv import load_dotenv
import os
load_dotenv()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
class Planilha:
    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self.SAMPLE_SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
        self.SAMPLE_RANGE_NAME = os.getenv("RANGE_NAME")
        self.logger = logging.getLogger(__name__)
    
    def carregar_credenciais(self):
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("sheets", "v4", credentials=creds)
            sheet = service.spreadsheets()
        except HttpError as err:
            self.logger.info(err)
        else:
            self.logger.info("Credenciais carregadas!")
            return sheet

    def atualizar_planilha(self, sheet, valores_para_add):
        try:
            sheet.values().update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range=self.SAMPLE_RANGE_NAME, valueInputOption="RAW",
                                        body={"values": valores_para_add}).execute()
        except HttpError as err:
            self.logger.info(err)
        else:
            self.logger.info("Planilha atualizada!")