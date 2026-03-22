from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")

        grid = QGridLayout()

        distance_label = QLabel("Distance:")
        self.distance_box = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_box = QLineEdit()

        calculate_button = QPushButton("Calculate")
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0,0)
        grid.addWidget(self.distance_box, 0,1)
        grid.addWidget(time_label, 1,0)
        grid.addWidget(self.time_box, 1,1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        self.setLayout(grid)



app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())