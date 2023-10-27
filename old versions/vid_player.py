import pyglet

video_file = "C:/Users/shai_/Desktop/github_Desktop/D-iD/videos-shai/0.mp4"
window = pyglet.window.Window()

player = pyglet.media.Player()
source = pyglet.media.load(video_file)
player.queue(source)
player.play()

@window.event
def on_draw():
    window.clear()
    
    if player.source and player.source.video_format:
        player.get_texture().blit(0, 0)

pyglet.app.run()