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
    """ Example task that rolls a die with a specified number of sides 
        args: sides
        return random int """
    return random.randrange(sides) + 1

@task()
def multi_dice(number,sides):
    """Example task that rolls a specified number of dice with a specified
       number of sides
       args: ('number of dice','number of sides')
       returns a list N integers in length"""
    dice = range(number)
    result = []
    for i in dice:
        result.append(dice_roll(sides))
    return result
    

    
    
