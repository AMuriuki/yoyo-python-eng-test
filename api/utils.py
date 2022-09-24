import statistics
from typing import Union
from dataclasses import dataclass


@dataclass
class WeatherData:
    temperature_data: dict

    def __post_init__(self) -> None:
        data = []
        for item in self.temperature_data["forecast"]["forecastday"]:
            data.append(
                self.__convert_str_to_num(val=item["day"]["avgtemp_c"])
            )
        self.data = data

    def __convert_str_to_num(self, val: str) -> Union[int, float]:
        try:
            return int(val)
        except ValueError:
            return float(val)

    @property
    def summary(self) -> dict:
        return {
            "maximum": max(self.data),
            "minimum": min(self.data),
            "average": round(sum(self.data) / len(self.data), 1),
            "median": statistics.median(self.data),
        }
