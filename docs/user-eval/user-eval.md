---
title: User Evaluation
nav_order: 4
---

{: .label }
[Jane Dane]

{: .no_toc }
# User evaluation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Registration and Login

### Meta

Status
: Work in progress - **Done** - Obsolete

Updated
: 30-09-2024

### Goal

During this part of the evaluation we wanted to see if the registration and login process would be logical for the average user. 

### Method

In this case, I instructed the test subject (my girlfriend) to create an account and log in with her chosen credentials, while i tracked the time. 

### Results

During my observations, the whole process of registration could be achieved in about 30 seconds. Due to the short time needed to do so, I would suspect a rather low drop-out rate. 

### Implications

During the first run of this test, i realized that the register page only reloaded upon completing the registration while giving the user a popup. To streamline this, i decided to set the redirection straight to the login page after successfully registering. 
---

## 02: Creating a project and inviting collaborators

### Meta

Status
: Work in progress - **Done** - Obsolete

Updated
: 30-09-2024

### Goal

The goal for this scenario would be checking if the process of creating a project and inviting a collaborator would be logical for the average user. 

### Method

In this case, I instructed the test subject (my girlfriend) to create an project and invite me as an collborator. 
After creating the project, she had to remove me from the list of the collaborators. 

### Results

During my observations, it got clear that the original method of adding users by their usernames was not efficient, since during my testing process, i have created multiple accounts with the same username. 
Because of this, i made sure that collaborators have to be added by using their unique userID. 
But this unearthed another bug: If you entered a non-existing userID, the whole Javascript part of the WebApp would crash.. 

### Implications

To completely streamline this process, i had to make sure that users were being added by their userId. I also had to make sure to check whether a certain userID existed prior to adding them to the list of collaborators. 
---