import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from NeuralNetwork import NeuralNetwork

# import matplotlib.pyplot as plt
# import numpy as np
# import cv2

def trainNeuralNetwork():
    neural_net = NeuralNetwork()
    train_set = ImageFolder(root='./resources/trash_dataset/train', transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]))
    trainloader = DataLoader(
        train_set, batch_size=2, shuffle=True, num_workers=2)

    # potrzebne do wyświetlania loss w każdej iteracji
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(neural_net.parameters(), lr=0.001, momentum=0.9)

    epoch_num = 10 # najlepiej 10, dla lepszej wiarygodności
    for epoch in range(epoch_num):
        measure_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            # czyszczenie gradientu f-cji
            optimizer.zero_grad()
            outputs = neural_net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            measure_loss += loss.item()
            if i:
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, measure_loss))
                measure_loss = 0.0

    print('Finished.')
    PATH = './trained_nn.pth'
    torch.save(neural_net.state_dict(), PATH)

def main():
    trainNeuralNetwork()

if __name__ == '__main__':
    main()

