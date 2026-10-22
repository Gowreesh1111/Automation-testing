<div align="center">

# Python Selenium Automation

### Web testing practice projects by Gowreesh G

![Selenium Automation animated banner](auto_test/assets/selenium-automation.gif>
)

**Python** · **Selenium WebDriver** · **Browser Automation** · **Software Testing**

A beginner-friendly collection of Python scripts that automate common browser tasks, including website searches, dropdown selection, checkbox handling, login-form testing, and screenshot capture.

</div>

---

## ✨ What this project demonstrates

- Automating browser interactions with Selenium WebDriver
- Searching websites and extracting page titles or text
- Selecting options from dropdown menus
- Finding and checking checkboxes
- Submitting a sample login form and reading its status message
- Capturing browser screenshots

## 🧰 Tech stack

- Python 3
- Selenium WebDriver
- Google Chrome

## 📁 Project structure

```text
Automation-testing-main/
├── auto_test/
│   ├── lab1.py
│   ├── lab2.py
│   ├── lab3.py
│   ├── lab4.py
│   ├── lab5.py
│   ├── lab6.py
│   ├── lab7.py
│   └── google.png
├── assets/
│   └── selenium-automation.gif
└── README.md
```

## ⚙️ Setup

1. Install Python 3 and Google Chrome.
2. Install Selenium:

   ```bash
   python -m pip install selenium
   ```

3. Open a terminal in the `auto_test` folder.
4. Run any script, for example:

   ```bash
   python lab1.py
   ```

Run the other scripts by replacing `lab1.py` with `lab2.py` through `lab7.py`.

Recent Selenium versions include Selenium Manager for browser-driver management. If a script fails to launch Chrome, update Selenium and Chrome and check the error message.

## 🧪 Script overview

| Script | Purpose |
|---|---|
| `lab1.py` | Search Wikipedia for Selenium and print page text |
| `lab2.py` | Search Amazon India for laptops and print product titles |
| `lab3.py` | Select an option from a dropdown |
| `lab4.py` | Find and check checkboxes |
| `lab5.py` | Capture a Google homepage screenshot |
| `lab6.py` | Submit a sample login form and print the response |
| `lab7.py` | Search Google and print result headings |

## 📝 Notes

- These are learning exercises rather than a full test framework.
- Website markup, access restrictions, and bot protection can change; selectors may need maintenance.
- Fixed sleeps are simple for demonstrations; explicit Selenium waits are generally more reliable.
- Use browser automation responsibly and respect each website's terms of service.

## 👨‍💻 Author

**Gowreesh G**

Interested in software development, web automation, and software testing.

---

<div align="center">

*Built with Python and Selenium — one test at a time.*

</div>
