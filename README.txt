================================================================================
                           HOROSCOPE FINDER
              AIXcelerate Python Level 2 Project Documentation
================================================================================

AUTHOR           : GOKULA KRISHNA S
REGISTER NUMBER  : 7376251CS187
PROJECT TITLE    : HOROSCOPE FINDER
COURSE           : AIXcelerate Python Level 2
APPLICATION FILE : main.py
DATA STORAGE     : lookups.txt

================================================================================
TABLE OF CONTENTS
================================================================================
1.  PROJECT OVERVIEW
2.  OBJECTIVES & LEARNING OUTCOMES
3.  FEATURES & CAPABILITIES
4.  TECHNOLOGIES USED
5.  PROJECT STRUCTURE & DIRECTORY LAYOUT
6.  SYSTEM REQUIREMENTS
7.  HOW TO RUN THE PROGRAM
8.  STEP-BY-STEP USER GUIDE & MENU OPTIONS
9.  ZODIAC SIGNS REFERENCE TABLE
10. DATA STORAGE SPECIFICATION (lookups.txt)
11. INPUT VALIDATION & ERROR HANDLING MATRIX
12. SAMPLE DATA
13. PROJECT LIMITATIONS & DESIGN DECISIONS
14. AUTHOR & SUBMISSION DETAILS

================================================================================
1. PROJECT OVERVIEW
================================================================================
Horoscope Finder is an interactive, console-based personal astrology and profile
management system written in core Python. The application allows users to:

  * Enter an individual's name and date of birth in DD-MM-YYYY format.
  * Determine their accurate Western zodiac sign based on calendar boundaries.
  * Retrieve their classical astrological element (Fire, Earth, Air, Water).
  * Display curated key personality traits and an astrological lucky number.
  * Compute their exact chronological age in completed years.
  * Calculate the precise number of days remaining until their next birthday.
  * Automatically persist calculated profiles to a flat-file database (lookups.txt).
  * View, search, and aggregate records across saved profiles via a CLI menu.

The entire application is engineered purely in standard Python without relying on
any third-party packages or the built-in 'datetime' module. All calendar arithmetic,
leap-year logic, and date validation are implemented completely from scratch.

================================================================================
2. OBJECTIVES & LEARNING OUTCOMES
================================================================================
This project was developed for the AIXcelerate Python Level 2 curriculum to
demonstrate mastery over essential software design patterns in Python:

  * Procedural Programming: Structured flow with functions, loops, and branching.
  * Custom Calendar Arithmetic: Algorithmic leap-year detection, month day counts,
    and cumulative day-of-year calculations without external imports.
  * Data Structures:
      - Dictionaries: Storing nested sign metadata (ZODIAC_INFO).
      - Lists: Dynamic in-memory record storage and elemental sign groups.
      - Tuples: Comparing calendar dates cleanly (year, month, day).
  * File I/O & Persistence: Pipe-delimited file reading, real-time appending,
    and fault-tolerant parsing of lookups.txt.
  * Defensive Programming: Rigorous verification of dates, future birthdays,
    delimiter injection, blank inputs, and menu navigation choices.
  * String Operations: Formatting, whitespace trimming, case-insensitive matches,
    and structured terminal text presentation.

