from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        """  super().__init__() is used to call the parent class's constructor from within a child class.
        This ensures that the parent class is properly initialized, allowing the child class to inherit
        and use its attributes and methods.
        If a child class defines its own __init__ method, it overrides the parent's. Without super().__init__(),
        the parent's setup code never runs, which can lead to errors when trying to access parent attributes
        """
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")

        grid = QGridLayout()

        distance_label = QLabel("Distance:")
        self.distance_box = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Metric (km)", "Imperial (miles)"])


        time_label = QLabel("Time (hours):")
        self.time_box = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.average_speed)
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0,0)
        grid.addWidget(self.distance_box, 0,1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1,0)
        grid.addWidget(self.time_box, 1,1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        self.setLayout(grid)

    def average_speed(self):
        try:
            distance = float(self.distance_box.text())
            time = float(self.time_box.text())

            speed = distance/time

            selected_text = self.unit_combo.currentText()
            if selected_text == "Metric (km)":
                self.output_label.setText(f"Average Speed: {speed} km/ph")
            if selected_text == "Imperial (miles)":
                new_speed = distance * 0.621/time
                self.output_label.setText(f"Average Speed: {new_speed} mph")
        except ValueError:
            self.output_label.setText("Error: Please enter valid numbers!.")
        except ZeroDivisionError:
            self.output_label.setText("Error: Time cannot be zero!.")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())