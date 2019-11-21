import torch.optim as optim

from torch import nn
import torch
import filehandler
from nettverk import Nettverk


class trainer:
    def __init__(self, net):
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
        self.path = './'
        self.net = net


    #Epoch definerer hvor mange ganger vi skal kjøre datasettet
    def trainNetwork(self, epoch=2, heroes=None, wins=None):
        for e in range(epoch):
            running_loss = 0.0
            for i, data in enumerate(heroes, 0):
                # get the inputs; data is a list of [inputs, labels]
                temp_heroes = heroes[i]
                temp_wins = wins[i]

                # zero the parameter gradients
                self.optimizer.zero_grad()

                # forward + backward + optimize
                outputs = self.net(temp_heroes)
                loss = self.criterion(outputs, temp_wins)
                loss.backward()
                self.optimizer.step()

                # print statistics
                running_loss += loss.item()
                if i % 2000 == 1999:  # print every 2000 mini-batches
                    print('[%d, %5d] loss: %.3f' %
                          (epoch + 1, i + 1, running_loss / 2000))
                    running_loss = 0.0

                print('Finished Training')


            torch.save(self.net.state_dict(), self.PATH)



#Starte med å importere dataen
data = filehandler.load_data()

wins = []
heroes = []
for i in range(len(data)):
    wins.append(data[i].radiantWin)
    heroes.append(data[i].heroArray)

model = Nettverk()
t = trainer(model)

t.trainNetwork(heroes=heroes, wins=wins)
