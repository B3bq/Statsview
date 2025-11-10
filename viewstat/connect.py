import os
import logging

# pure mode before mysql.connector load
os.environ["USE_PURE"] = "True"

# logs config
log_path = os.path.join(os.getenv("LOCALAPPDATA"), "Statsview")
if not os.path.exists(log_path):
    os.makedirs(log_path, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_path, "connection_error.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

logging.info("=== APP starts ===")
logging.info(f"Base path: {os.path.dirname(log_path)}")

try:
    import mysql.connector
    from mysql.connector import Error
    logging.info(f"MySQL connector load from: {mysql.connector.__file__}")
    logging.info(f"HAVE_CEXT = {getattr(mysql.connector, 'HAVE_CEXT', 'null')}")

    # jeśli jednak C-extension jest aktywne, wymuś fallback
    if getattr(mysql.connector, 'HAVE_CEXT', False):
        logging.warning("Loading C-extension MySQL – force pure python.")
        import importlib
        importlib.reload(mysql.connector)
        mysql.connector.HAVE_CEXT = False

except Exception as e:
    logging.exception(f"Error during import mysql.connector: {e}")


def connect():
    try:
        logging.info("Try to connect MySQL...")

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="base",
            use_pure=True
        )

        if connection.is_connected():
            logging.info("✅ Connected with database MySQL (pure Python mode)")
        return connection

    except Error as e:
        logging.error(f"Connection error MySQL: {e}")
        return None

    except Exception as e:
        logging.exception(f"Unexpected error: {e}")
        return None
