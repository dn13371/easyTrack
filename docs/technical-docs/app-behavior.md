---
title: App Behavior
parent: Technical Docs
nav_order: 2
---



# App Behavior
## Business Logic

1. ** Registration and Login**

Upon Registration, a User object is created. This User object is also being used inside the login process to verify the users credentials. 

2. ** Creating Project and inviting collaborators **

Upon creating a project, a Project object and a Access object are created. For each each collaborator the user decides to invite to the project, a new Access object is created. 

3. ** Visualization - dashboard**

The dashboard shows all projects the user can access and aggregates all timestamps for a given project. The aggregated timestamps are being show in a chart.

4. ** Creating a timestamp **

Upon starting a timestamp, a Timestamp object without a ending time is being created. The ending time will be added to the timestamp when the stop button gets pressed. By that logic, the timstamps will keep running even when the user logs off or closes the tab. 

5. ** Managing your Project **

If you own a project, you can make changes to it. These include adding or removing collaborators or deleting the project. 


