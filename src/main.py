from storage.file_storage import FileStorage
from storage.sql_database import DatabaseStorage
from views.main_view import __launch_ui__

if __name__ == "__main__":
    # storage = FileStorage()
    storage = DatabaseStorage()
    __launch_ui__(storage)
