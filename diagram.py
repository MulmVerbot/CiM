import matplotlib.pyplot as plt

# Daten für das Diagramm
x = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
                2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
y = [10012, 10764, 11532, 12127, 12678, 13248, 13741, 14428, 15157, 15785,
          16364, 17284, 18468, 19372, 20523, 19749, 20145, 22541, 24473, 25586,
          26438, 27167, 28422, 30145, 31250, 31894, 25483, 29455, 33147, 35000] # Hier stehen jetzt einfach mal die Einahmen der Deutschen Bahn als Testdaten

# Erstellen eines Plots
plt.plot(x, y)

# Hinzufügen von Titeln und Beschriftungen
plt.title('Einfaches Diagramm')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')

# Anzeigen des Diagramms
plt.show()
