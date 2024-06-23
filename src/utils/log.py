from src.settings.variables import LOG_PATH, SQL_LOG_PATH
from datetime import datetime


def log(msg: str, sql: bool | None):
    """This function logs a message to the LOG_PATH file

    Args:
            msg (str): Message to write in the file
            sql (bool): If its SQL, a title will be set
    """
    current_datetime = datetime.now()
    d = current_datetime.date()
    t = str(current_datetime.hour)+":"+str(current_datetime.minute)

    path = ""

    if sql:
        path = SQL_LOG_PATH
    else:
        path = LOG_PATH

    try:
        with open(path, "a") as f:
            m = str(d)+" | "+str(t)
            if sql:
                m += " [SQL] "
            else:
                m += " [LOG] "
            m += msg
            f.writelines(m+"\n")
    except FileNotFoundError:
        print(f"FileNotFoundError: The file '{LOG_PATH}' could not be found.")
    except PermissionError:
        print(
            f"PermissionError: Permission denied when trying to access '{LOG_PATH}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
