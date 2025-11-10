import os, sys, json, logging

# making logs
log_path = os.path.join(os.getenv("LOCALAPPDATA"), "Statsview")
if not os.path.exists(log_path):
    os.makedirs(log_path, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_path, "save.log"),
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# path to save user
def get_user_save_path():
    base = os.path.join(os.getenv("LOCALAPPDATA"), "Statsview")
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "save.json")

# load data
def load_save():
    user_path = get_user_save_path()

    if os.path.exists(user_path):
        try:
            with open(user_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            logging.info(f"Load save: {user_path}")
            return data
        except Exception as e:
            logging.error(F"Error during load seve.json: {e}")

    logging.warning("save.json doesn't exist, make it")
    
    default_data = {
        "user_id": 0,
        "lang": "en"
    }

    save_data(default_data)
    return default_data

def save_data(data: dict):
    user_path = get_user_save_path()

    try:
        with open(user_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        logging.info(f"Save save.json: {user_path}")

    except Exception as e:
        logging.error(f"Error during save save.json: {e}")        