from wpilib.drive import *
from wpilib import *
from phoenix5 import *
from subsystems.DriveTrain import DriveTrain

class Robot(TimedRobot):
    drive: DriveTrain
    controller: XboxController

    def robotInit(self):
        self.drive = DriveTrain()
        self.controller = XboxController(0)

    def teleopPeriodic(self):
        self.drive.drive.arcadeDrive(self.controller.getLeftY(), self.controller.getRightX())
    