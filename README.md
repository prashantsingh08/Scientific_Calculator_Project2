# Scientific Calculator

A desktop scientific calculator built with Python and the Tkinter GUI library. It provides basic arithmetic operations and common scientific functions in a responsive, modern dark interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Interface](#interface)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Operations](#supported-operations)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Overview

**Scientific Calculator** is a graphical calculator application developed in Python. The project demonstrates GUI development with Tkinter, expression handling, mathematical functions, event-driven programming, and responsive grid layout.

The application supports standard arithmetic, parentheses, powers, percentages, square roots, base-10 logarithms, trigonometry in degree mode, and constants such as π and e.

## Features

- Modern dark-themed interface
- Responsive 5-column grid layout
- Addition, subtraction, multiplication, and division
- Parentheses for grouping expressions
- Exponentiation
- Percentage calculations
- Square root
- Base-10 logarithm
- Sine, cosine, and tangent functions
- Trigonometric calculations in degree mode
- Mathematical constants: π and e
- Last-answer (`Ans`) support
- Clear (`C`) and delete (`DEL`) controls
- Error handling for invalid expressions
- Minimum application window size for consistent usability

## Interface

The calculator uses a configurable Tkinter grid containing:

- One right-aligned expression display
- 30 interactive calculator buttons
- A dark charcoal window background
- Colored button groups for numbers, operators, scientific functions, and controls

| Button color | Purpose |
|---|---|
| Dark gray | Numbers and decimal point |
| Blue | Arithmetic operators and exponent/percentage |
| Purple | Scientific functions and constants |
| Red | Clear and delete controls |
| Green | Equals button |
| Teal | Previous answer |

## Technologies Used

- **Python 3** — application logic
- **Tkinter** — desktop graphical interface
- **Math module** — trigonometric, logarithmic, square-root, π, and e operations

## Requirements

- Python 3.8 or newer
- Tkinter included with the Python installation

Tkinter is bundled with standard Python installations on most platforms. On some Linux distributions, it may need to be installed separately.

### Verify Python

```bash
python --version
```

### Verify Tkinter

```bash
python -c "import tkinter"
```

If the command prints no errors, Tkinter is available.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/prashantsingh08/Scientific_Calculator_Project2.git
cd Scientific_Calculator_Project2
```

### 2. Run the application

```bash
python scien_cal.py
```

On some systems, use:

```bash
python3 scien_cal.py
```

No third-party Python packages are required.

## Usage

1. Launch `scien_cal.py`.
2. Click number and operator buttons to build an expression.
3. Use scientific buttons for functions and constants.
4. Press `=` to evaluate the expression.
5. Press `C` to clear the entire expression.
6. Press `DEL` to remove the final character.
7. Use `Ans` to insert the most recently calculated result.

### Example Workflow

To calculate `(25 + 5) × 2`:

1. Press `(` → `25` → `+` → `5` → `)` → `*` → `2`.
2. Press `=`.
3. The display shows `60`.

To calculate the sine of 30 degrees:

1. Press `sin`.
2. Enter `30`.
3. Press `)`.
4. Press `=`.

The result is approximately `0.49999999999999994`.

## Supported Operations

| Button | Operation | Example |
|---|---|---|
| `+` | Addition | `12+8` |
| `-` | Subtraction | `20-7` |
| `*` | Multiplication | `6*9` |
| `/` | Division | `36/6` |
| `^` | Exponentiation | `2^8` |
| `%` | Percentage conversion | `50%` |
| `√` | Square root | `√(25)` |
| `log` | Base-10 logarithm | `log(100)` |
| `sin` | Sine in degrees | `sin(30)` |
| `cos` | Cosine in degrees | `cos(60)` |
| `tan` | Tangent in degrees | `tan(45)` |
| `π` | Pi constant | `π*2` |
| `e` | Euler's number | `e^2` |
| `(` `)` | Expression grouping | `(2+3)*4` |
| `Ans` | Insert last result | `Ans+10` |

### Percentage Behavior

The `%` button converts a percentage to a decimal fraction. For example:

```text
50% → 50/100 → 0.5
```

### Trigonometric Mode

Sine, cosine, and tangent interpret input in **degrees**, not radians.

For example:

- `sin(90)` evaluates to `1`
- `cos(180)` evaluates to `-1`
- `tan(45)` evaluates to approximately `1`

## Project Structure

```text
Scientific_Calculator_Project2/
├── scien_cal.py                         # Main Tkinter application
├── Scientific_Calculator_Presentation.pptx
│                                        # Project presentation
├── "Scientific Calculator"               # Placeholder repository file
└── README.md                             # Project documentation
```

## How It Works

### Application Initialization

The `ScientificCalculator` class initializes the main Tkinter window, display variable, expression string, and the previous-answer value.

### Button Handling

Every button is connected to `on_button_click()`. The method appends characters for normal input and executes special logic for:

- `C` — clears the expression
- `DEL` — deletes the last character
- `=` — evaluates the expression
- `√`, `sin`, `cos`, `tan`, and `log` — insert valid function syntax
- `π` and `e` — insert constant values
- `Ans` — inserts the previous result

### Expression Evaluation

Before evaluation, the application converts calculator symbols into Python-compatible syntax:

- `π` becomes the value of π
- `√` becomes `sqrt`
- `^` becomes `**`
- `%` becomes `/100`

It then evaluates the expression using a restricted environment with only the allowed mathematical functions. Built-ins are disabled to reduce the risk of unintended Python operations.

### Error Handling

Invalid expressions, division by zero, invalid functions, and unsupported inputs display `Error`. The stored expression is then cleared so the user can begin a new calculation.

## Limitations

- Trigonometric functions support degrees only
- There is no keyboard input handling in the current implementation
- The expression is evaluated with Python's `eval()` using a restricted environment
- Floating-point results may contain long decimal representations
- Scientific functions must include parentheses, for example `sqrt(9)` is entered as `√(9)`
- The repository does not currently contain automated tests
- The project has no formal software license

## Future Improvements

- Add keyboard shortcuts and direct keyboard input
- Add radian/degree mode switching
- Add calculation history
- Add backspace key support
- Improve input validation and parser safety
- Add parentheses and operator validation
- Format floating-point output
- Add scientific notation and more functions
- Add themes and settings
- Add unit tests and a reusable calculation engine
- Add an executable build for Windows, macOS, and Linux
- Add a license and contribution guidelines

## Contributing

Contributions, bug reports, and feature requests are welcome.

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```

4. Push the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request.

Please keep changes focused and test the application before submitting a pull request.

## License

No license is currently specified in this repository. Please contact the repository owner before using, modifying, or distributing the project for purposes that require an explicit license.

## Author

**Prashant Singh**

- GitHub: [@prashantsingh08](https://github.com/prashantsingh08)
- Repository: [Scientific_Calculator_Project2](https://github.com/prashantsingh08/Scientific_Calculator_Project2)
