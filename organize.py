import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "PDFs": [".pdf"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"]
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist!")
        return

    # Create category folders
    for category in FILE_TYPES.keys():
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

    others_path = os.path.join(folder_path, "Others")
    os.makedirs(others_path, exist_ok=True)

    # Scan files in folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()

        moved = False
        for category, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, category, filename))
                print(f"Moved: {filename} → {category}/")
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(others_path, filename))
            print(f"Moved: {filename} → Others/")

    print("\n🎉 All files organized successfully!")


# Run script
if __name__ == "__main__":
    folder = input("Enter folder path to organize: ")
    organize_folder(folder)
