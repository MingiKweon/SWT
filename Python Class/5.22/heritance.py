class Vehicle:
    ACC = 5

    def __init__(self):
        self.speed = 0

    def speed_up(self):
        self.speed += Vehicle.ACC
        self.speed = min(self.speed, 240)
    
    def __str__(self):
        return f"현재 속도는 {self.speed} 입니다."

mycar = Vehicle()


