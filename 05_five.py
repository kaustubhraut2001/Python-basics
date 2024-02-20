# Youtube Video Manager

videos = []

def add_video():
    title = input("Enter the title of the video: ")
    url = input("Enter the url of the video: ")
    duration = input("Enter the duration of the video: ")
    videos.append({
        "title": title,
        "url": url,
        "duration": duration
    })
    print("Video added successfully")


def delete_video():
    title = input("Enter the title of the video to delete: ")
    for video in videos:
        if video["title"] == title:
            videos.remove(video)
            print("Video deleted successfully")
            return
    print("Video not found")


def edit_video():
    title = input("Enter the title of the video to edit: ")
    for video in videos:
        if video["title"] == title:
            new_title = input("Enter the new title of the video: ")
            new_url = input("Enter the new url of the video: ")
            new_duration = input("Enter the new duration of the video: ")
            video["title"] = new_title
            video["url"] = new_url
            video["duration"] = new_duration
            print("Video edited successfully")
            return
    print("Video not found")


def view_videos():
    for video in videos:
        print(f"Title: {video['title']}, URL: {video['url']}, Duration: {video['duration']}")
    if not videos:
        print("No videos found")
    




def main():
    print("Welcome to the Youtube Video Manager")
    print("1. Add a video")
    print("2. Delete a video")
    print("3. Edit a video")
    print("4. View all videos")
    print("5. Exit")

    choice = (input("Enter your choice: "))
    print(choice)
    if choice == "1":
        add_video()
    elif choice == "2":
        delete_video()
    elif choice == "3":
        edit_video()
    elif choice == "4":
        view_videos()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")

    
if __name__ == "__main__":
    main()