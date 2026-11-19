import csv

f = "bridge.csv"
t = ["Bidding", "Play", "Lead", "Defence"]


def add():
    s = input("Where played (Club/Online/Practice): ")
    c = input("Contract (e.g. 3NT): ")
    for i in range(len(t)):
        print(i + 1, t[i])
    n = int(input("Mistake type number: "))
    fl = open(f, "a", newline="")
    w = csv.writer(fl)
    w.writerow([s, c, t[n - 1]])
    fl.close()
    print("Saved!")


def load():
    d = []
    try:
        fl = open(f, "r")
        for r in csv.reader(fl):
            d.append(r)
        fl.close()
    except FileNotFoundError:
        pass
    return d


def count(d, k):
    a = {}
    for r in d:
        a[r[k]] = a.get(r[k], 0) + 1
    return a


def top(a):
    m = ""
    for k in a:
        if m == "" or a[k] > a[m]:
            m = k
    return m


def table(title, a):
    h = "<h2>" + title + "</h2><table border='1' cellpadding='6'>"
    for k in a:
        h += "<tr><td>" + k + "</td><td>" + str(a[k]) + "</td></tr>"
    return h + "</table>"


def report():
    d = load()
    if len(d) == 0:
        print("No mistakes logged yet")
        return
    a = count(d, 2)
    b = count(d, 1)
    c = count(d, 0)
    h = "<html><head><style>"
    h += "body{font-family:Verdana,sans-serif;}"
    h += "</style></head><body><h1>Bridge Mistake Report</h1>"
    h += "<p>Total mistakes: " + str(len(d)) + "</p>"
    h += "<p>Biggest mistake type: <b>" + top(a) + "</b></p>"
    h += "<p>Most mistakes in contract: <b>" + top(b) + "</b></p>"
    h += table("By mistake type", a)
    h += table("By where played", c)
    h += table("By contract", b)
    h += "</body></html>"
    fl = open("bridge.html", "w")
    fl.write(h)
    fl.close()
    print("bridge.html created. Open it in a browser.")


while True:
    print("\n1. Add mistake  2. Make report  3. Quit")
    x = input("Choice: ")
    if x == "1":
        add()
    elif x == "2":
        report()
    elif x == "3":
        break
