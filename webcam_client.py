import pygame
import socket

HOST = 'localhost'  # The server's hostname or IP address. Change this if you're not running locally
PORT = 1234  # The port used by the server
BUFFER_SIZE = 4096

pygame.init()
pygame.display.init()

display_width, display_height = 840, 480
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Servertest')


def get_img():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    imag = "image.bmp"
    fp = open(imag, 'wb')
    s.send(b'img')
    while True:
        received = s.recv(BUFFER_SIZE)
        if not received:
            break
        fp.write(received)

    fp.close()
    print("Data Received successfully")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    get_img()

    frame = pygame.image.load("image.bmp")
    display.blit(frame, (200, 0))
    pygame.display.flip()

pygame.quit()
quit()