---
title: App Behavior
parent: Technical Docs
nav_order: 2
---



# App Behavior
## Business Logic

1. **Registration and Login**

   Upon Registration, a `User` object is created. This `User` object is also being used inside the login process to verify the user's credentials. 

2. **Creating Project and Inviting Collaborators**

   Upon creating a project, a `Project` object and an `Access` object are created. For each collaborator the user decides to invite to the project, a new `Access` object is created. 

3. **Visualization - Dashboard**

   The dashboard shows all projects the user can access and aggregates all timestamps for a given project. The aggregated timestamps are shown in a chart.

4. **Creating a Timestamp**

   Upon starting a timestamp, a `Timestamp` object without an ending time is created. The ending time will be added to the timestamp when the stop button is pressed. By that logic, the timestamps will keep running even when the user logs off or closes the tab. 

5. **Managing Your Project**

   If you own a project, you can make changes to it. These include adding or removing collaborators, or deleting the project.


