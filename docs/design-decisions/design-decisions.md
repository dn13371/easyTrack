---
title: Design Decisions
nav_order: 3
---


# Design decisions


## 01: Database


### Problem statement

How do we store Data of the WebApp?

### Decision

We decided to use SQL-Alchemy, since the ORM-Mapper allows us to interact directly with Objects instead of writing cumbersome SQL Queries. This also saves us the hassle of creating Objects for every table
(for example we would need a User class to user Flask-Login)

### Regarded options

- Dedicated SQL-Server
- SQLite
- Firebase

---

## 02: Login Manaement


### Problem statement

How do we make sure, that certain routes are only accessible to users, that are logged in?

### Decision

We decided to user Flask-Login to handle this task, since Flask-Login in very well documented and also allows us to work with hashed passwords out of the box. Also, Flask-Login keeps track of the logged-in-user at all times, so we are able to call for the user-id using `current_user.id`.

### Regarded options

- Session Cookies

---
## 03: Visualization of our Data


### Problem statement

How can we make sure that the user is able to quickly visualize all the data? 

### Decision

We decided to use Chart.js for this purpose, since it is way more visually appealing than the other options. Also, using Chart.js alllows us to use Jinja to populate the JS code. Also, Chart.js offers a visually better experience for the end user. 

### Regarded options

- Matplotlib

---

## 04: Sending requests to the Server without updating the whole Page


### Problem statement

How do we send requests to the Server without updating the whole Page(starting/stopping the timer) ? 

### Decision

We decided to use Fetch-API and created routes for that specific purpose. The Request and Repsponse Objects also allow us to move additional data within that request. 
This #1 fact that led to this decision is that Fetch-API is native and lightweight (no external dependencies) nature of Fetch-API.

### Regarded options

- Ajax
- WebSockets
- Reloading the page when a certain button is clicked

--- 

## 05: Styling of the WebApp


### Problem statement

How do we style the WebApp? 

### Decision

We decided to opt for stlying using Bootstrap-CSS, since Bootstrap offers us UI-Elements, that are already styled from the get go. Simply assigning HTML-elements to classes does the whole job. Even simple animations are being made possible since Bootstrap offers the CSS code for that purpose. 

### Regarded options

- Hand-Written CSS / JS

