class Tuner:
    def __init__(self, description: str) -> None:
        self.description: str = description
        self.frequency: float

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def set_frequency(self, frequency: float) -> None:
        print(f'{self.description} setting frequency to {frequency}')
        self.frequency = frequency

    def set_am(self) -> None:
        print(f'{self.description} setting AM mode')

    def set_fm(self) -> None:
        print(f'{self.description} setting FM mode')

    def __str__(self) -> str:
        return self.description


class StreamingPlayer:
    def __init__(self, description: str) -> None:
        self.description: str = description
        self.current_chapter: int
        self.movie: str

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def play(self, movie: str, chapter: int) -> None:
        if movie:
            self.movie = movie
            self.current_chapter = 0
            print(f'{self.description} playing "{movie}"')
        else:
            if not self.movie:
                print(f"{self.description} can't play chapter {chapter} no movie selected")
            else:
                self.current_chapter = chapter
                print(f'{self.description} playing chapter {self.current_chapter} of "{self.movie}"')

    def stop(self) -> None:
        self.current_chapter = 0
        print(f'{self.description} stopped "{self.movie}"')

    def pause(self) -> None:
        print(f'{self.description} paused "{self.movie}"')

    def set_two_channel_audio(self) -> None:
        print(f'{self.description} set two channel audio')

    def set_surround_audio(self) -> None:
        print(f'{self.description} set surround audio')

    def __str__(self) -> str:
        return self.description


class Amplifier:
    def __init__(self, description: str) -> None:
        self.description: str = description
        self.tuner: Tuner
        self.player: StreamingPlayer

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def set_stereo_sound(self) -> None:
        print(f'{self.description} stereo mode on')

    def set_surround_sound(self) -> None:
        print(f'{self.description} surround sound on (5 speakers, 1 subwoofer)')

    def set_volume(self, level: int) -> None:
        print(f'{self.description}  setting volume to {level}')

    def set_tuner(self, tuner: Tuner) -> None:
        print(f'{self.description} setting tuner to {self.tuner}')
        self.tuner = tuner

    def set_streaming_player(self, player: StreamingPlayer) -> None:
        print(f'{self.description} setting Streaming player to {player}')
        self.player = player

    def __str__(self) -> str:
        return self.description


class CdPlayer:
    def __init__(self, description: str) -> None:
        self.description: str = description
        self.current_track: int
        self.title: str

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def eject(self) -> None:
        self.title = ''
        print(f'{self.description} eject')

    def play(self, title: str, track: int) -> None:
        if title:
            self.title = title
            self.current_track = 0
            print(f'{self.description} playing "{title}"')
        else:
            if not self.title:
                print(f"{self.description} can't play track {self.current_track}, no cd inserted")
            else:
                self.current_track = track
                print(f'{self.description} playing track {self.current_track}')

    def stop(self) -> None:
        self.current_track = 0
        print(f'{self.description} stopped')

    def pause(self) -> None:
        print(f'{self.description} paused "{self.title}"')

    def __str__(self) -> str:
        return self.description


class Projector:
    def __init__(self, description: str) -> None:
        self.description: str = description

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def wide_screen_mode(self) -> None:
        print(f'{self.description} in widescreen mode (16x9 aspect ratio)')

    def tv_mode(self) -> None:
        print(f'{self.description} in tv mode (4x3 aspect ratio)')

    def __str__(self) -> str:
        return self.description


class Screen:
    def __init__(self, description: str) -> None:
        self.description: str = description

    def up(self) -> None:
        print(f'{self.description} going up')

    def down(self) -> None:
        print(f'{self.description} going down')

    def __str__(self) -> str:
        return self.description


class TheaterLights:
    def __init__(self, description: str) -> None:
        self.description: str = description

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def dim(self, level: int) -> None:
        print(f'{self.description} dimming to {level}%')

    def __str__(self) -> str:
        return self.description


class PopcornPopper:
    def __init__(self, description: str) -> None:
        self.description: str = description

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def pop(self) -> None:
        print(f'{self.description} popping popcorn!')

    def __str__(self) -> str:
        return self.description


class HomeTheaterFacade:
    def __init__(
        self, amp: Amplifier, tuner: Tuner, player: StreamingPlayer, projector: Projector, screen: Screen,
        lights: TheaterLights, popper: PopcornPopper
    ) -> None:
        self.amp: Amplifier = amp
        self.tuner: Tuner = tuner
        self.player: StreamingPlayer = player
        self.projector: Projector = projector
        self.screen: Screen = screen
        self.lights: TheaterLights = lights
        self.popper: PopcornPopper = popper

    def watch_movie(self, movie: str) -> None:
        print('Get ready to watch a movie...')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.player.on()
        self.player.play(movie, 0)

    def end_movie(self) -> None:
        print('Shutting movie theater down...')
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()

    def listen_to_radio(self, frequency: float) -> None:
        print('Tuning in the airwaves...')
        self.tuner.on()
        self.tuner.set_frequency(frequency)
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_tuner(self.tuner)

    def end_radio(self) -> None:
        print('Shutting down the tuner...')
        self.tuner.off()
        self.amp.off()


class HomeTheaterTestDrive:
    def __init__(self) -> None:
        amp: Amplifier = Amplifier('Amplifier')
        tuner: Tuner = Tuner('AM/FM Tuner')
        player: StreamingPlayer = StreamingPlayer('Streaming Player')
        # cd: CdPlayer = CdPlayer('CD Player')
        projector: Projector = Projector('Projector')
        lights: TheaterLights = TheaterLights('Theater Ceiling Lights')
        screen: Screen = Screen('Theater Screen')
        popper: PopcornPopper = PopcornPopper('Popcorn Popper')

        home_theater = HomeTheaterFacade(amp, tuner, player, projector, screen, lights, popper)
        home_theater.watch_movie('Raiders of the Lost Ark')
        home_theater.end_movie()


if __name__ == '__main__':
    HomeTheaterTestDrive()
