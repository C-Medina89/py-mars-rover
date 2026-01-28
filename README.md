# Mars Rover Project

A Python implementation of the Mars Rover coding challenge, built with test-driven development and clean architecture principles.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Design Decisions](#design-decisions)
- [Example](#example)
- [Contributing](#contributing)


## Overview

This project simulates NASA's Mars Rover mission control system. Rovers are deployed on a rectangular plateau and navigate using a series of movement instructions. The system handles multiple rovers moving sequentially, with collision and boundary detection.

## Features

- **Layered Architecture**: Separation of input parsing from business logic
- **Test-Driven Development**: Comprehensive test suite with 100% coverage
- **Error Handling**: Robust validation for invalid inputs and movements
- **Multiple Rover Support**: Sequential movement with collision avoidance
- **Type Safety**: Custom data types and enums for compass directions and instructions
- **Extensible Design**: Easy to add new features or modify input formats

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/C-Medina89/py-mars-rover.git
   cd py-mars-rover


2. python -m venv venv (Create a virtual environment)
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. pip install pytest  (Install dependencies)


### Usage
1. python main.py (Run the program with the example from the brief)

2. Expected output (
    1 3 N
    5 1 E
)

3. Custom input :
    To use custom input, modify the input_data variable in main.py. The expected format is:
    <plateau_max_x> <plateau_max_y>
    <rover1_x> <rover1_y> <rover1_direction>
    <rover1_instructions>
    <rover2_x> <rover2_y> <rover2_direction>
    <rover2_instructions>
    ...

4. Input Format Details:

    Plateau Size: Two integers representing maximum x and y coordinates (0-based grid)

    Rover Position: Two integers and a direction character (N, S, E, W)

    Instructions: String of letters (L, R, M) without spaces

5. Output Format:
    For each rover, the program outputs its final position:
    <x_coordinate> <y_coordinate> <facing_direction>

## Project Structure

```
py-mars-rover/
├── input_layer/                    # Input parsing layer
│   ├── input_types/                # Custom data types
│   │   ├── compass_directions.py   # CompassDirection enum (N, S, E, W)
│   │   ├── instructions.py         # Instruction enum (L, R, M)
│   │   ├── plateau_size.py         # PlateauSize dataclass
│   │   └── position.py             # Position dataclass
│   └── parsers/                    # String parsers
│       ├── instruction_parser.py   # Converts "LMR" to [Instruction.LEFT, ...]
│       ├── plateau_parser.py       # Converts "5 5" to PlateauSize
│       └── position_parser.py      # Converts "1 2 N" to Position
├── logic_layer/                    # Business logic layer
│   ├── plateau.py                  # Plateau with boundary checking
│   ├── rover.py                    # Rover movement and rotation
│   └── mission_control.py          # Coordinates multiple rovers
├── tests/                          # Test suite
│   ├── input_layer_tests/          # Tests for data types
│   ├── parser_tests/               # Tests for parsers
│   ├── logic_layer_tests/          # Tests for business logic
│   └── test_layer_integration.py   # End-to-end integration tests
├── main.py                         # Program entry point
├── README.md                       # This documentation
└── .gitignore                      # Git ignore rules
```



### Running Tests

1. Run all tests :
    pytest tests/

2. Run specific test categories :

    pytest tests/input_layer_tests/      # Data type tests
    pytest tests/parser_tests/           # Parser tests
    pytest tests/logic_layer_tests/      # Business logic tests
    pytest tests/test_layer_integration.py  # Integration tests


### Design Decisions

1. ## Layered Architecture
    The project separates concerns into distinct layers:

    - Input Layer: Handles parsing and validation of raw input strings

    - Logic Layer: Contains business logic for rover movement and plateau management

    This separation allows either layer to be modified independently, making the system more maintainable and testable.

2. ## Custom Data Types
    Instead of using primitive types (strings, integers), the project defines:

    - CompassDirection enum for direction validation

    - Instruction enum for movement command validation

    - Position and PlateauSize dataclasses for structured data

3. ## Collision and Boundary Handling
    - Rovers cannot move outside the plateau boundaries

    - Rovers cannot occupy the same position simultaneously

    - Invalid moves are silently ignored (rovers stay in place)

4. ## Sequential Movement
    Rovers move in the order they are deployed. Each rover must complete its entire instruction sequence before the next rover begins moving.

### Example

## Input

    text
    5 5
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM

## Rover 1 Journey

- Starting at (1, 2) facing North

- Instructions: LMLMLMLMM

- Path: Turn Left → Move West → Turn Left → Move South → Turn Left → Move East → Turn Left → Move North → Move North

- Final position: (1, 3) facing North

## Rover 2 Journey

- Starting at (3, 3) facing East

- Instructions: MMRMMRMRRM

- Path: Move East → Move East → Turn Right → Move South → Move South → Turn Right → Move West → Turn Right → Turn Right → Move West

- Final position: (5, 1) facing East

## Output

    text
    1 3 N
    5 1 E


### Contributing

- Fork the repository

- Create a feature branch: git checkout -b feature-name

- Make your changes and add tests

- Run the test suite to ensure all tests pass

- Commit your changes: git commit -am 'Add some feature'

- Push to the branch: git push origin feature-name

- Submit a pull request