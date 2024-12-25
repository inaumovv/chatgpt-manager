import requests
from speechkit import configure_credentials, model_repository
from speechkit.common.utils import creds
from speechkit.stt import AudioProcessingType


def transcrible(url: str):
    configure_credentials(
        yandex_credentials=creds.YandexCredentials(
            api_key='AQVNxDLYvobHrFXWB5rS2vD7BJAyZixTgLZ7fPKI'
        )
    )
    response = requests.get(url, stream=True)
    model = model_repository.recognition_model()
    model.model = 'general:rc'
    model.language = 'auto'
    model.audio_processing_type = AudioProcessingType.Full

    result = model.transcribe(response.content)
    for c, res in enumerate(result):
        text = res.normalized_text
        return text
