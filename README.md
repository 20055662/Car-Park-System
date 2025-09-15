# CarPark Management System 🅿️

A Python-based simulation of a smart car park system, demonstrating object-oriented programming, abstraction, and basic software design principles.

---

## Overview
This project simulates a car park with sensors, displays, and logging. It shows how vehicles enter and exit, how available bays are updated in real-time, and how the system tracks all activity. It demonstrates **Python OOP, abstraction, composition, and file I/O** in a structured project.

---

## Key Skills & Concepts Demonstrated
- **Python Object-Oriented Programming (OOP)**  
  Classes, inheritance, abstract base classes, and encapsulation.
- **Software Design & Architecture**  
  Composition of objects (`CarPark` contains `Sensor` and `Display` objects).
- **File Handling**  
  Logging vehicle activity and saving/loading configuration using JSON.
- **Abstraction**  
  Abstract `Sensor` class with concrete `EntrySensor` and `ExitSensor`.
- **Real-time Data Simulation**  
  Detecting cars and updating displays programmatically.
- **Version Control Practices**  
  Suggested semantic commit messages: `feat`, `fix`, `refactor`.

---

## Technologies Used
- Python 3.10+
- OOP principles: classes, inheritance, abstract base classes
- File I/O (`open`, `Path`)
- JSON configuration handling
- Random module for simulating vehicle plates

---
## Classes & Components

### `CarPark`
- Manages vehicles, sensors, and displays
- Keeps track of parked cars and available bays
- Handles logging of vehicle activity
- Updates registered display components

### `Sensor` (Abstract Base Class)
- Base class for all sensors
- Has methods for detecting vehicles
- Subclasses must implement `update_car_park(plate)`

#### `EntrySensor`
- Detects incoming vehicles
- Adds cars to the car park

#### `ExitSensor`
- Detects outgoing vehicles
- Removes cars from the car park

### `Display`
- Shows messages and current car park data
- Updates automatically when `CarPark` state changes

---