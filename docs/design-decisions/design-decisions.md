---
title: Design Decisions
nav_order: 3
---


# Design decisions

{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Database

### Meta

Status
: Work in progress - **Decided** - Obsolete


### Problem statement

Die Überlegung ist in welcher Hauptsprache schreiben wir die Web-Application - DE / EN. Außerdem war im Zuge dessen die Überlegung ein dediziertes Sprachangebot zu integrieren über eine Übersetzungsmatrix aller Texte.

### Decision

Es wurde sich **gegen** eine Übersetzungsmatrix entschieden und für die standardisierte Benutzung von **DE** als Sprache. Entscheidung wurde gemeinschaftlich getroffen von **OGD** **RS**, wegen des zu hohen **Mehraufwands**.

### Regarded options

- Übersetzungsmatrix
- Flask Babel

---

## 02: Login-Prozess Speicherung

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 2023-12-13

### Problem statement

Die Überlegung ist, wie der Login-Prozess gespeichert wird um auf geschützte Routen zuzugreifen. Möglichst mit den nativen Flask-Packages.

### Decision

Entschieden haben wir uns für eine Pre-Request Routine, die die UID des Users aus der Session lädt. Ist der User nicht eingeloggt, so gibt es kein Session Objekt mit der UID.

### Regarded options

- Via build-in Session
- Via JWT Token

---

## 03: Kerndarstellung des App Dashboards

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 2023-11-02

### Problem statement

Darstellung der Kern-Application im Dashboard um die monatliche Übersicht der Ein- und Ausnahmen zu sehen.

### Decision

Wir haben uns zum Sankey-Diagramm entschieden, weil damit besser Flüsse optisch dargestellt werden können.

### Regarded options

- Sankey-Diagramm
- Pie-Charts
- Linien-Diagramm

---

## 04: Auswahl der Graphic-Library

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 2023-11-28

### Problem statement

Auswahl der Graphic-Library zur Umsetzung des Sankey-Diagramms in unseren Jinja-Templates.

### Decision

Plotly

### Regarded options

/

---

## 05: Styling der Web-Komponenten

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 2024-02-03

### Problem statement

Wie sollen die Jinja-Templates gestylet werden und wie werden die Templates strukturiert.

### Decision

Entschieden wurde für Bootstrap, weil es vorlesungsbegleitend ist und auf Vorerfahrung gesetzt werden kann. Desweiteren haben wir uns auch für Google Fonts entschieden. Auch hier kann auf Vorerfahrung zurückgegriffen werden und die Implementierung ist leicht. Auch Icons können hierüber verwendet werden.

### Regarded options

- Bootstrap | - GoogleFonts
- TailwindCSS | - FontAwesome
- Plain CSS | 

---

## 06: Datenbankzugriff

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 2023-12-01

### Problem statement

Wie soll innerhalb der Applikation auf die Datenbank zugegriffen werden.

### Decision

Wir haben uns für SQLAlchemy entschieden, um einen Abstraktionslayer dazwischen zu haben und die Möglichkeit die Datenbank auszutauschen ohne den Code ändern zu müssen.

### Regarded options

- SQLite
- SQLAlchemy
- Plain SQL

---

## 07: Struktureller Aufbau der Applikation

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 2023-11-01

### Problem statement

Aufbau der grundlegenden Applikation und das Design-Pattern.

### Decision

Wir haben uns für das Factory Design als Package entschieden, um skalierbarer zu sein für die Zukunft. Das Design erwartet zwar ein höheres Konfigurationslevel, erlaubt es da durch aber, es beliebig zu erweitern. Desweiteren erleichtert diese Art des Designs die Zusammenarbeit, da Funktionalitäten in eigene Dateien gegliedert sind (Stichwort: Git-Konflikt).

### Regarded options

- Factory Design mit Blueprints
  - Als Package
  - Als App
- App.py Design

---

## 08: Environment Konfiguration

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 2023-12-11

### Problem statement

Wie soll das Environment konfiguriert werden. Betrifft das Starten des Entwicklungsserver und der Festlegung der verwendeten Datenbank.

### Decision

Entschieden haben wir uns für das .env und .flaskenv, um unser Environment zu komfigurieren. Das bedeutet, dass in den entsprechenden Dateien, der Debug Mode, der Host und Port eingestellt werden können. Desweiteren kann da durch die Datenbank spielendleicht geändert werden und es kann festgelegt werden ob Demodaten geladen werden.

### Regarded options

- .env Datei
- Commandline Interface

---

## 09: Pattern für den Umgang mit Formularen

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 2023-11-05

### Problem statement

Wie soll das Handling mit Formularen gestaltet sein um eine sichere und einfachere Kommunikation zwischen Client und Server sicherzustellen.

### Decision

Wir haben uns für WTForms entschieden, da es die Flexibilität bietet, die Formulare zentral zu konfigurieren und Teile daraus wieder zu verwenden. Desweiteren kümmert sich das Modul um die sichere Übertragung der Daten und deren Form.

### Regarded options

- WTForms
- Händisch, HTML, JavaScript

---