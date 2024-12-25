from src.bot.utils.keyboards import Keyboards
from src.config import settings
from src.services.openai_worker import OpenAIWorker

openai_worker: OpenAIWorker = OpenAIWorker(
    'gpt-3.5-turbo',
    'user_history.json',
    settings.OPENAI_API_KEY,
    settings.OPENAI_ORGANIZATION,
    settings.OPENAI_PROJECT
)

keyboards: Keyboards = Keyboards()
