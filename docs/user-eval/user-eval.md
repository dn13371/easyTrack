---
title: User Evaluation
nav_order: 4
---

# User evaluation

<details open markdown="block">
<summary>Table of Contents</summary>

- [01: Registration and Login](#01-registration-and-login)
- [02: Creating a project and inviting collaborators](#02-creating-a-project-and-inviting-collaborators)

</details>

## 01: Registration and Login

### Meta

**Status**: Work in progress - **Done** - Obsolete

**Updated**: 30-09-2024

### Goal

During this part of the evaluation, we wanted to see if the registration and login process would be logical for the average user.

### Method

I instructed the test subject (my girlfriend) to create an account and log in with her chosen credentials, while I tracked the time.

### Results

During my observations, the whole process of registration could be completed in about 30 seconds. Due to the short time required, I suspect a low drop-out rate for this process.

### Implications

During the first test run, I realized that the registration page only reloaded after completing the registration, showing the user a popup. To streamline this, I decided to redirect users straight to the login page after successful registration.

---

## 02: Creating a project and inviting collaborators

### Meta

**Status**: Work in progress - **Done** - Obsolete

**Updated**: 30-09-2024

### Goal

The goal of this scenario was to check if the process of creating a project and inviting a collaborator would be intuitive for the average user.

### Method

I instructed the test subject to create a project and invite me as a collaborator. After creating the project, she was also tasked with removing me from the list of collaborators.

### Results

During my observations, it became clear that the original method of adding users by their usernames was inefficient, as I had multiple accounts with the same username. Because of this, I changed the process so that collaborators had to be added using their unique userID.

However, this revealed another bug: if a non-existing userID was entered, the JavaScript part of the web app would crash.

### Implications

To streamline this process, I ensured that users are added by their userID. I also added checks to confirm whether a userID exists before adding them to the list of collaborators.
