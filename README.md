# Mars Rover Project

A Python implementation of the Mars Rover coding challenge, built with test-driven development and clean architecture principles.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start Guide](#-quick-start-guide)
- [Interactive Terminal Usage](#interactive-terminal-usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Design Decisions](#design-decisions)
- [UI Features & Design](#ui-features--design)
- [Example](#example)
- [Command Line Options](#command-line-options)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#contributing)
- [Acknowledgments](#-acknowledgments)

## Overview

This project simulates NASA's Mars Rover mission control system. Rovers are deployed on a rectangular plateau and navigate using a series of movement instructions. The system handles multiple rovers moving sequentially, with collision and boundary detection.

## Features

- **Layered Architecture**: Separation of input parsing from business logic
- **Test-Driven Development**: Comprehensive test suite with 100% coverage
- **Error Handling**: Robust validation for invalid inputs and movements
- **Multiple Rover Support**: Sequential movement with collision avoidance
- **Type Safety**: Custom data types and enums for compass directions and instructions
- **Extensible Design**: Easy to add new features or modify input formats
- **Interactive Terminal UI**: User-friendly command-line interface with step-by-step guidance
- **Visual Grid Display**: Optional graphical representation of rover positions using ASCII art
- **Real-time Visualization**: Watch rovers move step-by-step with visual feedback
- **Save/Load Missions**: Export results to text files for later reference

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/C-Medina89/py-mars-rover.git
   cd py-mars-rover
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install pytest  # Only pytest is required for testing
   ```

## Quick Start Guide

### For First-Time Users
1. **Clone and navigate** to the project:
   ```bash
   git clone <repository-url>
   cd py-mars-rover
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Follow the prompts**:
   - Press `y` for visual display (recommended)
   - Enter `5 5` for plateau size
   - Press `Enter` to use example rover position
   - Press `Enter` to use example instructions
   - Watch the rover move on the visual grid!

### For Developers
1. **Run all tests**:
   ```bash
   pytest tests/
   ```

2. **Test specific component**:
   ```bash
   pytest tests/logic_layer_tests/test_rover.py
   ```

3. **Run integration test**:
   ```bash
   pytest tests/test_layer_integration.py
   ```

## Interactive Terminal Usage

### Starting the Application
```bash
python main.py
```

### Example Interactive Session
```
==================================================
🚀 MARS ROVER MISSION CONTROL
==================================================

👁️  VISUAL DISPLAY OPTION
-------------------------
Enable visual display of rovers? (y/n): y

📐 STEP 1: SETUP PLATEAU
------------------------------
Enter plateau size (format: 'width height' e.g., '5 5'): 5 5

👁️  Visual display enabled!

========================================
🛰️  Initial Empty Plateau
========================================
Y
5 [.][.][.][.][.][.]
4 [.][.][.][.][.][.]
3 [.][.][.][.][.][.]
2 [.][.][.][.][.][.]
1 [.][.][.][.][.][.]
0 [.][.][.][.][.][.]
     0  1  2  3  4  5  X

Legend: ↑=N ↓=S →=E ←=W .=Empty
========================================

🤖 STEP 2: DEPLOY ROVERS
------------------------------

Rover #1
Enter Rover #1 starting position (format: 'x y direction' e.g., '1 2 N'): 1 2 N
Enter Rover #1 instructions (L=Left, R=Right, M=Move): LMLMLMLMM

✓ Rover #1 deployed and moved!
  Final position: 1 3 N

Add another rover? (y/n): y

Rover #2
Enter Rover #2 starting position (format: 'x y direction' e.g., '1 2 N'): 3 3 E
Enter Rover #2 instructions (L=Left, R=Right, M=Move): MMRMMRMRRM

✓ Rover #2 deployed and moved!
  Final position: 5 1 E

Add another rover? (y/n): n

========================================
🛰️  Final Rover Positions
========================================
Y
5 [.][.][.][.][.][.]
4 [.][.][.][.][.][.]
3 [↑][.][.][.][.][.]
2 [.][.][.][.][.][.]
1 [.][.][.][.][→][.]
0 [.][.][.][.][.][.]
     0  1  2  3  4  5  X

Legend: ↑=N ↓=S →=E ←=W .=Empty
========================================

📊 MISSION RESULTS
========================================

Total rovers deployed: 2

Final positions:
--------------------
Rover #1: 1 3 N
Rover #2: 5 1 E

Save results to file? (y/n): y
Enter filename (default: 'results.txt'): mission_001.txt
✓ Results saved to mission_001.txt
```

### Available Commands
- Press **Enter** to use default values for first rover
- Type **'y'** or **'n'** for yes/no questions
- Enter **empty input** for position/instructions to use example values
- **Ctrl+C** to abort mission at any time

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
│       ├── instruction_parser.py   # Parse movement instructions
│       ├── plateau_parser.py       # Parse plateau dimensions
│       ├── position_parser.py      # Parse rover positions
├── logic_layer/                    # Business logic layer
│   ├── plateau.py                  # Plateau with bounds checking
│   ├── rover.py                    # Rover movement logic
│   └── mission_control.py          # Coordinate multiple rovers
├── ui_layer/                       # NEW: User interface layer
│   ├── terminal_ui.py              # Interactive terminal interface
│             
├── tests/                          # Test suite
│   ├── input_layer_tests/          # Tests for data types
│   ├── parser_tests/               # Tests for parsers
│   ├── logic_layer_tests/          # Tests for business logic
│   └── test_layer_integration.py   # End-to-end integration tests
├── main.py                         # Program entry point
├── README.md                       # This documentation
└── .gitignore                      # Git ignore rules
```

## Running Tests

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test Categories
```bash
pytest tests/input_layer_tests/      # Data type tests
pytest tests/parser_tests/           # Parser tests
pytest tests/logic_layer_tests/      # Business logic tests
pytest tests/test_layer_integration.py  # Integration tests
```

### Run Tests with Coverage
```bash
pytest --cov=. tests/
```

## Design Decisions

### 1. Layered Architecture
The project separates concerns into distinct layers:

- **Input Layer**: Handles parsing and validation of raw input strings
- **Logic Layer**: Contains business logic for rover movement and plateau management
- **UI Layer**: Manages user interaction and display (newly added)

This separation allows each layer to be modified independently, making the system more maintainable and testable.

### 2. Custom Data Types
Instead of using primitive types (strings, integers), the project defines:

- `CompassDirection` enum for direction validation
- `Instruction` enum for movement command validation
- `Position` and `PlateauSize` dataclasses for structured data

### 3. Collision and Boundary Handling
- Rovers cannot move outside the plateau boundaries
- Rovers cannot occupy the same position simultaneously
- Invalid moves are silently ignored (rovers stay in place)

### 4. Sequential Movement
Rovers move in the order they are deployed. Each rover must complete its entire instruction sequence before the next rover begins moving.

## UI Features & Design

### Visual Display System
The application includes an optional ASCII-based visual display that shows:
- **Grid coordinates** with proper orientation (y=0 at bottom)
- **Rover positions** using directional arrows (↑ ↓ → ←)
- **Empty cells** represented as dots (.)
- **Real-time updates** as rovers move

### User Experience Features
1. **Progressive Disclosure**: Only asks for needed information
2. **Smart Defaults**: Press Enter to use example values
3. **Error Recovery**: Clear error messages with retry options
4. **Confirmation Prompts**: Yes/No questions with validation
5. **Mission Saving**: Export results to text files

### Input Validation
- **Plateau size**: Must be positive integers
- **Rover positions**: Must be within plateau bounds
- **Directions**: Must be N, S, E, or W
- **Instructions**: Invalid characters are ignored
- **Collisions**: Prevent rovers from occupying same space

## Example

### Input (via interactive terminal)
```
Plateau: 5 5
Rover 1: Start at (1, 2) facing North with instructions "LMLMLMLMM"
Rover 2: Start at (3, 3) facing East with instructions "MMRMMRMRRM"
```

### Visual Output
```
========================================
🛰️  Final Rover Positions
========================================
Y
5 [.][.][.][.][.][.]
4 [.][.][.][.][.][.]
3 [↑][.][.][.][.][.]   ← Rover 1 at (1,3) facing North
2 [.][.][.][.][.][.]
1 [.][.][.][.][→][.]   ← Rover 2 at (5,1) facing East
0 [.][.][.][.][.][.]
     0  1  2  3  4  5  X
```

### Text Output
```
1 3 N
5 1 E
```

## Command Line Options

### Interactive Mode (Default)
```bash
python main.py
```

### Direct Python Execution
```python
from ui_layer.terminal_ui import TerminalUI
ui = TerminalUI()
ui.run()
```

## 🔧 Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'ui_layer'"**
   ```bash
   # Make sure you're in the project root directory
   pwd  # Should show: /path/to/py-mars-rover
   
   # Check ui_layer folder exists
   ls -la ui_layer/
   ```

2. **Visual display looks scrambled**
   - Ensure your terminal supports UTF-8 characters
   - Try increasing terminal window size
   - Disable visual mode with 'n' when prompted

3. **Rover not moving as expected**
   - Check that coordinates are within plateau bounds
   - Verify instructions use only L, R, M characters
   - Ensure no other rover is blocking the path

4. **Tests failing**
   ```bash
   # Run with verbose output
   pytest tests/ -v
   
   # Run specific failing test
   pytest tests/test_file.py::test_function_name -v
   ```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the test suite to ensure all tests pass
5. Commit your changes: `git commit -am 'Add some feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## Acknowledgments

- **Mars Rover Kata**: Original programming challenge
- **NASA Mars Exploration Program**: Real-world inspiration
- **Test-Driven Development**: Methodology for robust code
- **Clean Architecture**: Principles for maintainable design
- **Python Community**: For excellent tools and libraries

---

## Learning Outcomes

This project demonstrates:
1. **Clean Architecture** with separated layers
2. **Test-Driven Development** practices
3. **User Experience Design** for CLI applications
4. **Visualization Techniques** in terminal environments
5. **Error Handling** and input validation strategies
6. **Professional Documentation** practices

---

