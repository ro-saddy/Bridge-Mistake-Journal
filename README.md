# **Bridge Mistake Journal**

Bridge mistake journal is a tool for bridge players to log the mistakes they make during games and find out which ones they make the most. One adds each mistake from a small menu in Python, and the tool turns the saved data into a report page that can be opened in any browser, showing where to improve.

<img width="809" height="682" alt="Screenshot 2026-11-22 at 10 40 28 PM" src="https://github.com/user-attachments/assets/f19f42ba-ceea-476c-bfe6-466d71ad3dc3" />

<img width="1027" height="766" alt="Screenshot 2026-11-22 at 10 41 07 PM" src="https://github.com/user-attachments/assets/1d709043-9c9f-4fbe-a1eb-39775c35f9d7" />


## **Features**

- Each mistake is logged with where it was played (Club, Online or Practice), the contract, and the type of mistake.
- 4 mistake types which are Bidding, Play, Lead and Defence.
- A report shows the total number of mistakes, the biggest mistake type, and the contract with the most mistakes.
- The report also has 3 tables which break the mistakes down by type, by where played, and by contract.
- Everything is saved, so the log keeps growing across games.

## **Why I built it**

My mother is a professional bridge player, who has often wanted a platform where she could track all her mistakes, in order to analyse them. So, I built this tool so that bridge players like her can add their mistakes and view the reports of where they make them. It becomes particularly useful after many mistakes have been logged, when a pattern begins to form and one can work on their weaknesses.

## **How it works**

- bridge.py is the menu-based program. It lets the user add a mistake, make a report, or quit.
- Every mistake is added as a new row in a CSV file called bridge.csv, which is created automatically when the first mistake is saved.
- To make a report, the program reads all rows and counts how many times each mistake type, place and contract appears, using dictionaries.
- A loop then finds the most common value in each count.
- The results are written into bridge.html, which is the report that is viewed in the browser.

## **How to Run it**

1. Install Python 3. The CSV module is built-in.
2. Keep bridge.p` in its own folder.
3. Run:
     python bridge.py
5. Choose 1 to log a mistake, and 2 to make the report. Choose 3 to quit.
6. Open bridge.html in a browser. 

## **Possible improvements**

- A date for each mistake, to show whether the player is improving over time.
- Charts instead of tables to make the report easier to read.
- A note for each mistake to remember what exactly went wrong.
- A mobile version which makes it more accessible.

## **Built using**

Python, HTML, CSV
