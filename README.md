# Internet Speed Test ⚡

A lightweight Python CLI application to measure internet connection speed (Download, Upload, and Ping) directly from your terminal.

## 🚀 Features
- **Server Selection**: Automatically locates the nearest Speedtest.net server with the lowest latency.
- **Download & Upload Test**: Measures bandwidth speeds in Megabits per second (Mbps).
- **Ping Measurement**: Measures network response latency in milliseconds (ms).
- **Interactive Spinner**: Includes a terminal spinner animation while running benchmarks.
- **Secure Connections**: Uses HTTPS endpoints for server discovery and test execution.

## 🛠️ Installation & Setup

1. **Navigate to project directory**:
   ```bash
   cd "Speedtest"
   ```

2. **Create & activate virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run**:
   ```bash
   python internet_speedtest.py
   ```

## 📝 Output Example
```text
=============================================
 🚀 Internet Speed Test
=============================================

✅ Test completed successfully!

📥 Download Speed : 154.25 Mbps
📤 Upload Speed   : 92.40 Mbps
⚡ Ping           : 12.5 ms
```
