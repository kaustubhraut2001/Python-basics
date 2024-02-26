

import pymongo

# Connect to the MongoDB, change the connection string per your MongoDB environment

from dotenv import load_dotenv
import os
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
print(MONGO_URI)


client = pymongo.MongoClient(MONGO_URI)
db = client["learning"]

# Create a new collection
videos = db['videos']

def add_video():
    title = input("Enter the title of the video: ")
    url = input("Enter the url of the video: ")
    duration = int(input("Enter the duration of the video: "))
    videos.insert_one({
        "title": title,
        "url": url,
        "duration": duration
    })
    print("Video added successfully")
    return


def delete_video():
    title = input("Enter the title of the video to delete: ")
    result = videos.delete_one({"title":
        title})
    if result.deleted_count == 0:
        print("Video not found")
        return
    else:
        print("Video deleted successfully")
        return


def edit_video():
    title = input("Enter the title of the video to edit: ")
    new_title = input("Enter the new title of the video: ")
    new_url = input("Enter the new url of the video: ")
    new_duration = input("Enter the new duration of the video: ")
    result = videos.update_one({"title": title}, {"$set": {
        "title": new_title,
        "url": new_url,
        "duration": new_duration
    }})
    if result.modified_count == 0:
        print("Video not found")
        return
    else:
        print("Video edited successfully")
        return

def getallvideoes():
    for video in videos.find():
        print(f"Title: {video['title']}, URL: {video['url']}, Duration: {video['duration']}")
    if not videos.count_documents({}):
        print("No videos found")
        return
    

def main():
    print("Welcome to the Youtube Video Manager")
    print("1. Add a video")
    print("2. Delete a video")
    print("3. Edit a video")
    print("4. View all videos")
    print("5. Exit")

    choice = (input("Enter your choice: "))
    if choice == "1":
        add_video()
        
    elif choice == "2":
        delete_video()
        
    elif choice == "3":
        edit_video()
        
        
    elif choice == "4":
        getallvideoes()
       
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()