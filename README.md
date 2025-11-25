# fractree

Python 3 fractal tree generator with TKINTER interface and unit tests

## Project Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gabrielbrise/fractree.git
   cd fractree
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv

   # On Linux/macOS:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install system dependencies (Linux only):**
   ```bash
   sudo apt update
   sudo apt install libcairo2-dev pkg-config python3-dev
   ```

### Running the Application

To run the fractal tree generator:

```bash
python fractreeUI.py
```

The application will open a GUI where you can:

- Adjust tree parameters (angle, levels, randomness)
- Generate multiple trees
- Export trees to SVG format
- Control drawing speed

## Running Unit Tests

To run the unit tests:

```bash
pytest test_twig.py
```

## Dependencies

- **Pillow** - Image processing and display
- **cairosvg** - SVG export functionality
- **pytest** - Unit testing framework

## Cross-Platform Compatibility

This project works on:

- ✅ Linux (tested)
- ✅ macOS
- ✅ Windows

The code automatically handles platform-specific differences for window management and dependencies.
