import logging


def setup_logging():
    """
    Sets up the logging configuration for the Botzilla application.

    This function configures the logging to use a specific format that includes
    the timestamp and the log message. The logging level is set to INFO.

    Returns:
        logging.Logger: A logger instance with the name 'Botzilla'.
    """
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    return logging.getLogger("Botzilla")
