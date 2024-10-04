# Mridu Manda

Mridu-Manda is a minimal console application that shows weather and is based on the OpenWeatherMap API.

## Features

- Compact display of weather
- Supports automatic location detection using ipInfo
- Supports command line city input
- Four different output formats, one liner, with ascii, with ascii and color and default

## Requirements

- Requires an API key from OpenWeatherMap
- Requires Python 3.8 or later
- Requires `requests` module 2.31 or later
- Requires `rich` module 13.8.0 or later

## Installation

### From PyPI

```bash
pip install mridumanda_shvedt
```

## Usage

After installing run

```bash
mrdmnd                  # for default display of weather
mrdmnd -o               # for one line display of weather
mrdmnd -g               # for weather display with ascii art
mrdmnd -c Kolkata       # for weather display with city name 
```

If it is first time, you will be prompted to enter your API key from OpenWeatherMap. After it is done, run the program again and enjoy.

## Contributions

Feel free to contribute to the project by opening an issue.

## Credits

The ASCII art for weather representation in this project was created by [Julynx](https://github.com/Julynx). It was taken from [here](https://github.com/Julynx/wthr).


## License

This is licensed under the GNU General Public License version 3.0

## Changelog

## Version 1.6 - Latest Release

- Added a new weather display option `-gc` to display weather data with ascii and colors
- Added sunrise and sunset times, feels like, visibility
- Optimized some parts of the code to be more efficient