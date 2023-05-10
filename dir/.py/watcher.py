import os
import time

WATCHED_FOLDER = '/workspaces/moon'  # Ändere dies auf den Pfad deines zu überwachenden Ordners
LOG_FILE = 'log.md'   # Ändere dies auf den Pfad und den Namen deiner Log-Datei

# Überwacht den Ordner auf Änderungen und schreibt sie in das Log
def watch_folder():
    with open(LOG_FILE, 'a') as log:
        while True:
            for filename in os.listdir(WATCHED_FOLDER):
                # Überprüfe, ob das Element eine Datei ist
                if os.path.isfile(os.path.join(WATCHED_FOLDER, filename)):
                    # Überprüfe, ob die Datei seit dem letzten Durchlauf verändert wurde
                    modified_time = os.path.getmtime(os.path.join(WATCHED_FOLDER, filename))
                    if modified_time > watch_folder.last_modified.get(filename, 0):
                        # Schreibe die Änderung ins Log
                        log.write(f"{filename} wurde verändert\n")
                        watch_folder.last_modified[filename] = modified_time
            time.sleep(1)

if __name__ == '__main__':
    watch_folder.last_modified = {}
    watch_folder()


