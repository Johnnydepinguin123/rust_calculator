# Rust Recycling Calculator Web App

A web-based calculator for determining the resources you'll receive from recycling various components in the game Rust.

## Features

- Calculate recycling yields for multiple components
- Modern, responsive web interface
- Real-time calculations
- Support for all major components:
  - Road Signs
  - Metal Pipes
  - Metal Blades
  - Metal Springs
  - SMG Bodies
  - SAR Bodies
  - Rifle Bodies
  - Sheet Metal
  - Tech Trash

## Installation

1. Make sure you have Python 3.7+ installed on your system.

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter the quantity of each component you want to recycle
2. Click the "Calculate" button
3. View the total amount of Scrap, HQM (High Quality Metal), and Metal Fragments you'll receive

## Development

The application is built with:
- Backend: Flask (Python)
- Frontend: HTML, TailwindCSS, and JavaScript
- No database required - all calculations are done in real-time

## Contributing

Feel free to submit issues and enhancement requests!
