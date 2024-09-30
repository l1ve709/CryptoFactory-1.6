    # 
    # *****************************************************************
    # *    *                                                *          *
    # *     *               _ _          _____ ___   ___  
    # *   *       | / |_   ____|___  / _ \ / _ \ 
    # *  *        | | \ \ / / _ \ / / | | | (_) |        *
    # *     *     | | |\ V /  __// /| |_| |\__, |
    # *   *       |_|_| \_/ \___/_/  \___/   /_/      *
    # *      *                                                     *    *
    # *    *          Contact Mail: businnes@l1ve709.com   *
    # *   *            Contact to Instagram: l1ve709                *   *
    # *      *            Created by Ediz Sönmez                       *
    # *****************************************************************
    # 

import sys
import random
import time
import webbrowser
import requests
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QDateTime
from PyQt5.QtGui import QFont, QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QSizePolicy, QDialog, QComboBox, QFormLayout

base58forCryptoAlfa = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'   # * used "base58" to make it realistic
fakeGPUSl1ve709 = [
    'NVIDIA GeForce RTX 3090', 
    'AMD Radeon RX 6900 XT',   # * fake GPUs
    'NVIDIA GeForce RTX 3080', 
    'AMD Radeon RX 6800 XT'
]

class PerformanceData:
    def __init__(self):
        self.speeds = []
        self.avg_times = []
        self.timestamps = []

    def add_data(self, speed, avg_time):
        now = QDateTime.currentDateTime().toString('HH:mm:ss')
        self.timestamps.append(now)
        self.speeds.append(speed)
        self.avg_times.append(avg_time)

    def plot_data(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.timestamps, self.speeds, label='Speed', color='orange')
        plt.plot(self.timestamps, self.avg_times, label='Average Time', color='blue')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Performance Data')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def fetch_real_time_btc_price():
    """real time btc value(S)"""
    response = requests.get('https://api.coingecko.com/api/v3/simple/price', params={'ids': 'bitcoin', 'vs_currencies': 'usd'})
    data = response.json()
    return data['bitcoin']['usd']

def generate_mining_stats():
    speed = round(random.uniform(2.0, 5.0), 1) 
    avg_time = random.choice([60, 120, 300])
    stats = (
        f"{time.strftime('%H:%M:%S')} speed {speed}s/{avg_time}s "
        f"{random.uniform(100, 150):.1f} {random.uniform(100, 150):.1f} "
        f"{random.randint(10, 150)} {random.randint(100, 1200)} "
        f"{random.randint(0, 30)} diff {random.randint(10000, 20000)}"
    )
    return speed, avg_time, stats

class MiningStatsWindow(QDialog):
    def __init__(self, performance_data):
        super().__init__()
        self.setWindowTitle("Mining Performance Data")
        self.setGeometry(200, 200, 800, 600)

        self.performance_data = performance_data

        
        layout = QVBoxLayout()
        self.stats_text_edit = QTextEdit()
        self.stats_text_edit.setStyleSheet("background-color: #000000 ; color: #000000 ;")
        self.stats_text_edit.setFont(QFont('Arial', 10))
        self.stats_text_edit.setReadOnly(True)
        layout.addWidget(self.stats_text_edit)

        self.plot_button = QPushButton("Plot Performance Data")
        self.plot_button.clicked.connect(self.plot_data)
        layout.addWidget(self.plot_button)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(2500) 

        self.color_cycle = [
            "#FF4500", 
            "#32CD32", 
            "#1E90FF",  
            "#FFD700",  
            "#8A2BE2",  
            "#00CED1"   
        ]
        self.color_index = 0

    def update_stats(self):
        speed, avg_time, stats = generate_mining_stats()
        color = self.color_cycle[self.color_index % len(self.color_cycle)]
        self.color_index += 1

        
        stats_message = (
            f'<p style="color: {color};">{time.strftime("%H:%M:%S")} | '
            f'Speed: {speed}s | Avg Time: {avg_time}s | {stats}</p>'
        )
        self.stats_text_edit.append(stats_message)
        self.performance_data.add_data(speed, avg_time)

    def plot_data(self):
        self.performance_data.plot_data()

class MiningThread(QThread):
    yenilog = pyqtSignal(str)
    yanlistoken = pyqtSignal(float, float)

    def __init__(self):
        super().__init__()
        self.mining = False
        self.valid_token_interval = 25

    def generate_fake_token(self, length=34):
        return ''.join(random.choices(base58forCryptoAlfa, k=length))

    def generate_valid_token(self, length=34):
        btc_value = round(random.uniform(0.01, 0.03), 5)  # ? Here you can determine how much BTC you will earn in a certain period of time.
        usd_value = round(btc_value * fetch_real_time_btc_price(), 2)
        return (btc_value, usd_value)

    def run(self):
        last_valid_time = time.time()
        while self.mining:
            token = self.generate_fake_token()
            current_time = time.time()

            if current_time - last_valid_time >= self.valid_token_interval:
                btc_value, usd_value = self.generate_valid_token()
                log_message = f"<font color='green'>VALID {token} - {btc_value} BTC - ${usd_value}</font>"
                self.yanlistoken.emit(btc_value, usd_value)
                last_valid_time = current_time
            else:
                log_message = f"<font color='red'>INVALID {token} - $0.00</font>"

            self.yenilog.emit(log_message)
            time.sleep(0.03)

