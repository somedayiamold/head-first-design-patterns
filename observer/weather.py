from abc import ABCMeta, abstractmethod
from typing import List, Optional


class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, temp: float, humidity: float, perssure: float) -> None:
        raise NotImplementedError('`update` method not implemented')


class Subject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def register_observer(self, o: Observer) -> None:
        raise NotImplementedError('`register_observer` method not implemented')

    @abstractmethod
    def remove_observer(self, o: Observer) -> None:
        raise NotImplementedError('`remove_observer` method not implemented')

    @abstractmethod
    def notify_observers(self) -> None:
        raise NotImplementedError('`remove_observer` method not implemented')


class DisplayElement:
    __metaclass__ = ABCMeta

    def display(self) -> None:
        raise NotImplementedError('`display` method not implemented')


class WeatherData(Subject):
    def __init__(self) -> None:
        self._temperature: float
        self._humidity: float
        self._perssure: float
        self._observers: List[Observer] = []

    def register_observer(self, o: Observer) -> None:
        self._observers.append(o)

    def remove_observer(self, o: Observer) -> None:
        self._observers.remove(o)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._perssure)

    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, perssure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._perssure = perssure
        self.measurements_changed()

    def get_temperature(self) -> float:
        return self._temperature

    def get_humidity(self) -> float:
        return self._humidity

    def get_pressure(self) -> float:
        return self._perssure


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        self._current_pressure: float = 29.92
        self._last_pressure: float
        self._weather_data: WeatherData = weather_data
        self._weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, perssure: float) -> None:
        self._last_pressure = self._current_pressure
        self._current_pressure = perssure
        self.display()

    def display(self) -> None:
        print('Forecast: ')
        if self._current_pressure > self._last_pressure:
            print('Improving weather on the way!')
        elif self._current_pressure == self._last_pressure:
            print('More of the same')
        elif self._current_pressure < self._last_pressure:
            print('Watch out for cooler, rainy weather')


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        self._temperature: Optional[float] = None
        self._humidity: float
        self._weather_data: WeatherData = weather_data
        self._weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, perssure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        print(f'Current conditions: {self._temperature} F degrees and {self._humidity}% humidity')


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        self._max_temp: float = 0.0
        self._min_temp: float = 200
        self._temp_sum: float = 0.0
        self._num_readings: int = 0
        self._weather_data: WeatherData = weather_data
        self._weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, perssure: float) -> None:
        self._temp_sum += temp
        self._num_readings += 1
        if temp > self._max_temp:
            self._max_temp = temp
        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self) -> None:
        print(f'Avg/Max/Min temperature = {self._temp_sum / self._num_readings}/{self._max_temp}/{self._min_temp}')


class HeatIndexDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        self._heat_index: float = 0.0
        self._weather_data: WeatherData = weather_data
        self._weather_data.register_observer(self)

    def update(self, t: float, rh: float, perssure: float) -> None:
        self._heat_index = self.compute_heat_index(t, rh)
        self.display()

    def compute_heat_index(self, t: float, rh: float) -> float:
        index: float = (
            (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) + (0.00941695 * (t * t)) + (
                0.00728898 * (rh * rh)
            ) + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
            (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 * (rh * rh * rh)) +
            (0.00000142721 * (t * t * t * rh)) + (0.000000197483 * (t * rh * rh * rh)) -
            (0.0000000218429 * (t * t * t * rh * rh)) + 0.000000000843296 * (t * t * rh * rh * rh)) -
            (0.0000000000481975 * (t * t * t * rh * rh * rh))
        )
        return index

    def display(self) -> None:
        print(f'Heat index is {self._heat_index}')


if __name__ == '__main__':
    weather_data: WeatherData = WeatherData()

    current_display: CurrentConditionsDisplay = CurrentConditionsDisplay(weather_data)
    statistics_display: StatisticsDisplay = StatisticsDisplay(weather_data)
    forecast_display: ForecastDisplay = ForecastDisplay(weather_data)
    heatIndex_display: HeatIndexDisplay = HeatIndexDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
