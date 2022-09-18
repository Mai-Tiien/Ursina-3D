from ursina import *
from memory import *
    
class Player(FrameAnimation3d):
    def __init__(self, position = (0, 0, 2)):
        super().__init__(
            'access//run//run_', 
            texture='texture/fam.png',
            frame_times=140,
            fps=80,
            loop=True,
            autoplay=False,
            position=position,
        )   
        self.pause 
        
        self.Tree = Entity(
            model = 'model/lowpolytree.obj',
            position = (4, 2.6, 2),
            scale = (2, 2, 2),
        ) 
        
        self.ed = EditorCamera(rotation_smoothing=10, enabled=1, rotation=(30,30,0))
        
    def input(self, key):
        if held_keys['w'] or held_keys['s'] or held_keys['d'] or held_keys['a']:
            invoke(self.resume)
        if held_keys['n']:
            invoke(self.pause)    
            # cam.speed = 5  
        elif key == 'v':
            self.position = (0, 0, 2)
        elif key == 'q':
            self.position = (0, 0, -0.5)



class Ground(Entity):       
    def __init__(self):        
        self.ground = Entity(
            model='plane', 
            collider='box', 
            scale=200, 
            texture='grass', 
            texture_scale=(4,4)
        )                       
    
def update():
    if held_keys['escape']:
        application.quit()
    # if held_keys['shift']:
    #     cam.speed = 10
    # if not held_keys['shift']:
    #     cam.speed = 5    
               
        
    
if __name__ == '__main__':
    app = Ursina()
    
    window.title = "Test"
    window.borderless = True
    window.fullscreen = True
    window.exit_button.visible = False
    window.fps_counter.enabled = True
    
    # cam = FirstPersonController()
    # cam.gravity = 1
    # cam.jump_height = 3
    
    Player()
    Ground()
    Sky()
    MemoryCounter()
    app.run()