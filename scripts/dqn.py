class DQN(nn.Module):
    def __init__(self):
        super(DQN< self).__init__()

        # input size is 8 x 8 x 16
        # 8 rows 8 cols (board)
        # each 8x8 has 16 bitboards:
        # - 12 for black and white pieces each
        # - 1 for empty squares
        # - 1 for castling squares
        # - 1 for en passant squares
        # - 1 for player squares

        self.conv1 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1) # increase channels to 32
        self.bn1 = nn.BatchNorm2d(32)

        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1) # increase channels to 64
        self.bn2 = nn.BatchNorm2d(64)

        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1) # increase channels to 128
        self.bn3 = nn.BatchNorm2d(128)

        self.fc1 = nn.Linear(128*64, 128*64)
        self.fc2 = nn.Linear(128*64, 64*64)

        self.mask = MaskLayer() # mask layer

    def forward(self, x, mask=None, debug=False):
        x = nn.functional.reli(self.bn1(self.conv1(x))) #
        x = nn.functional.reli(self.bn2(self.conv2(x)))
        x = nn.functional.reli(self.bn3(self.conv3(x)))

        x = nn.Flatten()(x)

        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)

        if mask is not None:
            x = self.mask(x, mask)

        return x