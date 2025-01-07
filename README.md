# Chatbot

A Python-based chatbot named **Buzz** that interacts with users via a graphical user interface (GUI). Buzz supports natural language queries, email functionality, weather updates, news headlines, website browsing, and system commands.

## Features

- **Interactive Chat**: Responds to user queries with a conversational approach.
- **Email Automation**: Send emails through Gmail directly from the chatbot.
- **Weather Updates**: Fetches real-time weather details for any city.
- **News Headlines**: Displays top news from the Times of India.
- **Web Browsing**: Opens websites directly.
- **System Commands**: Execute system-level commands like shutdown, restart, and sleep.
- **Gemini API Integration**: Provides intelligent and dynamic responses using Google Generative AI.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/harsh24mi/Chatbot.git
   cd Chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables for API keys (if applicable):
   - `WEATHER_API_KEY`
   - `NEWS_API_KEY`
   - `GMAIL_API_CREDENTIALS`
   - `GENAI_API_KEY`

4. Run the chatbot:
   ```bash
   python main.py
   ```

---

## Usage

1. Launch the chatbot by running `main.py`.
2. Use the GUI interface to interact with Buzz.
3. Supported queries and commands:
   - "Send mail": Automates email sending.
   - "What's the weather in [city]?": Fetches real-time weather.
   - "Show me news": Displays the latest headlines.
   - "Open website [name]": Launches a website in the browser.
   - System commands: "shutdown," "restart," "lock," and more.

---

## Project Structure

```
Chatbot/
├── main.py            # Entry point of the chatbot
├── requirements.txt   # Dependencies
├── README.md          # Documentation
├── utils/             # Utility scripts and helpers
│   ├── nlp.py         # Natural Language Processing logic
│   ├── email.py       # Email automation logic
│   ├── api.py         # API integration logic
│   └── gui.py         # GUI implementation with tkinter
└── tests/             # Test scripts
    ├── test_nlp.py
    ├── test_email.py
    └── test_api.py
```

---

## Prerequisites

Before using this chatbot, ensure you have the following:

- Python 3.8+
- API keys for Weather API, News API, and Google Generative AI.
- Gmail account credentials for email functionality.
- Installed required libraries (use `pip install -r requirements.txt`).

---

## Tech Stack

- **Programming Language**: Python
- **Libraries**:
  - `tkinter`: GUI development
  - `requests`: API calls
  - `smtplib`: Email automation
  - `os`: System commands
- **APIs**:
  - Weather API
  - Gmail API
  - News API
  - Google Generative AI (Gemini)

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For queries or suggestions, reach out at:

- **Author**: Harsh24mi
- **GitHub**: [harsh24mi](https://github.com/harsh24mi)

