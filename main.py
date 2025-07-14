import os
import shutil
import psutil
import subprocess
import platform
import tempfile

def clean_temp():
	temp_path = tempfile.gettempdir()
	if not os.path.exists(temp_path):
		print(" Temp folder not found. ")
		return

	deleted = 0
	skipped = 0

	for file in os.listdir(temp_path):
			full_path = os.path.join(temp_path, file)
			try: 
				if os.path.isfile(full_path) or os.path.islink(full_path):
					os.unlink(full_path)
					deleted += 1
				elif os.path.isdir(full_path):
					shutil.rmtree(full_path)
					deleted += 1
			except:
				skipped += 1
	print(f"Deleted: {deleted}, skipped (locked): {skipped}")

def show_sys_info():
	print(" CPU Usage: " , psutil.cpu_percent(), " % ")
	print(" RAM Usage: " , psutil.virtual_memory().percent, " % ")
	print(" Disk Usage: " , psutil.disk_usage('c:\\').percent, " % ")
	print(" OS: ", platform.system() , platform.release())

def main():
    while True:
        print("\n--- Windows Automation Tool ---")
        print("1. Clean Temp Files")
        print("2. Show System Info")
        print("3. Backup Documents")
        print("4. Open Task Manager")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            clean_temp()
        elif choice == "2":
            show_sys_info()
        elif choice == "3":
            backup_documents()
        elif choice == "4":
            open_task_manager()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
	main()