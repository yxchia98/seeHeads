from pynput.mouse import Controller, Button
import time

mouse = Controller()

while True:
    mouse.click(Button.left, 1)
    print('clicked')
    time.sleep(5)
    print('clicked')
    mouse.click(Button.left, 1)
    time.sleep(30)

# import torch
# print(torch.cuda.is_available())
# # setting device on GPU if available, else CPU
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# print('Using device:', device)
# print()
#
# #Additional Info when using cuda
# if device.type == 'cuda':
#     print(torch.cuda.get_device_name(0))
#     print('Memory Usage:')
#     print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
#     print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')