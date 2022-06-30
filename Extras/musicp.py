import os
def music():
    music_dir= 'C:\\Users\\R D\\Music\\Attitude'
    song = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,song[1]))