import logging

# Configure logging format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    """
    Log an informational message
    """
    logging.info(message)


def log_error(message):
    """
    Log an error message
    """
    logging.error(message)
# New function added for dependency update
def log_warning(message):
    logging.warning(message)
    