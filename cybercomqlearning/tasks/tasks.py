from celery.task import task
from dockertask import docker_task
from subprocess import call,STDOUT
import requests
import random

#Default base directory 
#basedir="/data/static/"


#Example task
@task()
def add(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x + y
    return result

@task()
def dice_roll(sides):
def dice(number_dice):
for dice_roll in range(x)
    x = dice
    
    """ Example task that rolls a die with a specified number of sides 
        args: (sides, number_dice)
        return random int """
    return random.randrange(sides) + 1
print dice_roll(x)

    
    