================================================================================
3. FEATURES & CAPABILITIES
================================================================================
1. Pure Python Date & Calendar Validation:
   - Validates strict DD-MM-YYYY format (lengths 2, 2, and 4 digits).
   - Validates real calendar dates using Gregorian leap-year rules:
       (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
   - Checks month lengths dynamically (28/29 for Feb, 30 for Apr/Jun/Sep/Nov,
     31 for Jan/Mar/May/Jul/Aug/Oct/Dec).
   - Automatically prevents nonexistent dates (e.g., 31-04-2024, 29-02-2023).

2. Zodiac Sign Determination:
   - Covers all 12 Western zodiac signs with standard astronomical boundaries.

3. Complete Astrological Profiles:
   - Element mapping (FIRE, EARTH, AIR, WATER).
   - Core personality traits and lucky numbers.

4. Chronological Age & Birthday Countdown:
   - Accurately adjusts age if birthday has not yet occurred in the reference year.
   - Computes exact days remaining until the upcoming birthday across month lengths.

5. Automatic Flat-File Storage:
   - Seamlessly appends new profiles to lookups.txt in pipe-delimited format:
     Name|DOB|ZodiacSign|Age
   - Immediately updates active in-memory lists without requiring restarts.

6. Profile Search & Aggregation:
   - View all saved profiles in neatly formatted blocks.
   - Search by name with case-insensitive matching.
   - Count saved people by specific zodiac sign.
   - Count saved people by astrological element.

================================================================================
4. TECHNOLOGIES USED
================================================================================
  * Programming Language : Python 3 (Python 3.6+ supported; tested on Python 3.14.7)
  * External Libraries   : None (100% standard built-in Python constructs)
  * Data Storage         : Plain-text flat file (lookups.txt)
  * Environment          : Cross-platform command-line / terminal interface
                           (PowerShell, Command Prompt, macOS Terminal, Bash)

================================================================================
5. PROJECT STRUCTURE & DIRECTORY LAYOUT
================================================================================
P02_HOROSCOPE_FINDER/
|
|-- main.py            Application entry point containing all program logic,
|                      data structures, calculation routines, and CLI menu.
|
|-- lookups.txt        Persistent flat-file database storing lookup profiles
|                      using a 4-field pipe-separated schema.
|
|-- README.txt         Plain-text project documentation, instructions, and guide.
|
|-- README.md          Rich Markdown project documentation and manual.
|
`-- SAMPLE_RUN.txt     Full interactive terminal transcript showcasing program
                       execution, menu operations, and edge-case handling.

================================================================================
6. SYSTEM REQUIREMENTS
================================================================================
  * Python: Version 3.6 or higher installed on your system.
  * Dependencies: None. No 'pip install' or virtual environment required.
  * Operating System: Windows 10/11, macOS, or Linux.
  * Terminal: Any standard console or terminal emulator.

================================================================================
7. HOW TO RUN THE PROGRAM
================================================================================
1. Open your terminal or command prompt (PowerShell, CMD, or Terminal).
2. Change directory into the project folder:
     cd c:\Users\gokul\Documents\P02_HOROSCOPE_FINDER
3. Execute the script using Python:
     python main.py

================================================================================
8. STEP-BY-STEP USER GUIDE & MENU OPTIONS
================================================================================

--- STEP 1: INITIAL REFERENCE DATE ---
Upon running the program, you are prompted to provide today's date:
  ENTER TODAY'S DATE IN DD-MM-YYYY FORMAT: 21-10-2026

This reference date is used throughout the session to compute ages and days
until future birthdays.

--- STEP 2: MAIN MENU ---
After validating the reference date, the main menu is presented:

  ========== HOROSCOPE FINDER ==========
  1. FIND HOROSCOPE
  2. VIEW ALL SAVED RECORDS
  3. SEARCH PERSON BY NAME
  4. COUNT PEOPLE BY ZODIAC SIGN
  5. COUNT PEOPLE BY ELEMENT
  6. EXIT
  ENTER YOUR CHOICE: 

--- OPTION 1: FIND HOROSCOPE ---
  * Prompts for the individual's name (cannot be blank or contain '|').
  * Prompts for date of birth in DD-MM-YYYY format.
  * Validates date validity and verifies DOB is not in the future.
  * Computes and prints:
      - Zodiac sign, element, traits, lucky number
      - Current age
      - Days until next birthday
  * Automatically saves record to lookups.txt.

--- OPTION 2: VIEW ALL SAVED RECORDS ---
  * Displays every saved record in memory with clear labels:
      NAME, DOB, ZODIAC SIGN, and AGE.
  * If no records have been saved yet, notifies "NO SAVED RECORDS YET".

--- OPTION 3: SEARCH PERSON BY NAME ---
  * Prompts for a target name.
  * Performs a case-insensitive search across saved profiles.
  * Displays all matching profiles or "PERSON NOT FOUND".

--- OPTION 4: COUNT PEOPLE BY ZODIAC SIGN ---
  * Prompts for one of the 12 zodiac signs (e.g., ARIES, LIBRA).
  * Returns the total count of stored individuals born under that sign.

--- OPTION 5: COUNT PEOPLE BY ELEMENT ---
  * Prompts for one of the four elements (FIRE, EARTH, AIR, WATER).
  * Returns the cumulative count of people belonging to all signs in that element.

--- OPTION 6: EXIT ---
  * Displays farewell message and terminates execution gracefully.

================================================================================
9. ZODIAC SIGNS REFERENCE TABLE
================================================================================
+-------------+----------------------+---------+----------+-------------------------------------+
| ZODIAC SIGN | DATE BOUNDARIES      | ELEMENT | LUCKY NO | KEY PERSONALITY TRAITS              |
+-------------+----------------------+---------+----------+-------------------------------------+
| ARIES       | Mar 21 - Apr 19      | FIRE    |    9     | BRAVE, CONFIDENT, ENERGETIC         |
| TAURUS      | Apr 20 - May 20      | EARTH   |    6     | PATIENT, RELIABLE, PRACTICAL        |
| GEMINI      | May 21 - Jun 20      | AIR     |    5     | CURIOUS, ADAPTABLE, COMMUNICATIVE   |
| CANCER      | Jun 21 - Jul 22      | WATER   |    2     | INTUITIVE, CARING, LOYAL            |
| LEO         | Jul 23 - Aug 22      | FIRE    |    1     | CONFIDENT, GENEROUS, CREATIVE       |
| VIRGO       | Aug 23 - Sep 22      | EARTH   |    5     | PRACTICAL, ANALYTICAL, LOYAL        |
| LIBRA       | Sep 23 - Oct 22      | AIR     |    6     | FAIR, CHARMING, DIPLOMATIC          |
| SCORPIO     | Oct 23 - Nov 21      | WATER   |    9     | PASSIONATE, RESOURCEFUL, DETERMINED |
| SAGITTARIUS | Nov 22 - Dec 21      | FIRE    |    3     | ADVENTUROUS, OPTIMISTIC, HONEST     |
| CAPRICORN   | Dec 22 - Jan 19      | EARTH   |    8     | DISCIPLINED, AMBITIOUS, RESPONSIBLE |
| AQUARIUS    | Jan 20 - Feb 18      | AIR     |    4     | INDEPENDENT, ORIGINAL, PROGRESSIVE  |
| PISCES      | Feb 19 - Mar 20      | WATER   |    7     | COMPASSIONATE, IMAGINATIVE, GENTLE  |
+-------------+----------------------+---------+----------+-------------------------------------+

================================================================================
10. DATA STORAGE SPECIFICATION (lookups.txt)
================================================================================
All saved profiles are stored in lookups.txt using a single pipe-delimited line
per entry:

  Name|DateOfBirth|ZodiacSign|Age

Field Details:
  1. Name        (string)  : Full name of the individual (pipe character '|' disallowed).
  2. DateOfBirth (string)  : DOB in DD-MM-YYYY format.
  3. ZodiacSign  (string)  : Calculated zodiac sign in uppercase.
  4. Age         (integer) : Calculated chronological age in completed years.

Fault Tolerance & In-Memory Synchronization:
  * On launch, load_records() opens lookups.txt in read mode ("r").
  * If lookups.txt does not exist, FileNotFoundError is handled gracefully and an
    empty list is initialized.
  * Every line is validated to ensure exactly 4 fields (len(details) == 4); malformed
    lines are ignored to prevent runtime errors.
  * When a new lookup is completed, save_record() appends the entry to lookups.txt
    using append mode ("a") and appends the entry to the active 'records' list.

================================================================================
11. INPUT VALIDATION & ERROR HANDLING MATRIX
================================================================================
+---------------------+-----------------------------------+------------------------------------------+
| INPUT STAGE         | VALIDATION RULE                   | SYSTEM RESPONSE / ERROR MESSAGE          |
+---------------------+-----------------------------------+------------------------------------------+
| Session Today Date  | Format must match DD-MM-YYYY      | "INVALID FORMAT. PLEASE USE DD-MM-YYYY." |
| Session Today Date  | Calendar day must be genuine      | "INVALID TODAY'S DATE. PLEASE ENTER..."  |
| Person Name         | Cannot be empty / no '|' allowed  | "INVALID NAME" (returns to menu)         |
| Person DOB          | Format and calendar validity      | "INVALID DOB. PLEASE USE A REAL DATE..." |
| Person DOB          | Date cannot be in the future      | "DOB IS IN FUTURE. ENTER AGAIN."         |
| Menu Selection      | Must be '1', '2', '3', '4', '5','6'| "INVALID MENU CHOICE" (re-prompts menu)  |
| Search Name         | Cannot be blank whitespace        | "NAME CANNOT BE EMPTY" / "NOT FOUND"     |
| Zodiac Sign Input   | Must match 1 of 12 valid signs    | "INVALID ZODIAC SIGN. ENTER ONE OF..."   |
| Element Input       | Must be FIRE, EARTH, AIR, or WATER| "INVALID ELEMENT. ENTER FIRE, EARTH..."  |
| Empty Store Actions | Accessing records when list is 0  | "NO SAVED RECORDS YET"                   |
+---------------------+-----------------------------------+------------------------------------------+

================================================================================
12. SAMPLE DATA
================================================================================
The following actual records are currently present in lookups.txt:

  GOKULA KRISHNA S|22-10-2007|LIBRA|18
  SRINITHI S|09-05-2002|TAURUS|24
  NIRMALA S|15-08-1984|LEO|42
  SURESH M|26-08-1974|VIRGO|52
  KEERTI T|23-03-2009|ARIES|17
  KEERTHNA P|30-10-2007|SCORPIO|18
  HARINE T|28-12-2004|CAPRICORN|21
  SARVESHWAR S|06-06-2008|GEMINI|18
  ABINESH P|19-10-2007|LIBRA|19

================================================================================
13. PROJECT LIMITATIONS & DESIGN DECISIONS
================================================================================
  1. Entertainment & Educational Nature:
     Zodiac signs, elements, and traits reflect traditional Western astrological
     conventions and are provided for educational and entertainment purposes.

  2. Manual Reference Date:
     The program takes today's date from user input on startup rather than from
     the system clock. This was chosen specifically to satisfy the curriculum
     requirement of avoiding the 'datetime' module while allowing date testing.

  3. Calendar-Day Precision:
     Calculations operate on day/month boundaries without solar cusp or birth
     time adjustments.

  4. Record Operations:
     The database supports querying, filtering, and appending. Manual deletion
     or in-place record edits are not part of the console menu.

================================================================================
14. AUTHOR & SUBMISSION DETAILS
================================================================================
  Student Name    : GOKULA KRISHNA S
  Register Number : 7376251CS187
  Course          : AIXcelerate Python Level 2
  Project Title   : HOROSCOPE FINDER
  Submitted For   : Python Level 2 Capstone Assessment
================================================================================
