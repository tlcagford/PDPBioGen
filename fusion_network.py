import torch
import torch.nn as nn

class FusionLSTM(nn.Module):
    def __init__(self, eeg_dim=2, ecg_dim=2, met_dim=2, hidden=32):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=eeg_dim+ecg_dim+met_dim,
            hidden_size=hidden,
            num_layers=1,
            batch_first=True
        )
        self.fc = nn.Linear(hidden, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return torch.sigmoid(self.fc(out[:, -1, :]))
