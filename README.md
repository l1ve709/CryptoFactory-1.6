# CryptoFactory.exe - Fake Cryptocurrency Mining Application


## Language(s) used

<picture>
  <source srcset="https://skillicons.dev/icons?i=py" media="(prefers-color-scheme: dark)">
  <img src="https://skillicons.dev/icons?i=py">
</picture>


Welcome to **CryptoFactory.exe** – a fun and interactive fake cryptocurrency mining simulator built with Python and PyQt5. This application mimics the process of mining cryptocurrency with a user-friendly interface, fake GPU stats, and the ability to plot performance data in real-time.

## Features

- **Real-time Mining Simulation**: The app simulates mining operations, showing fake statistics such as speed, average time, and GPU performance.
- **BTC Price Fetching**: The app fetches the real-time Bitcoin price from the CoinGecko API.
- **Performance Data**: Users can view mining performance data and plot speed and average time using Matplotlib.
- **GPU Information**: Fake GPU stats including temperature, load, and memory usage are displayed.
- **BTC and USD Values**: The app tracks and displays fake Bitcoin and USD values as mining progresses.
- **User Interaction**: Start and stop mining at any time. Explore additional features like settings, about, and support links.

## Dependencies

To run the application, you need the following Python libraries installed:

- `PyQt5`: for building the GUI
- `requests`: to fetch real-time BTC prices
- `matplotlib`: for plotting performance data

### Installing Dependencies on Linux

For Linux users, you can install the necessary dependencies as follows:

1. **Install Python 3**: Ensure that Python 3 is installed.
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. **Install PyQt5**:
    ```bash
    sudo apt install python3-pyqt5
    ```

3. **Install Additional Python Libraries**:
    ```bash
    pip3 install requests matplotlib
    ```

If `PyQt5` is not available through your package manager, you can install it via pip:

```bash
pip3 install PyQt5
```

## How to Run

### Running on Linux

1. **Clone the repository**:
    ```bash
    git clone <https://github.com/l1ve709XXD/CryptoFactory-1.6.git>
    cd <main.py>
    ```

2. **Make the script executable**:
    ```bash
    chmod +x main.py
    ```

3. **Run the application**:
    ```bash
    ./main.py
    ```

Alternatively, you can run it with Python 3 directly:
```bash
python3 main.py
```

## File Overview

- **main.py**: The main Python file that runs the fake mining application.
- **background.jpg**: An optional background image file used in the main window. Ensure it's in the same directory as `main.py`.

## Functionality

### Start/Stop Mining
- **Start Mining**: Click the `RUN` button to simulate cryptocurrency mining.
- **Stop Mining**: Click the `STOP` button to stop the simulation.

### Wallet and Transactions
- Monitor your fake Bitcoin and USD wallet values as they update during the mining process.

### GPU Stats
- Displays fake GPU information (e.g., temperature, memory usage) that updates in real-time.

### Performance Data
- The app records and displays performance data, which you can visualize with the **Plot Performance Data** button.

## Settings and Customization

- **Theme**: Change between light and dark themes from the settings window.
- **About & Support**: Links to an external website and a Discord server for additional information and support.

## Linux-Specific Notes

- **Permission Issues**: If you encounter permission issues while trying to run the script, ensure the `main.py` file is executable (`chmod +x main.py`).
- **Python Version**: Make sure you are using Python 3. Some distributions might still default to Python 2.
- **PyQt5 Installation**: If you encounter issues with installing PyQt5 via `apt`, using `pip` to install it (`pip3 install PyQt5`) is an alternative solution.

## Future Improvements
- Add real-time mining pool interaction.
- Enhance GPU information with real-time hardware monitoring.

## License

This project is licensed under the GPL-3.0 license.

```

### Key Additions for Linux:
- **Dependencies Installation**: Detailed steps for installing Python, PyQt5, and other dependencies on Linux.
- **Running the App**: Steps to make the Python script executable and run it via the terminal.
- **Linux-Specific Notes**: Tips on dealing with permissions, ensuring Python 3 is being used, and troubleshooting PyQt5 installation.
```

## My Discord Acc

![My Discord](https://lantern.rest/api/v1/users/794909914760871967?svg=1&theme=dark&borderRadius=2&hideActivity=1&hideStatus=0)

