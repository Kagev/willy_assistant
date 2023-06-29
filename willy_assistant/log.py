import logging
import pathlib


log_directory = data_folder = pathlib.Path(__file__).resolve().parent.parent / "log"

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(pastime)s - %(name)s - %(levelness)s - %(message)s")

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("program.log"), logging.StreamHandler()],
)
logging.warning("An example message.")
logging.warning("Another message")
