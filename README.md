# Barcode Input Timing Analyzer

This Python script allows for the analysis of time intervals between barcode inputs, specifically useful for rapid barcode scanning. The script records time differences between each key press during barcode input, calculates statistics such as **minimum**, **maximum**, and **average** times, and displays the results in real-time.

## Features
- **Real-time Barcode Input**: Tracks and records key presses from barcode scanners.
- **Time Interval Analysis**: Calculates the time differences (in milliseconds) between key presses.
- **Statistics Calculation**: Provides minimum, maximum, and average time intervals for each barcode input.
- **Multiple Barcode Support**: Scan multiple barcodes continuously, with results for each barcode entry.
- **ESC Key Summary**: Pressing the ESC key will display a summary of all barcode inputs along with their timing statistics.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/barcode-input-analyzer.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install pynput pyautogui pyperclip
   ```

## Usage

1. Run the script:
   ```bash
   python barcode_analyzer.py
   ```

2. **Active Window**: Ensure that Notepad++ or your desired text editor is open and active.
3. **Scan Barcodes**: Scan barcodes with your barcode scanner. The script will automatically track key presses and record time intervals.
4. **ESC Key for Summary**: After scanning, press the ESC key to output the results into the active text editor.

## Example Output

```
7 karakter: 30.37 32.05 31.33 30.76 16.57 46.8 31.89 ms | Min: 16.57 ms, Max: 46.8 ms, Ortalama: 31.39 ms
5 karakter: 29.0 31.2 30.6 30.4 16.1 ms | Min: 16.1 ms, Max: 31.2 ms, Ortalama: 27.86 ms
Sonuçlar tamamlandı.
```

## Dependencies
- **pynput**: For capturing keyboard events.
- **pyautogui**: For simulating keyboard actions such as pasting the results.
- **pyperclip**: For copying the results to the clipboard.

## Contributing

If you'd like to contribute to the project, feel free to submit pull requests or open issues for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
