$ renpy.include("Helpers/glitch.rpy")
$ renpy.include("Helpers/transforms.rpy")

init -1 python:
    class ParticleSystem:
        def __init__(self,layer,image,density,speed,duration):
            self.layer = layer
            self.image = image
            self.density = density
            self.speed = speed 
            self.duration = duration
        
        def create_particles(self):
            particles = []
            for i in range(self.density):
                particles.append(
                    Particle(self.layer, self.image, x=100, y=100, alpha=255, 
                            sx=1, sy=1, linear=((-50, -50), (50, 50)), dx=0, dy=self.speed)
                )
            return particles

init python:
    class Chapter:
        def __init__(self,ch_number):
            self.ch_number = ch_number
            self.ch_title = f"Chapter {ch_number}"
        
        def start(self):
            renpy.call(f"ch_{self.ch_number}")
    
    def show_particles(particle_system):
        for particle in particle_system.create_particles():
            yield particle

label start:

    scene bg whitehouse:
        zoom 1.5

    image eileen glitched:
        At("eileen happy",glitch)
        pause 0.2
        At("eileen happy")
        pause 0.2
        At("eileen happy", glitch)
        pause 0.3
        At("eileen happy")
        pause 1.3
        At("eileen happy", glitch)
        pause 0.1
        At("eileen happy")
        pause 1.0
        repeat 
    
    $ snow_behind_character = ParticleSystem("b", "game\Helpers\effects\snow1.png", 50, 5, 10)  # Adjust parameters as needed
    $ snow_between_character_and_text = ParticleSystem("n", "game\Helpers\effects\snow1.png", 50, 5, 10)
    $ snow_in_front_of_text_box = ParticleSystem("f", "game\Helpers\effects\snow2.png", 50, 5, 10)

    #show particles:
    #    show_particles(snow_behind_character)
    #    show_particles(snow_between_character_and_text)
    #    show_particles(snow_in_front_of_text_box)

    show eileen glitched at center
        
    "start of visual novel"

    $ Chapter(1).start()

    $ Chapter(2).start()

    return
