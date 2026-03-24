# 🏎️ PyQt6 Average Speed Calculator

A lightweight, robust Desktop Graphical User Interface (GUI) application built with Python and PyQt6. This tool calculates average speed based on distance and time inputs, seamlessly handling both Metric (km/h) and Imperial (mph) unit conversions.

<img width="1108" height="627" alt="Speed Calculator" src="https://github.com/user-attachments/assets/78e21466-e600-4ac4-8bbc-10f01889448f" />


## 🧠 Engineering Features
Unlike basic script calculators, this application is designed with strict user-input validation and event-driven architecture:
* **Dynamic Unit Conversion:** Utilizes `QComboBox` to switch logic between Metric and Imperial outputs without requiring page reloads.
* **Bulletproof Error Handling:** * Implements `try-except` blocks to catch `ValueError` (e.g., if a user types text instead of numbers).
  * Prevents `ZeroDivisionError` (ensuring the app doesn't crash if Time is set to 0).
* **Responsive GUI:** Built using `QGridLayout` for a clean, scalable, and intuitive interface.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Framework:** PyQt6
* **Architecture:** Object-Oriented Programming (OOP)

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Nayanxyz/Speed-Calculator-PyQt6.git 
cd Speed-Calculator-PyQt6
```
**2. Install Dependencies**
```bash
pip install PyQt6
```

**3. Execute the Application**
```bash
python SpeedCalculator.py
```

