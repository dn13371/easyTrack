---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }


# Reference 

# CLI Commands

# Routes

## Register

### `register()`

**Route:** `/register`

**Methods:** `POST` `GET`

**Purpose:** 
Renders the register page, whilst containing the logic for the registation process

**Sample output:**
![register](register.PNG)

## Login

### `login()`

**Route:** `/login`

**Methods:** `POST` `GET`

**Purpose:** 
Renders the login page, whilst containing the logic for the login process

**Sample output:**
![register](login.PNG)

## Dashboard
### `dashboard()`
**Route:** `/dashboard`
**Purpose:** 
Give the user a overview of their projects and their time consumption in general. The user is also allowed to create new projects whilst on this page. 

**Sample output** 
![register](dashboard.PNG)
![register](dashboard_modal.PNG)

## Project
### `/project/(int : project_id)`
**Route:** `/project/ int: id`
**Purpose:** 
Lets the user track their timestamps within a given project. If the user is the Owner of the project, they can also manage the project. This Route also allows visualization of the time spend on a given project. 

**Sample output** 
![register](project.PNG)
![register](project_modal.PNG)

## Timer control routes
### `startTime`; `stopTime`
**Route:** `/start`; `/stop`
**Purpose:** 
These routes are built for the Fetch-API to start or stop timers. If the Timer was started or stopped successfully, the routes return a JSON containing the Success-Status

## Loading timestamps
### `loadtimestamps(project_id)`
**Route:** `/load/(int : project_id)`
**Purpose:** 
This route is built for the Fetch-API to load all timestamps belonging to a certain project. This route returns a JSON containing all the timestamps or an error code.


## Loading collaborators for a project
### `access(project_id)`
**Route:** `/access/(int : project_id)`
**Purpose:**
This route is built for the Fetch-API to load all the collaborators belonging to a certain project. This route returns a JSON containing all the collaborators or an error code. 

## Adding collaborators for a project
### `gainaccess()`
**Route:** `/gainaccess`
**Purpose:**
This route is built for the Fetch-API to add a new user to the collaborators. This route returns a status code for whether adding the collaborator was successful. 
## Deleting collaborators for a project
### `revokeaccess()`
**Route:** `/revokeaccess`
**Purpose:**
This route is built for the Fetch-API to remove collaborators. This route returns a status code for whether adding the collaborator was successful. 

##  Create a new project
### `create()`
**Route:** `/create`
**Purpose:**
This route is built for the Fetch-API to create a new project. If the creation was successful, this route returns the projectID of the newly created project.


## Delete a project
### `delete()`
**Route:** `/delete`
**Purpose:**
This route is built for the Fetch-API to delete a project. If the deletion was successful, this route returns a status code. 