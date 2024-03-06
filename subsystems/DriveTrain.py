from wpilib.drive import *
from wpilib import *
from phoenix5 import *
import constants

class DriveTrain:
    left_master: TalonSRX
    left_slave: TalonSRX

    right_master: TalonSRX
    right_slave: TalonSRX

    drive: DifferentialDrive

    def __init__(self):
        #! Left side
        self.left_master = TalonSRX(constants.DriveTrain.LEFT_MASTER)
        self.left_master.setNeutralMode(NeutralMode.Brake)

        self.left_slave = TalonSRX(13)
        self.left_slave.setNeutralMode(constants.DriveTrain.LEFT_SLAVE)
        self.left_slave.setInverted(True)
        self.left_slave.follow(self.left_master)

        #! Right side
        self.right_master = TalonSRX(constants.DriveTrain.RIGHT_MASTER)
        self.right_master.setNeutralMode(NeutralMode.Brake)

        self.right_slave = TalonSRX(constants.DriveTrain.RIGHT_SLAVE)
        self.right_slave.setNeutralMode(NeutralMode.Brake)
        self.right_slave.setInverted(True)

        #! Drive handler
        self.drive = DifferentialDrive(self.left_master, self.right_master)