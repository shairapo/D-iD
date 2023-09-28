import pyglet

video_file = "/Users/zhichengu/Desktop/0.mp4"
window = pyglet.window.Window(480, 480)

player = pyglet.media.Player()
source = pyglet.media.StreamingSource()

# Load the media and queue it for playback
MediaLoad = pyglet.media.load(video_file)
player.queue(MediaLoad)

# Start playing the video
player.play()

@window.event
def on_draw():
    window.clear()
    
    if player.source and player.source.video_format:
        player.get_texture().blit(50, 50)

pyglet.app.run()