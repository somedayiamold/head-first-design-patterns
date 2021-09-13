from abc import ABCMeta, abstractmethod
from typing import List


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError('`execute` method not implemented')


class CeilingFan:
    HIGH: int = 2
    MEDIUM: int = 1
    LOW: int = 0

    def __init__(self, location: str) -> None:
        self.location: str = location

    def high(self) -> None:
        self.level: int = self.HIGH
        print(f'{self.location} ceiling fan is on high')

    def medium(self) -> None:
        self.level = self.MEDIUM
        print(f'{self.location} ceiling fan is on medium')

    def low(self) -> None:
        self.level = self.LOW
        print(f'{self.location} ceiling fan is on low')

    def off(self) -> None:
        self.level = 0
        print(f'{self.location} ceiling fan is off')

    def get_speed(self) -> int:
        return self.level


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan: CeilingFan = ceiling_fan

    def execute(self) -> None:
        self.ceiling_fan.off()


class CeilingFanOnCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan: CeilingFan = ceiling_fan

    def execute(self) -> None:
        self.ceiling_fan.high()


class GarageDoor:
    def __init__(self, location: str) -> None:
        self.location: str = location

    def up(self) -> None:
        print(f'{self.location} garage Door is Up')

    def down(self) -> None:
        print(f'{self.location} garage Door is Down')

    def stop(self) -> None:
        print(f'{self.location} garage Door is Stopped')

    def light_on(self) -> None:
        print(f'{self.location} garage light is on')

    def light_off(self) -> None:
        print(f'{self.location} garage Door is off')


class GarageDoorDownCommand(Command):
    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door: GarageDoor = garage_door

    def execute(self) -> None:
        self.garage_door.down()


class GarageDoorUpCommand(Command):
    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door: GarageDoor = garage_door

    def execute(self) -> None:
        self.garage_door.up()


class Hottub:
    def on(self) -> None:
        self._on: bool = True

    def off(self) -> None:
        self._on = False

    def bubbles_on(self) -> None:
        if self._on:
            print('Hottub is bubbling!')

    def jets_on(self) -> None:
        if self._on:
            print('Hottub jets are on')

    def jets_off(self) -> None:
        if self._on:
            print('Hottub jets are off')

    def set_temperature(self, temperature: int) -> None:
        self.temperature: int = temperature

    def heat(self) -> None:
        self.temperature = 105
        print('Hottub is heating to a steaming 105 degrees')

    def cool(self) -> None:
        self.temperature = 98
        print('Hottub is cooling to 98 degrees')


class HottubOffCommand(Command):
    def __init__(self, hottub: Hottub) -> None:
        self.hottub: Hottub = hottub

    def execute(self) -> None:
        self.hottub.cool()
        self.hottub.off()


class HottubOnCommand(Command):
    def __init__(self, hottub: Hottub) -> None:
        self.hottub: Hottub = hottub

    def execute(self) -> None:
        self.hottub.on()
        self.hottub.heat()
        self.hottub.bubbles_on()


class Light:
    def __init__(self, location: str) -> None:
        self.location: str = location

    def on(self) -> None:
        print(f'{self.location} light is on')

    def off(self) -> None:
        print(f'{self.location} light is off')


class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.off()


class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.on()


class LivingroomLightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.off()


class LivingroomLightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.on()


class Stereo:
    def __init__(self, location: str) -> None:
        self.location: str = location

    def on(self) -> None:
        print(f'{self.location} stereo is on')

    def off(self) -> None:
        print(f'{self.location} stereo is off')

    def set_cd(self) -> None:
        print(f'{self.location} stereo is set for CD input')

    def set_dvd(self) -> None:
        print(f'{self.location} stereo is set for DVD input')

    def set_radio(self) -> None:
        print(f'{self.location} stereo is set for Radio')

    def set_volume(self, volume: int) -> None:
        print(f'{self.location}  stereo volume set to {volume}')


class StereoOffCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self.stereo: Stereo = stereo

    def execute(self) -> None:
        self.stereo.off()


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self.stereo: Stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)


class NoCommand(Command):
    def execute(self) -> None:
        pass


class RemoteControl:
    def __init__(self) -> None:
        self.on_commands: List[Command] = []
        self.off_commands: List[Command] = []

        no_command = NoCommand()
        for i in range(7):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int) -> None:
        self.on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int) -> None:
        self.off_commands[slot].execute()

    def __str__(self) -> str:
        result: List[str] = []
        result.append('\n------ Remote Control -------\n')
        for i in range(len(self.on_commands)):
            result.append(
                f'[slot {i}] {self.on_commands[i].__class__.__name__}     {self.off_commands[i].__class__.__name__}\n'
            )
        return ''.join(result)


if __name__ == '__main__':
    remote_control: RemoteControl = RemoteControl()
    living_room_light = Light('Living Room')
    kitchen_light: Light = Light('Kitchen')
    ceiling_fan: CeilingFan = CeilingFan('Living Room')
    garage_door: GarageDoor = GarageDoor('Garage')
    stereo: Stereo = Stereo('Living Room')

    living_room_light_on: LightOnCommand = LightOnCommand(living_room_light)
    living_room_light_off: LightOffCommand = LightOffCommand(living_room_light)
    kitchen_light_on: LightOnCommand = LightOnCommand(kitchen_light)
    kitchen_light_off: LightOffCommand = LightOffCommand(kitchen_light)

    ceiling_fan_on: CeilingFanOnCommand = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off: CeilingFanOffCommand = CeilingFanOffCommand(ceiling_fan)

    garage_door_up: GarageDoorUpCommand = GarageDoorUpCommand(garage_door)
    garage_door_down: GarageDoorDownCommand = GarageDoorDownCommand(garage_door)

    stereo_on_with_cd: StereoOnWithCDCommand = StereoOnWithCDCommand(stereo)
    stereo_off: StereoOffCommand = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, stereo_on_with_cd, stereo_off)

    print(remote_control)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)
