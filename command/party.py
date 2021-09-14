from abc import ABCMeta, abstractmethod
from typing import List


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError('`execute` method not implemented')

    @abstractmethod
    def undo(self) -> None:
        raise NotImplementedError('`undo` method not implemented')


class CeilingFan:
    HIGH: int = 3
    MEDIUM: int = 2
    LOW: int = 1
    OFF: int = 0

    def __init__(self, location: str) -> None:
        self.location: str = location
        self.speed: int

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
        self.level = self.OFF
        print(f'{self.location} ceiling fan is off')

    def get_speed(self) -> int:
        return self.speed


class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan: CeilingFan = ceiling_fan

    def execute(self) -> None:
        self.prev_speed: int = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self) -> None:
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan: CeilingFan = ceiling_fan

    def execute(self) -> None:
        self.prev_speed: int = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()

    def undo(self) -> None:
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan: CeilingFan = ceiling_fan

    def execute(self) -> None:
        self.prev_speed: int = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()

    def undo(self) -> None:
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()


class Hottub:
    def __init__(self) -> None:
        self._on: bool
        self.temperature: int = 0

    def on(self) -> None:
        self._on = True

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
        if temperature > self.temperature:
            print(f'Hottub is heating to a steaming {temperature} degrees')
        else:
            print(f'Hottub is cooling to {temperature} degrees')
        self.temperature = temperature


class HottubOffCommand(Command):
    def __init__(self, hottub: Hottub) -> None:
        self.hottub: Hottub = hottub

    def execute(self) -> None:
        self.hottub.set_temperature(98)
        self.hottub.off()

    def undo(self) -> None:
        self.hottub.off()


class HottubOnCommand(Command):
    def __init__(self, hottub: Hottub) -> None:
        self.hottub: Hottub = hottub

    def execute(self) -> None:
        self.hottub.on()
        self.hottub.set_temperature(104)
        self.hottub.bubbles_on()

    def undo(self) -> None:
        self.hottub.off()


class Light:
    def __init__(self, location: str) -> None:
        self.location: str = location

    def on(self) -> None:
        self.level: int = 100
        print(f'{self.location} light is on')

    def off(self) -> None:
        self.level = 0
        print(f'{self.location} light is off')

    def dim(self, level: int) -> None:
        self.level = level
        if level == 0:
            self.off()
        else:
            print(f'Light is dimmed to {level}%')


class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        self.light.on()


class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LivingroomLightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        self.light.on()


class LivingroomLightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


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

    def undo(self) -> None:
        self.stereo.on()


class StereoOnCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self.stereo: Stereo = stereo

    def execute(self) -> None:
        self.stereo.on()

    def undo(self) -> None:
        self.stereo.off()


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self.stereo: Stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

    def undo(self) -> None:
        self.stereo.off()


class TV:
    def __init__(self, location: str) -> None:
        self.location: str = location

    def on(self) -> None:
        print(f'{self.location} TV is on')

    def off(self) -> None:
        print(f'{self.location} TV is off')

    def set_input_channel(self) -> None:
        self.channel: int = 3
        print(f'{self.location} TV channel is set for DVD')


class TVOffCommand(Command):
    def __init__(self, tv: TV) -> None:
        self.tv: TV = tv

    def execute(self) -> None:
        self.tv.off()

    def undo(self) -> None:
        self.tv.on()


class TVOnCommand(Command):
    def __init__(self, tv: TV) -> None:
        self.tv: TV = tv

    def execute(self) -> None:
        self.tv.on()
        self.tv.set_input_channel()

    def undo(self) -> None:
        self.tv.off()


class NoCommand(Command):
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class MacroCommand(Command):
    def __init__(self, commands: List[Command]) -> None:
        self.commands = commands

    def execute(self) -> None:
        for i in self.commands:
            i.execute()

    def undo(self) -> None:
        for i in self.commands[::-1]:
            i.undo()


class RemoteControl:
    def __init__(self) -> None:
        self.on_commands: List[Command] = []
        self.off_commands: List[Command] = []

        no_command = NoCommand()
        for i in range(7):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)

        self.undo_command: Command = no_command

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int) -> None:
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot: int) -> None:
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self) -> None:
        self.undo_command.undo()

    def __str__(self) -> str:
        result: List[str] = []
        result.append('\n------ Remote Control -------\n')
        for i in range(len(self.on_commands)):
            result.append(
                f'[slot {i}] {self.on_commands[i].__class__.__name__}     {self.off_commands[i].__class__.__name__}\n'
            )
        result.append(f'[undo] {self.undo_command.__class__.__name__}\n')
        return ''.join(result)


if __name__ == '__main__':
    remote_control: RemoteControl = RemoteControl()
    light: Light = Light('Living Room')
    tv: TV = TV('Living Room')
    stereo: Stereo = Stereo('Living Room')
    hottub: Hottub = Hottub()

    light_on: LightOnCommand = LightOnCommand(light)
    stereo_on: StereoOnCommand = StereoOnCommand(stereo)
    tv_on: TVOnCommand = TVOnCommand(tv)
    hottub_on: HottubOnCommand = HottubOnCommand(hottub)
    light_off: LightOffCommand = LightOffCommand(light)
    stereo_off: StereoOffCommand = StereoOffCommand(stereo)
    tv_off: TVOffCommand = TVOffCommand(tv)
    hottub_off: HottubOffCommand = HottubOffCommand(hottub)

    party_on: List[Command] = [light_on, stereo_on, tv_on, hottub_on]
    party_off: List[Command] = [light_off, stereo_off, tv_off, hottub_off]
    party_on_macro: MacroCommand = MacroCommand(party_on)
    party_off_macro: MacroCommand = MacroCommand(party_off)

    remote_control.set_command(0, party_on_macro, party_off_macro)

    print(remote_control)
    print('--- Pushing Macro On---')
    remote_control.on_button_was_pushed(0)
    print('--- Pushing Macro Off---')
    remote_control.off_button_was_pushed(0)
