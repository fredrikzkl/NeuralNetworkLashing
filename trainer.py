import torch.optim as optim

from torch import nn
import torch
import filehandler

class trainer:
    def __init__(self, net):
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
        self.path = './'


    #Epoch definerer hvor mange ganger vi skal kjøre datasettet
    def trainNetwork(self, epoch=2, trainset=None):
        for e in range(epoch):
            running_loss = 0.0
            for i, data in enumerate(trainset, 0):
                # get the inputs; data is a list of [inputs, labels]
                inputs, labels = data

                # zero the parameter gradients
                self.optimizer.zero_grad()

                # forward + backward + optimize
                outputs = self.net(inputs)
                loss = self.criterion(outputs, labels)
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



