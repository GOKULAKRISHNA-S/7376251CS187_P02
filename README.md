# Horoscope Finder

**AIXcelerate Python Level 2 Project**  
**Author :** GOKULA KRISHNA S  
**Register Number :** 7376251CS187  
**Project Title :** HOROSCOPE FINDER  

---

## 1. Project Overview

**Horoscope Finder** is an interactive, terminal-based personal astrology and profile management application built in Python. The program calculates an individual's Western zodiac sign based on their birth date, retrieves their astrological element, core personality traits, and lucky number, and calculates their current chronological age alongside an exact countdown in days until their next birthday.

All calculated profiles are automatically persisted to a local flat-file database (`lookups.txt`). Through a user-friendly console menu, users can perform new lookups, inspect all saved profiles, search for individuals by name, and compute statistical aggregates grouped by zodiac signs and astrological elements.

The entire application is developed using standard core Python without importing third-party libraries or external calendar modules, demonstrating custom date arithmetic and defensive input validation.

---

## 2. Objectives

This project was developed as part of the **AIXcelerate Python Level 2** curriculum to demonstrate fundamental software engineering principles and core Python concepts:

- **Procedural Programming & Control Flow:** Implementing interactive loops (`while True`), conditional branching (`if-elif-else`), and structured function decomposition.
- **Custom Calendar Arithmetic:** Writing date validation, leap-year calculations, and day-of-year conversions from scratch without external libraries or the `datetime` module.
- **Data Structures:** Utilizing dictionaries for nested lookup mappings (`ZODIAC_INFO`), lists for multi-record storage (`records`), and tuples for date comparisons.
- **File Persistence & I/O:** Reading from and appending to plain-text files (`lookups.txt`) with custom pipe-delimited formatting, including graceful handling of missing files.
- **Defensive Input Validation:** Enforcing strict format constraints, calendar boundary checks, future date detection, delimiter sanitization, and menu choice verification.
- **Case-Insensitive String Operations:** Implementing robust searching and grouping using string formatting methods (`strip()`, `lower()`, `upper()`, `split()`).

---

## 3. Features

### Core Capabilities

1. **Input and Date Validation Using Core Python:**
   - Validates user input dates using custom string inspection functions (`is_correct_date_format` and `is_valid_date`).
   - Ensures strict compliance with the `DD-MM-YYYY` pattern, checking component lengths, hyphens, and numeric digits.

2. **Leap-Year and Calendar-Date Validation:**
   - Implements the Gregorian leap-year algorithm (`year % 4 == 0 and year % 100 != 0 or year % 400 == 0`).
   - Dynamically checks February days (29 in leap years, 28 in common years).
   - Validates 30-day months (April, June, September, November) and 31-day months (January, March, May, July, August, October, December).
   - Rejects non-existent calendar dates such as `31-02-2024` or `31-04-2023`.

3. **All 12 Zodiac Signs and Accurate Date Boundaries:**
   - Accurately maps any valid calendar birth date to one of the 12 Western zodiac signs via `get_zodiac_sign(day, month)`.

   | Zodiac Sign | Date Range | Element | Lucky Number | Key Personality Traits |
   | :--- | :--- | :--- | :---: | :--- |
   | **ARIES** | March 21 – April 19 | FIRE | 9 | BRAVE, CONFIDENT, ENERGETIC |
   | **TAURUS** | April 20 – May 20 | EARTH | 6 | PATIENT, RELIABLE, PRACTICAL |
   | **GEMINI** | May 21 – June 20 | AIR | 5 | CURIOUS, ADAPTABLE, COMMUNICATIVE |
   | **CANCER** | June 21 – July 22 | WATER | 2 | INTUITIVE, CARING, LOYAL |
   | **LEO** | July 23 – August 22 | FIRE | 1 | CONFIDENT, GENEROUS, CREATIVE |
   | **VIRGO** | August 23 – September 22 | EARTH | 5 | PRACTICAL, ANALYTICAL, LOYAL |
   | **LIBRA** | September 23 – October 22 | AIR | 6 | FAIR, CHARMING, DIPLOMATIC |
   | **SCORPIO** | October 23 – November 21 | WATER | 9 | PASSIONATE, RESOURCEFUL, DETERMINED |
   | **SAGITTARIUS** | November 22 – December 21 | FIRE | 3 | ADVENTUROUS, OPTIMISTIC, HONEST |
   | **CAPRICORN** | December 22 – January 19 | EARTH | 8 | DISCIPLINED, AMBITIOUS, RESPONSIBLE |
   | **AQUARIUS** | January 20 – February 18 | AIR | 4 | INDEPENDENT, ORIGINAL, PROGRESSIVE |
   | **PISCES** | February 19 – March 20 | WATER | 7 | COMPASSIONATE, IMAGINATIVE, GENTLE |

