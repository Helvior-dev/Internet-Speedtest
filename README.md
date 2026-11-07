# Internet Speedtest

A small interactive Python CLI that measures download speed, upload speed, and ping using Speedtest.net servers.

## Features

- Selects a nearby test server with the lowest latency.
- Reports download and upload rates in Mbps and ping in milliseconds.
- Shows an ASCII spinner while each test runs.
- Uses the secure mode provided by `speedtest-cli`.

## Requirements

- Python 3.8 or newer
- Packages listed in `requirements.txt`
- An active internet connection

## Setup

Clone the repository and enter its directory:

```bash
git clone https://github.com/Helvior-dev/Internet-Speedtest.git
cd Internet-Speedtest
```

Create and activate a virtual environment, then install dependencies:

- Windows PowerShell:

  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  ```

- Linux or macOS:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

## Usage

Run the test from a terminal:

```bash
python internet_speedtest.py
```

The test transfers data to a Speedtest.net server. Results vary with server load and network conditions, and the test may use a noticeable amount of data.

## Tests

Run the offline tests without starting a network speed test:

```bash
python -m unittest discover -s tests -v
```
