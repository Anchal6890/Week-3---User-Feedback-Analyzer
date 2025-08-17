# Week-3---User-Feedback-Analyzer
# Feedback Analyzer Mini Project

## Project Overview
The **Feedback Analyzer** is a Python-based mini project that allows users to collect, store, and view feedback efficiently. The project provides a simple menu-driven interface to **add**, **view**, and **analyze** feedback from users.  

This project is ideal for beginners to learn Python **file handling**, **CSV storage**, and basic **data display**.

---

## Features
- **Add New Feedback:** Users can enter their name, rating, and feedback.  
- **View Feedback:** Display all saved feedback in a **numbered list** format.  
- **File-Based Storage:** Feedback is stored locally in a CSV file for persistence.  
- **Menu-Driven Interface:** Simple and user-friendly for beginners.

---

## Installation
1. Ensure **Python 3.x** is installed on your system.  
2. Clone this repository or download the source code:
```bash
git clone <repository_url>
```
3. Navigate to the project folder:
```bash
cd Feedback-Analyzer
```
4. Run the Python script:
```bash
python Feedback_Analyzer.py
```

---

## Usage
1. Launch the program.  
2. You will see the following menu:
```
--- Feedback Analyzer Menu ---
1. Add New Feedback
2. View Feedback
3. Exit
```
3. Choose the desired option by entering the corresponding number.  
4. Follow the prompts to add or view feedback.  

---

## Example Feedback Display
When you choose **View Feedback**, the output will show all entries in a numbered list:

```
All Feedback:
1. I love this product, it's excellent!
2. The service was slow and terrible.
3. It's okay, nothing special.
```

---

## Sample CSV File
The project uses a CSV file named `feedback_data.csv` to store feedback.  
Example structure:

| Name   | Rating | Feedback                             |
|--------|--------|--------------------------------------|
| User1  | 5      | I love this product, it's excellent! |
| User2  | 1      | The service was slow and terrible.   |
| User3  | 3      | It's okay, nothing special.          |

---

## File Structure
```
Feedback-Analyzer/
│
├── Feedback_Analyzer.py      # Main Python script
├── feedback_data.csv         # Stores all user feedback
└── README.md                 # Project description
```

---

## Dependencies
- Python standard libraries: `csv`, `os`  
- No external libraries required.

---

## Future Enhancements
- Add a **GUI** interface using Tkinter or PyQt.  
- Implement **advanced sentiment analysis** for feedback comments.  
- Add options to **delete or update** feedback entries.  
- Generate **visual reports** like charts for better analysis.

---

## Author
**Anchal Singh**  