4. **Zodiac Elements, Personality Traits, and Lucky Numbers:**
   - Stored in a structured dictionary (`ZODIAC_INFO`) mapping each sign to its classical astrological element (`FIRE`, `EARTH`, `AIR`, `WATER`), a curated list of personality traits, and a lucky number.

5. **Age Calculation and Birthday Countdown:**
   - **Chronological Age:** Accurately computed by comparing birth year, month, and day against the reference date. If the birthday has not yet occurred in the reference year, age is decremented by 1.
   - **Days Until Next Birthday:** Determines whether the birthday is still ahead in the current year or falls in the subsequent year, then computes the exact remaining day count by summing month lengths.

6. **Saving Lookup Results to `lookups.txt`:**
   - Successfully completed lookups are appended in real time to `lookups.txt` using the standard pipe-delimited format: `Name|DOB|ZodiacSign|Age`.
   - In-memory record lists are immediately updated so that subsequent operations reflect the new record without restarting.

7. **Viewing Saved Records:**
   - Formats and displays all stored records with labeled attributes (`NAME`, `DOB`, `ZODIAC SIGN`, `AGE`) and distinct divider lines.

8. **Searching Records by Name:**
   - Allows users to search for any individual by name. The search is case-insensitive (e.g., searching `gokula krishna s` matches `GOKULA KRISHNA S`).

9. **Counting People by Zodiac Sign and Element:**
   - **Count by Sign:** Prompts for any of the 12 zodiac signs and outputs the number of matching records.
   - **Count by Element:** Prompts for one of the four elements (`FIRE`, `EARTH`, `AIR`, `WATER`) and calculates the sum of all matching individuals across corresponding signs.

10. **Menu Validation and Error Handling:**
    - Continuous loop keeps the program active until explicitly exited by the user.
    - Guards against future birth dates, blank names, delimiter injection, invalid date formats, unknown menu options, and invalid element/sign names.

---

## 4. Technologies Used

- **Python 3:** The entire application logic is written in core Python (compatible with Python 3.6+; tested on Python 3.14.7).
- **Standard Library Only:** No external packages, third-party libraries, or `pip` dependencies are used. Even date operations avoid external imports, relying purely on algorithmic Python code.
- **Plain-Text File Storage:** File persistence is handled via standard Python file I/O (`open()`, `read()`, `write()`) storing records in `lookups.txt`.
- **Operating System Terminal:** Runs across all major terminal and console environments (Windows PowerShell, Command Prompt, macOS Terminal, Linux Bash).

---

## 5. Project Structure

The project directory consists strictly of the following files:

```
P02_HOROSCOPE_FINDER/
├── main.py          # Main application script containing all program logic and CLI interface
├── lookups.txt       # Plain-text file storing saved lookup records
├── README.txt        # Plain-text project documentation and user manual
├── README.md         # Comprehensive Markdown documentation and user guide
└── SAMPLE_RUN.txt    # Transcript showing an illustrative terminal execution session
```

