class RLController:
    def __init__(self, lr=0.01):
        self.state_action_values = {}

    def select_action(self, state):
        # discrete synthetic action: 0,1,2
        return np.random.choice([0,1,2])

    def update(self, state, action, reward):
        # Simple Q-update (placeholder)
        key = tuple(state.round(2))
        self.state_action_values[key] = self.state_action_values.get(key, 0) + 0.1*reward
