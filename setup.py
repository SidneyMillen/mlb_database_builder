"""Used for initial setup. optional for now since its so simple"""
import shutil
import os.path

def main():
    if not os.path.isfile("config.py"):
        shutil.copyfile("config.example.py", "config.py")
    else:
        while True:
            choice = input("config.py already exists.\nDo you wish to overwrite with default values? [y/n]: ").lower()
            if choice in ["y", "yes"]:
                shutil.copyfile("config.example.py", "config.py")
                break
            elif choice in ["n", "no"]:
                print("cancelling operation. config.py will not be altered")
                break
if __name__ == "__main__":
    main()
