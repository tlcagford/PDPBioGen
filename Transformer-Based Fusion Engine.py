import torch
import torch.nn as nn

class FusionTransformer(nn.Module):
    def __init__(self, input_dim=6, d_model=32, nhead=4, num_layers=1):
        super().__init__()
        self.embedding = nn.Linear(input_dim, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(d_model, 1)

    def forward(self, x):
        # x shape: [batch, seq_len, input_dim]
        x = self.embedding(x)
        x = self.transformer(x.transpose(0, 1))  # seq first
        return torch.sigmoid(self.fc(x[-1]))
