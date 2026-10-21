# NAME : GOKULA KRISHNA S
# REGISTER NUMBER : 7376251CS187
# PROJECT TITLE : HOROSCOPE FINDER

records = []

ZODIAC_INFO = {
    "ARIES": {"element": "FIRE", "traits": ["BRAVE", "CONFIDENT", "ENERGETIC"], "lucky_number": 9},
    "TAURUS": {"element": "EARTH", "traits": ["PATIENT", "RELIABLE", "PRACTICAL"], "lucky_number": 6},
    "GEMINI": {"element": "AIR", "traits": ["CURIOUS", "ADAPTABLE", "COMMUNICATIVE"], "lucky_number": 5},
    "CANCER": {"element": "WATER", "traits": ["INTUITIVE", "CARING", "LOYAL"], "lucky_number": 2},
    "LEO": {"element": "FIRE", "traits": ["CONFIDENT", "GENEROUS", "CREATIVE"], "lucky_number": 1},
    "VIRGO": {"element": "EARTH", "traits": ["PRACTICAL", "ANALYTICAL", "LOYAL"], "lucky_number": 5},
    "LIBRA": {"element": "AIR", "traits": ["FAIR", "CHARMING", "DIPLOMATIC"], "lucky_number": 6},
    "SCORPIO": {"element": "WATER", "traits": ["PASSIONATE", "RESOURCEFUL", "DETERMINED"], "lucky_number": 9},
    "SAGITTARIUS": {"element": "FIRE", "traits": ["ADVENTUROUS", "OPTIMISTIC", "HONEST"], "lucky_number": 3},
    "CAPRICORN": {"element": "EARTH", "traits": ["DISCIPLINED", "AMBITIOUS", "RESPONSIBLE"], "lucky_number": 8},
    "AQUARIUS": {"element": "AIR", "traits": ["INDEPENDENT", "ORIGINAL", "PROGRESSIVE"], "lucky_number": 4},
    "PISCES": {"element": "WATER", "traits": ["COMPASSIONATE", "IMAGINATIVE", "GENTLE"], "lucky_number": 7}
}

ELEMENTS = ["FIRE", "EARTH", "AIR", "WATER"]


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    if 1 <= month <= 12:
        return 31
    return 0


def is_valid_date(date_text):
    parts = date_text.split("-")
    if len(parts) != 3:
        return False
    if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        return False
    if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        return False
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    return year > 0 and 1 <= month <= 12 and 1 <= day <= days_in_month(month, year)


def date_parts(date_text):
    parts = date_text.split("-")
    return int(parts[0]), int(parts[1]), int(parts[2])


def date_day_number(day, month, year):
    total = day
    for current_month in range(1, month):
        total += days_in_month(current_month, year)
    return total


def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "ARIES"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "TAURUS"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "GEMINI"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "CANCER"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "LEO"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "VIRGO"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "LIBRA"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "SCORPIO"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "SAGITTARIUS"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "CAPRICORN"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "AQUARIUS"
    return "PISCES"


def calculate_age(day, month, year, today_day, today_month, today_year):
    age = today_year - year
    if (today_month, today_day) < (month, day):
        age -= 1
    return age


def days_until_birthday(day, month, today_day, today_month, today_year):
    birthday_this_year = (month, day)
    today = (today_month, today_day)
    target_year = today_year if birthday_this_year > today else today_year + 1
    today_number = date_day_number(today_day, today_month, today_year)
    birthday_number = date_day_number(day, month, target_year)

    if target_year == today_year:
        return birthday_number - today_number
    return sum(days_in_month(m, today_year) for m in range(1, 13)) - today_number + birthday_number


def load_records():
    records.clear()
    try:
        with open("lookups.txt", "r") as file:
            for line in file:
                details = line.strip().split("|")
                if len(details) == 4:
                    records.append(details)
    except FileNotFoundError:
        pass


def save_record(name, dob, sign, age):
    with open("lookups.txt", "a") as file:
        file.write(f"{name}|{dob}|{sign}|{age}\n")
    records.append([name, dob, sign, str(age)])


def view_all_records():
    if not records:
        print("NO SAVED RECORDS YET")
        return
    print("\n========== SAVED RECORDS ==========")
    for record in records:
        print(f"NAME : {record[0]}")
        print(f"DOB : {record[1]}")
        print(f"ZODIAC SIGN : {record[2]}")
        print(f"AGE : {record[3]}")
        print("----------------------------------")


