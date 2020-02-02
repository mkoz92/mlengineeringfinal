# torch imports
import torch.nn.functional as F
import torch.nn as nn

#binary classifier original
## TODO: Complete this classifier
class Vol_Predictor(nn.Module):
    """
    Define a neural network that performs binary classification.
    The network should accept your number of features as input, and produce 
    a single sigmoid value, that can be rounded to a label: 0 or 1, as output.
    
    Notes on training:
    To train a binary classifier in PyTorch, use BCELoss.
    BCELoss is binary cross entropy loss, documentation: https://pytorch.org/docs/stable/nn.html#torch.nn.BCELoss
    """

    ## TODO: Define the init function, the input params are required (for loading code in train.py to work)
    def __init__(self, input_dim, hidden_dim, output_dim):
        """
        Initialize the model by setting up linear layers.
        Use the input parameters to help define the layers of your model.
        :param input_features: the number of input features in your training/test data
        :param hidden_dim: helps define the number of nodes in the hidden layer(s)
        :param output_dim: the number of outputs you want to produce
        """
        super(Vol_Predictor, self).__init__()

        # define any initial layers, here\
        
        # linear layer (input -> hidden_1)
        #self.fc1 = nn.Linear(input_dim, hidden_dim)
        # linear layer (n_hidden -> hidden_2)
        #self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        #self.fc3 = nn.Linear(hidden_dim, output_dim)
        # linear layer (n_hidden -> 10)
        # dropout layer (p=0.2)
        # dropout prevents overfitting of data
        #self.dropout = nn.Dropout(0.2)
        self.drop = nn.Dropout(0.3)
        self.sig = nn.Sigmoid()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, output_dim)

        
    
    ## TODO: Define the feedforward behavior of the network
    def forward(self, x):
        """
        Perform a forward pass of our model on input features, x.
        :param x: A batch of input features of size (batch_size, input_features)
        :return: A single, sigmoid-activated value as output
        """
        
        
        # define the feedforward behavior
        out = F.relu(self.fc1(x))
        out = self.drop(out)
        out = F.relu(self.fc2(out))
        out = self.drop(out)
        out = (self.fc3(out))
        #x = self.sig(out)
        x = out
        
        #out = F.relu(self.fc1(x))
        #out = self.fc2(out)
        #x = self.sig(out)
        
        return x
    