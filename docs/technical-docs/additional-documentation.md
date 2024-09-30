---
title: Additional Documentation
parent: Technical Docs
nav_order: 5
---

# Additional Documentation

Since I have decided to you JavaScript in some places to enhance the WebApp, I am explaining the uses in this Section. 

## Registration

In this section, JS is being used to check whether the entered passwords match.

## Dashboard

### Chart.js

A Chart.js element is being used to display the total time spent by the user. The JS-code to populate the Chart is static, while the data for the chart originate from Jinja. 

### Modal 

A Bootstrap Modal is being used to create new Projects and to invite other collaborators. For this reason, some JS from bootstrap is being used to inflate or deflate the Modal. 

In addition to that, the list of users is dynamically rendered using JavaScript, the data from which stems from buttons within the modal sending requests via Fetch-API. 

Sending and processing Fetch-API-requests are also being handled by JavaScript. 

## Timestamps

JavaScript is being used within project.html to render the timer dynamically. This means that the timer resumes to the correct time even if the user decides to log out or close the tab. 

In addition to that, the Start and Stop buttons within project.html are bound to JS-code that sends Fetch-API-requests, and the Stop button is able to refresh the list of all timestamps without reloading the whole page. 