class GPUUpdateThread(QThread):
    update_gpu_signal = pyqtSignal(str)

    def run(self):
        while True:
            gpu_info = "" # none
            for i in range(4):
                model = random.choice(fakeGPUSl1ve709)
                temp = random.randint(63, 80)  # TODO, GPU temperature setting can be changed manually here
                load = random.uniform(0, 1)
                mem_total = random.randint(12000, 24000)
                mem_used = random.randint(0, mem_total)
                mem_free = mem_total - mem_used
                
                gpu_info += f"{model}\n   Temp: {temp} °C\n   Load: {load * 100:.1f}%\n"
                gpu_info += f"   Total Mem: {mem_total} MB\n   Used Mem: {mem_used} MB\n   Free Mem: {mem_free} MB\n\n"
                
            self.update_gpu_signal.emit(gpu_info)
            time.sleep(2)

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setGeometry(200, 200, 400, 300)
        
        layout = QFormLayout()

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark"]) 
        layout.addRow("Theme:", self.theme_combo)

        self.apply_button = QPushButton("Apply")
        self.apply_button.clicked.connect(self.apply_settings)
        layout.addWidget(self.apply_button)

        self.setLayout(layout)

    def apply_settings(self):
        theme = self.theme_combo.currentText()
        print(f"Applying theme: {theme}")

