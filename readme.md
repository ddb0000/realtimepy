# realtimepy
![realtimepy in action](https://raw.githubusercontent.com/ddb0000/realtimepy/main/rtpy.gif)

dynamic particle simulation with real-time logging and interactive controls.  `pygame` + `ipython`

### run
   ```
   pip install -r requirements.txt
   ```

   ```
   py realtimepy.py
   ```

### fun
interact with the simulation using these functions or create new ones:
```python
change_global_speed(factor)
randomize_directions()
change_particle_size(new_size)
adjust_gravity(new_gravity)
toggle_bouncing()
update_particle_colors(new_r, new_g, new_b)
```
add new particles to the simulation with a custom function. define the function and use it in the ipython shell:
```python
def add_particles(count, size=3, speed=2.0):
    global particles
    for _ in range(count):
        new_particle = Particle(screen_width, screen_height)
        new_particle.size = size
        new_particle.speed = speed
        particles.append(new_particle)
# use in ipython shell
add_particles(50, size=5, speed=1.5)
```
