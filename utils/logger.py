
import logging
from datetime import datetime
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Generate a unique filename for every session
filename = "chatbot_session_" + datetime.now().strftime("session_%Y%m%d_%H%M%S.txt")
log_path = os.path.join("logs", filename)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(log_path, encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger("MyApp")