class FakeMiningApp(QMainWindow):   # ! index page 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CryptoFactory.exe")  # window name
        self.setGeometry(100, 100, 1400, 900)

        main_layout = QVBoxLayout()
        info_layout = QVBoxLayout()
        gpu_layout = QVBoxLayout()
        wallet_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.title_label = QLabel("₿ CryptoFactory  VER 1.6 ₿")  # main title
        self.title_label.setFont(QFont('Arial', 24, QFont.Bold))
        self.title_label.setStyleSheet("color: #D32F2F;")
        main_layout.addWidget(self.title_label)

        self.btc_label = QLabel("BTC to USD: $58397.00") # 1 BTC to Dollar (change)
        self.btc_label.setFont(QFont('Arial', 14))
        self.btc_label.setStyleSheet("color: #F7931A;")
        info_layout.addWidget(self.btc_label)

        self.current_btc_label = QLabel("BTC Value: 0,0025 BTC") # fake btc currently in our account (0,0025)
        self.current_btc_label.setFont(QFont('Arial', 14))
        self.current_btc_label.setStyleSheet("color: #F7931A;")
        info_layout.addWidget(self.current_btc_label)

        self.current_usd_label = QLabel("USD Value: $146.97") # fake dollar in wallet
        self.current_usd_label.setFont(QFont('Arial', 14))
        self.current_usd_label.setStyleSheet("color: #90EE90;")
        info_layout.addWidget(self.current_usd_label)

        self.mining_duration_label = QLabel("Mining Duration: 0s") 
        self.mining_duration_label.setFont(QFont('Arial', 12))
        self.mining_duration_label.setStyleSheet("color: #C0C0C0;")
        info_layout.addWidget(self.mining_duration_label)

        main_layout.addLayout(info_layout)

        self.gpu_label = QLabel("GPU Information")
        self.gpu_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.gpu_label.setStyleSheet("color: #8C8C8C;")
        gpu_layout.addWidget(self.gpu_label)

        self.gpu_text = QTextEdit()
        self.gpu_text.setStyleSheet("background-color: rgba(30, 30, 30, 0.8); color: #6D6D6D;")
        self.gpu_text.setFont(QFont('Arial', 10))
        self.gpu_text.setReadOnly(True)
        gpu_layout.addWidget(self.gpu_text)

        main_layout.addLayout(gpu_layout)

        self.wallet_label = QLabel("Wallet and Transactions")
        self.wallet_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.wallet_label.setStyleSheet("color: #8C8C8C ;")
        wallet_layout.addWidget(self.wallet_label)

        self.wallet_text = QTextEdit()
        self.wallet_text.setStyleSheet("background-color: rgba(30, 30, 30, 0.8); color: #6D6D6D;")
        self.wallet_text.setFont(QFont('Arial', 10))
        self.wallet_text.setReadOnly(True)
        self.wallet_text.setTextInteractionFlags(Qt.TextBrowserInteraction)
        wallet_layout.addWidget(self.wallet_text)

        main_layout.addLayout(wallet_layout)

        self.start_button = QPushButton("RUN") # start button
        self.start_button.setStyleSheet("background-color: #4CAF50; color: #FFFFFF; font: bold 12pt Arial;")
        self.start_button.clicked.connect(self.start_mining)
        button_layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton("STOP") # stop button
        self.stop_button.setStyleSheet("background-color: #f44336; color: #FFFFFF; font: bold 12pt Arial;")
        self.stop_button.clicked.connect(self.stop_mining)
        button_layout.addWidget(self.stop_button)

        self.about_button = QPushButton("About") 
        self.about_button.setStyleSheet("background-color: #A9A9A9; color: #FFFFFF; font: bold 12pt Arial;")
        self.about_button.setFixedSize(100, 30)
        self.about_button.clicked.connect(self.show_about_message)
        button_layout.addWidget(self.about_button)

        self.settings_button = QPushButton("Settings")
        self.settings_button.setStyleSheet("background-color: #A9A9A9; color: #001F3F; font: bold 12pt Arial;")
        self.settings_button.setFixedSize(100, 30)
        self.settings_button.clicked.connect(self.open_settings_window)
        button_layout.addWidget(self.settings_button)

        self.support_button = QPushButton("Support")
        self.support_button.setStyleSheet("background-color: #A9A9A9; color: #6C6C6C; font: bold 12pt Arial;")
        self.support_button.setFixedSize(100, 30)
        self.support_button.clicked.connect(self.open_support_link)
        button_layout.addWidget(self.support_button)

        self.stats_button = QPushButton("Performance Data")  # realistic Performance-Data
        self.stats_button.setStyleSheet("background-color: #A9A9A9; color: #001F3F; font: bold 12pt Arial;")
        self.stats_button.setFixedSize(150, 30)
        self.stats_button.clicked.connect(self.show_stats_window)
        button_layout.addWidget(self.stats_button)

        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.mining = False
        self.mining_thread = None
        self.gpu_update_thread = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_mining_duration)

        self.total_btc = 0.0
        self.total_usd = 0.0

        self.start_datetime = QDateTime(2024, 8, 12, 17, 46, 2) 

        self.performance_data = PerformanceData()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pixmap = QPixmap('background.jpg')  # ! app background
        if pixmap.isNull():
            print("picture upload error")
        else:
            painter.drawPixmap(self.rect(), pixmap)

    def update_btc_and_usd(self):
        self.current_btc_label.setText(f"BTC Value: {self.total_btc:.5f} BTC")
        self.current_usd_label.setText(f"USD Value: ${self.total_usd:.2f}")

    def update_gpu_info(self, gpu_info):
        self.gpu_text.setPlainText(gpu_info)

    def start_mining(self):
        if not self.mining:
            self.mining = True
            self.start_time = self.start_datetime.toSecsSinceEpoch()

            self.mining_thread = MiningThread()
            self.mining_thread.yenilog.connect(self.append_to_wallet_text)
            self.mining_thread.yanlistoken.connect(self.add_valid_token_value)
            self.mining_thread.mining = True
            self.mining_thread.start()

            self.gpu_update_thread = GPUUpdateThread()
            self.gpu_update_thread.update_gpu_signal.connect(self.update_gpu_info)
            self.gpu_update_thread.start()

            self.timer.start(1000)

    def stop_mining(self):
        if self.mining:
            self.mining = False
            if self.mining_thread:
                self.mining_thread.mining = False
                self.mining_thread.quit()
                self.mining_thread.wait()
            if self.gpu_update_thread:
                self.gpu_update_thread.quit()
                self.gpu_update_thread.wait()
            self.timer.stop()

    def update_mining_duration(self):
        elapsed_time = QDateTime.currentDateTime().toSecsSinceEpoch() - self.start_time
        seconds = elapsed_time % 60
        minutes = (elapsed_time // 60) % 60
        hours = (elapsed_time // 3600) % 24
        days = elapsed_time // 86400
        self.mining_duration_label.setText(f"Mining Duration: {days}d {hours}h {minutes}m {seconds}s")

    def append_to_wallet_text(self, log_message):
        self.wallet_text.append(log_message)

    def add_valid_token_value(self, btc_value, usd_value):
        self.total_btc += btc_value
        self.total_usd += usd_value
        self.update_btc_and_usd()

    def open_support_link(self):
        webbrowser.open("https://discord.com/invite/")  # my discord server for support (closed)

    def show_about_message(self):
        webbrowser.open("https://l1ve709.com") # my website for support

    def show_stats_window(self):
        self.stats_window = MiningStatsWindow(self.performance_data)
        self.stats_window.exec_()

    def open_settings_window(self):
        self.settings_window = SettingsWindow()
        self.settings_window.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FakeMiningApp()
    window.show()
    sys.exit(app.exec_())