def search_person_by_name():
    if not records:
        print("NO SAVED RECORDS YET")
        return
    search_name = input("ENTER NAME TO SEARCH: ").strip().lower()
    if not search_name:
        print("NAME CANNOT BE EMPTY")
        return
    found = False
    for record in records:
        if record[0].lower() == search_name:
            print("\n========== PERSON FOUND ==========")
            print(f"NAME : {record[0]}")
            print(f"DOB : {record[1]}")
            print(f"ZODIAC SIGN : {record[2]}")
            print(f"AGE : {record[3]}")
            found = True
    if not found:
        print("PERSON NOT FOUND")


def find_horoscope(today_day, today_month, today_year):
    print("\n========== FIND HOROSCOPE ==========")
    name = input("ENTER YOUR NAME: ").strip()
    if not name or "|" in name :
        print("INVALID NAME")
        return

    while True:
        dob_text = input("ENTER YOUR DOB IN DD-MM-YYYY FORMAT: ").strip()
        if not is_valid_date(dob_text):
            print("INVALID DOB. PLEASE USE A REAL DATE IN DD-MM-YYYY FORMAT.")
            continue

        day, month, year = date_parts(dob_text)
        if (year, month, day) > (today_year, today_month, today_day):
            print("DOB IS IN FUTURE. ENTER AGAIN.")
            continue
        break

    sign = get_zodiac_sign(day, month)
    info = ZODIAC_INFO[sign]
    age = calculate_age(day, month, year, today_day, today_month, today_year)
    countdown = days_until_birthday(day, month, today_day, today_month, today_year)

    print("DOB IS VALID")
    print(f"ZODIAC SIGN : {sign}")
    print(f"ELEMENT : {info['element']}")
    print("TRAITS : " + ", ".join(info["traits"]))
    print(f"LUCKY NUMBER : {info['lucky_number']}")
    print(f"YOU ARE {age} YEARS OLD")
    print(f"DAYS UNTIL NEXT BIRTHDAY: {countdown}")
    save_record(name, dob_text, sign, age)
    print("RECORD SAVED SUCCESSFULLY")


def count_people_by_sign():
    if not records:
        print("NO SAVED RECORDS YET")
        return
    sign_name = input("ENTER THE ZODIAC SIGN: ").strip().upper()
    if sign_name not in ZODIAC_INFO:
        print("INVALID ZODIAC SIGN. ENTER ONE OF THE 12 ZODIAC SIGNS.")
        return
    count = 0
    for record in records:
        if record[2].upper() == sign_name:
            count += 1
    print(f"NUMBER OF PEOPLE WITH {sign_name} SIGN: {count}")


def count_people_by_element():
    if not records:
        print("NO SAVED RECORDS YET")
        return
    element_name = input("ENTER THE ELEMENT (FIRE, EARTH, AIR, WATER): ").strip().upper()
    if element_name not in ELEMENTS:
        print("INVALID ELEMENT. ENTER FIRE, EARTH, AIR, OR WATER.")
        return
    count = 0
    for record in records:
        sign_name = record[2].upper()
        if sign_name in ZODIAC_INFO and ZODIAC_INFO[sign_name]["element"] == element_name:
            count += 1
    print(f"NUMBER OF PEOPLE WITH {element_name} ELEMENT: {count}")

def is_correct_date_format(date_text):
    parts = date_text.split("-")

    if len(parts) != 3:
        return False

    if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        return False

    if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        return False

    return True

def show_menu():
    print("\n========== HOROSCOPE FINDER ==========")
    print("1. FIND HOROSCOPE")
    print("2. VIEW ALL SAVED RECORDS")
    print("3. SEARCH PERSON BY NAME")
    print("4. COUNT PEOPLE BY ZODIAC SIGN")
    print("5. COUNT PEOPLE BY ELEMENT")
    print("6. EXIT")


def main():
    load_records()
    while True:
        today_text = input("ENTER TODAY'S DATE IN DD-MM-YYYY FORMAT: ").strip()
        if not is_correct_date_format(today_text):
            print("INVALID FORMAT. PLEASE USE DD-MM-YYYY.")
        elif not is_valid_date(today_text):
            print("INVALID TODAY'S DATE. PLEASE ENTER A VALID DATE.")
        else:
            break

    today_day, today_month, today_year = date_parts(today_text)

    while True:
        show_menu()
        choice = input("ENTER YOUR CHOICE: ").strip()
        if choice == "1":
            find_horoscope(today_day, today_month, today_year)
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            search_person_by_name()
        elif choice == "4":
            count_people_by_sign()
        elif choice == "5":
            count_people_by_element()
        elif choice == "6":
            print("THANK YOU FOR USING HOROSCOPE FINDER!")
            print("GOODBYE!")
            break
        else:
            print("INVALID MENU CHOICE")

main()
