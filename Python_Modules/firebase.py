import pyrebase

class Firebase:
    """
    Firebase class that initializes the database connection and provides
    accessible 'db' and 'storage' objects for accessing the database and storage.
    """
    def __init__(self):
        api_key = "AIzaSyBWMHPeUjEqT_P6g_jrxlKC431pr2xkTaU"
        project_id = "sysc3010-project"
        database_url = "https://sysc3010-project-default-rtdb.firebaseio.com/"

        config = {
        "apiKey": api_key,
        "authDomain": "{}.firebaseapp.com".format(project_id),
        "databaseURL": database_url,
        "storageBucket": "{}.appspot.com".format(project_id)
        }

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
        self.sr = firebase.storage()