\<div align="center"\>
\<img src="[https://img.shields.io/badge/python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)" alt="Python"\>
\<img src="[https://img.shields.io/badge/tk-2C2C2C?style=for-the-badge\&logo=tkinter\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/tk-2C2C2C%3Fstyle%3Dfor-the-badge%26logo%3Dtkinter%26logoColor%3Dwhite)" alt="Tkinter"\>
\</div\>

# YouTube Channel Data Scraper

A simple Python application with a graphical user interface (GUI) to scrape video data from a YouTube channel and save it to a CSV file.

-----

## 📜 Table of Contents

  - [🚀 Overview](https://www.google.com/search?q=%23-overview)
  - [✨ Features](https://www.google.com/search?q=%23-features)
  - [📂 Project Structure](https://www.google.com/search?q=%23-project-structure)
  - [🏁 Getting Started](https://www.google.com/search?q=%23-getting-started)
      - [Prerequisites](https://www.google.com/search?q=%23prerequisites)
      - [Installation](https://www.google.com/search?q=%23installation)
  - [🤝 Contributing](https://www.google.com/search?q=%23-contributing)
  - [📄 License](https://www.google.com/search?q=%23-license)

-----

## 🚀 Overview

This project provides a user-friendly tool to extract information about all the videos on a given YouTube channel. The application is built with Python and uses the Tkinter library for the GUI. It fetches data using the YouTube Data API v3 and saves it in a structured CSV file for easy analysis.

-----

## ✨ Features

  - **GUI:** A simple and intuitive graphical user interface built with Tkinter.
  - **Channel URL Support:** It can resolve channel IDs from various YouTube URL formats (e.g., `/channel/`, `/user/`, and `@handle`).
  - **Data Extraction:** Scrapes video titles, descriptions, publication dates, and video URLs.
  - **CSV Export:** Saves the collected data into a CSV file named `channel_videos.csv`.
  - **Progress Indicator:** A progress bar and a label to show the status of the data scraping process.

-----

## 📂 Project Structure

```
/
|-- main.py         # The main Python script containing the application logic
|-- README.md       # This file
```

-----

## 🏁 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

  - Python 3.x
  - `requests` library

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/onkar-vaidya/youtube-channel-data-scraper.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd youtube-channel-data-scraper
    ```
3.  **Install the required packages:**
    ```sh
    pip install requests
    ```
4.  **Add your YouTube API Key:**
    Open `main.py` and replace `"your-API-key"` with your actual YouTube Data API v3 key.
    ```python
    API_KEY = "your-API-key"
    ```
5.  **Run the application:**
    ```sh
    python main.py
    ```

-----

## 🤝 Contributing

Contributions are welcome\! If you have suggestions for improving the application, please fork the repository and submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/NewFeature`)
3.  Commit your Changes (`git commit -m 'Add some NewFeature'`)
4.  Push to the Branch (`git push origin feature/NewFeature`)
5.  Open a Pull Request

-----

## 📄 License

This project is licensed under the ISC License.