- **`main.py`**: The sole executable script containing data tables (`ZODIAC_INFO`, `ELEMENTS`), custom date validation functions, mathematical calculation routines, file I/O handlers, and the interactive terminal menu loop.
- **`lookups.txt`**: A persistent plain-text storage file where each line represents one saved profile in four-field pipe-separated format.
- **`README.txt`**: Plain-text project documentation, specification, requirements, and usage manual.
- **`README.md`**: Comprehensive Markdown project documentation, specification, requirements, and user guide.
- **`SAMPLE_RUN.txt`**: A sample run transcript illustrating user interactions, input validation, menu options, and formatted terminal outputs.

---

## 6. Requirements

- **Python Version:** Python 3 (Python 3.6 or higher recommended due to f-string formatting; verified and tested on Python 3.14.7).
- **External Dependencies:** None. No installations via `pip` are needed.
- **Operating System:** Platform independent (Windows, macOS, Linux).

---

## 7. How to Run

1. Open your terminal or command prompt (e.g., Windows PowerShell, Command Prompt, or Bash).
2. Navigate to the project directory:
   ```bash
   cd c:\Users\gokul\Documents\P02_HOROSCOPE_FINDER
   ```
3. Run the application with the Python interpreter:
   ```bash
   python main.py
   ```

---

## 8. How to Use

### Step 1: Session Reference Date
When launched, the program asks for today's date:
```text
ENTER TODAY'S DATE IN DD-MM-YYYY FORMAT: 
```
Enter a valid calendar date (e.g., `21-10-2026`). This date serves as the reference point for calculating age and the remaining days until an individual's next birthday.

### Step 2: Main Menu Navigation
Once the date is validated, the main menu displays:
```text
========== HOROSCOPE FINDER ==========
1. FIND HOROSCOPE
2. VIEW ALL SAVED RECORDS
3. SEARCH PERSON BY NAME
4. COUNT PEOPLE BY ZODIAC SIGN
5. COUNT PEOPLE BY ELEMENT
6. EXIT
ENTER YOUR CHOICE: 
```

### Menu Options Explained

- **Option 1: FIND HOROSCOPE**
  - Prompts for the person's name and birth date in `DD-MM-YYYY` format.
  - Validates the date, verifies it does not lie in the future, and displays:
    - Zodiac sign
    - Element
    - Personality traits
    - Lucky number
    - Calculated age
    - Days remaining until the next birthday
  - Automatically appends the result to `lookups.txt` and updates active memory.

- **Option 2: VIEW ALL SAVED RECORDS**
  - Reads all valid records stored in memory and displays each person's Name, DOB, Zodiac Sign, and Age formatted inside clean divider blocks.
  - If no records exist, prints `NO SAVED RECORDS YET`.

- **Option 3: SEARCH PERSON BY NAME**
  - Prompts for a name and performs a case-insensitive search across saved records.
  - Displays matching records under `========== PERSON FOUND ==========`.
  - If no record matches, displays `PERSON NOT FOUND`.

- **Option 4: COUNT PEOPLE BY ZODIAC SIGN**
  - Prompts for one of the 12 zodiac signs (case-insensitive).
  - Displays the total number of individuals in storage with that sign.

- **Option 5: COUNT PEOPLE BY ELEMENT**
  - Prompts for one of the four elements: `FIRE`, `EARTH`, `AIR`, or `WATER` (case-insensitive).
  - Displays the total count of individuals whose zodiac signs belong to that element.

- **Option 6: EXIT**
  - Displays closing appreciation messages (`THANK YOU FOR USING HOROSCOPE FINDER!`, `GOODBYE!`) and exits the program loop.

---

## 9. Data Storage Format

Saved horoscope records are stored in `lookups.txt` using a four-field, pipe-delimited format:

```text
Name|DateOfBirth|ZodiacSign|Age
```

### Field Definitions

1. **`Name`** (`string`): The individual's full name as entered by the user. Pipe characters (`|`) are prohibited to maintain file schema integrity.
2. **`DateOfBirth`** (`string`): The person's date of birth in two-digit day, two-digit month, and four-digit year format (`DD-MM-YYYY`).
3. **`ZodiacSign`** (`string`): The calculated Western zodiac sign in uppercase (e.g., `LIBRA`, `TAURUS`).
4. **`Age`** (`integer` / `string`): The person's calculated age in completed years as of the lookup session.

