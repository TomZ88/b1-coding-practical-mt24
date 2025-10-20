class PDController:
    #setting default kp and kd values, initialising previous error
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0

    #resets controller's memory
    def reset(self):
        self.prev_error = 0.0

    def get_action(self, reference, observation):
        error = reference - observation
        action = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return action
