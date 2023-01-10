# initialize pygame
import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([1920, 1080]) # use this to set screen resolution

# Manually entered picture colors
statusColors = {
    "red": (184, 29, 19),
    "yellow": (239, 183, 0),
    "green": (0, 132, 80),
    "waiting": (84, 84, 84)
}

#input references to images
images = {
    "red": pygame.image.load("./images/red.jpg"),
    "yellow": pygame.image.load("./images/yellow.jpg"),
    "green": pygame.image.load("./images/green.jpg"),
    "waiting": pygame.image.load("./images/waiting.jpg")
}

# scale each image
for image in images:
    images[image] = pygame.transform.scale(images[image], (screen.get_width(), int(screen.get_width() * images[image].get_height() / images[image].get_width())))


def updateStatus(status):
    # load the relevant audio file and play it
    try:
        pygame.mixer.music.load("./audio/" + status + ".mp3")
        pygame.mixer.music.play()
    except:
        pass

    # change the background color to the color of the image in case it isn't large enough to cover the whole screen
    screen.fill(statusColors[status])
    screen.blit(images[status], (0, (screen.get_height() - images[status].get_height()) / 2))

    # update display
    pygame.display.flip()

def running():
    # Exit program when the windows is exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

updateStatus("waiting")