### Loading and Persistence Behavior

- At program startup, `load_records()` opens `lookups.txt` in read mode (`"r"`).
- Each line is stripped and split by the pipe delimiter (`|`).
- **Resilience check:** Only lines with exactly four fields (`len(details) == 4`) are parsed into memory. Lines with incorrect field counts are safely bypassed without raising exceptions.
- If `lookups.txt` does not exist on initial run, `FileNotFoundError` is caught silently and an empty list is initialized.
- When `save_record()` is called, the new profile is appended to `lookups.txt` using append mode (`"a"`), followed by a newline (`\n`), ensuring persistent retention across sessions.

---

## 10. Validation and Error Handling

The application enforces validation at every user input stage:

| Input Stage | Validation Rule | Behavior / Error Message |
| :--- | :--- | :--- |
| **Startup Date Format** | Must contain 3 hyphen-separated parts (`DD-MM-YYYY`) of lengths 2, 2, and 4 digits. | Displays `INVALID FORMAT. PLEASE USE DD-MM-YYYY.` and prompts again. |
| **Startup Date Validity** | Must represent a real calendar day (checks leap years and days per month). | Displays `INVALID TODAY'S DATE. PLEASE ENTER A VALID DATE.` and prompts again. |
| **Person Name** | Cannot be empty or contain pipe delimiter (`\|`). | Displays `INVALID NAME` and immediately returns to the main menu. |
| **Date of Birth Format/Day** | Must match `DD-MM-YYYY` and valid month day limits. | Displays `INVALID DOB. PLEASE USE A REAL DATE IN DD-MM-YYYY FORMAT.` and prompts again. |
| **Future Birthday** | DOB cannot exceed the startup reference date (`(year, month, day) > (today_year, today_month, today_day)`). | Displays `DOB IS IN FUTURE. ENTER AGAIN.` and prompts again. |
| **Menu Selection** | Input must strictly be `"1"`, `"2"`, `"3"`, `"4"`, `"5"`, or `"6"`. | Displays `INVALID MENU CHOICE` and re-displays the main menu. |
| **Search Name** | Input cannot be blank or whitespace-only. | Displays `NAME CANNOT BE EMPTY`. If no matches exist, displays `PERSON NOT FOUND`. |
| **Zodiac Sign Input** | Sign must exist in `ZODIAC_INFO` dictionary. | Displays `INVALID ZODIAC SIGN. ENTER ONE OF THE 12 ZODIAC SIGNS.` |
| **Element Input** | Element must be one of `FIRE`, `EARTH`, `AIR`, or `WATER`. | Displays `INVALID ELEMENT. ENTER FIRE, EARTH, AIR, OR WATER.` |
| **Empty File Records** | Viewing, searching, or counting with zero records loaded. | Displays `NO SAVED RECORDS YET`. |

---

## 11. Sample Data

The application stores records in `lookups.txt`. Here are two actual sample records directly from the project's data file:

```
GOKULA KRISHNA S|22-10-2007|LIBRA|18
SRINITHI S|09-05-2002|TAURUS|24
```

These records illustrate the pipe-delimited schema and represent valid entries previously calculated by the program.

---

## 12. Limitations

- **Entertainment Purpose:** Astrological signs, personality traits, and lucky numbers are traditional cultural concepts provided strictly for educational and entertainment purposes. They are not scientific assessments or predictive tools.
- **Reference Date Input:** Today's date is manually provided at the start of each session rather than fetched from the operating system clock. This is a deliberate educational choice to avoid importing `datetime`, while enabling simulations across past or future reference dates.
- **Date Granularity:** Calculations operate on calendar dates only; exact birth times, time zones, and solar cusp calculations are not modeled.
- **Record Modification:** The program currently supports appending and querying records, but does not include in-menu editing or deletion of records once saved.

---

## 13. Author Details

- **Name:** GOKULA KRISHNA S  
- **Register Number:** 7376251CS187  
- **Project Title:** HOROSCOPE FINDER  
- **Course:** AIXcelerate Python Level 2  