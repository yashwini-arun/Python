steps = 0

def add_steps(count):
    global steps
    steps += count

def total_steps():
    return steps

def calories_burned():
    return steps * 0.04   # approx calories per step
