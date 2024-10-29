# **Code Breaker**

## **Application Overview**

Code Breaker is a terminal-based game where the user is givven a secret code of 4 numbers that are randomly generated from 0-9, and concealed from the player. The player is then given 12 attempts to guess the secret code. If the player succeeds and guesses the code in the 12 attempts they win, if they do not, they lose. Duplicate numbers are allowed, which makes it more difficult for the player.

When creating this game, I really wanted to focus on everything working properly but also with a theme that is in relation to the time of it being made, halloween. I have put text with blood-like font at the end of the game that tells you if you have won or lost, i have also added a pumpkin to the home page, all of this was created by the use of [ASCII.](https://www.asciiart.eu/)

## **Table of Contents:**

1. [**Application Overview**](#application-overview)
1. [**Planning Stages**](#planning-stages)
   - [**Target Audience**](#target-audience)
   - [**User Stories**](#user-stories)
   - [**Application Aims**](#application-aims)
   - [**UX Flow Chart**](#ux-flow-chart)
   - [**Technology Used**](#technology-used)
     - [**_Libraries_**](#libraries)
1. [**Current Features**](#current-features)
   - [**Main Menu**](#main-menu)
     - [**_Main Logo Graphic_**](#main-logo-graphic)
     - [**_Instructions_**](#instructions)
     - [**_Exit Game_**](#exit-game)
   - [**Run Game**](#run-game)
     - [**_Generating the Secret Code_**](#generating-the-secret-code)
   - [**Player Guess Input with Error Handling**](#player-guess-input-with-error-handling)
   - [**Comparing Player Guess to Secret Code**](#comparing-player-guess-to-secret-code)
     - [**_Player Guess Output_**](#player-guess-ouput)
   - [**Game Graphics and Messages**](#game-graphics-and-messages)
     - [**_You Win!_**](#you-win-graphic-and-message)
     - [**_Game Over_**](#game-over-graphic-and-message)
   - [**Play Again Function with Error Handling**](#play-again-function-with-error-handling)
1. [**Considerations for Future Enhancements**](#considerations-for-future-enhancements)
   - [**Difficulty Levels**](#difficulty-levels)
   - [**Story-Based Levels**](#story-based-levels)
   - [**Improved UI**](#improved-ui)
   - [**Accessibility Features**](#accessibility-features)
1. [**Testing**](#testing)
1. [**Deployment**](#deployment)
   - [**Cloning/Forking to Local Environments**](#cloningforking-to-local-environments)
   - [**Final Deployment (Render)**](#final-deployment-render)
1. [**Credits**](#credits)
   - [**Honourable Mentions**](#honourable-mentions)
   - [**Code and Content References**](#code-and-content-references)

## **Planning Stages**

### **Target Audience**

This game has been created with a wide target audience in mind. Anyone who feels like they would like to test their brain and see if they are able to crack the code are able to test themselves, whether that be a 20+ year old or someone from the younger audience who would like to try and crack it with help from a parent.

### **User Stories**

As a user:

- I would like to play a fun and engaging code breaker game where i need to test myself.
- I wish to clearly see what game I am playing.
- I wish to have the choice to play the game straight from the menu and be able to see the instructions.
- When I have entered my guess, I want to see how many numbers in my guess were correct and in the right position, and how many were correct but in the wrong position, so that I can advance on to my next attempt having an understanding on what ive done so far.
- I want to be reminded of how many attempts I have remaining.
- I wish to be told whether i won the game or lost the game with enjoyable graphics.
- I want to be able to exit the game from the menu if i do not wish to play.

### **Application Aims**

This application aims to:

- Provide a fun and engaging code breaking game that tests the brain of the user.
- Make clear to the player that they are able to play the game, read the instructions and exit the game from the main menu.
- Provide the user with an easy to understand user interface that is clear, and provides easy to understand feedback.
- Run successfully on a loop for as long as the player needs, without crashing due to errors or the players input.

### **UX Flow Chart**

In order to help me visualise the basic logic of how the game will work and for the user to have a smooth experience, I created the following flow chart during the planning stages using [draw.io's flow chart maker](https://app.diagrams.net/):

![UX planning flow chart](docs/images/game-flow-chart.png)

### **Technology Used**

This project has been written entirely in Python.

#### **Libraries**

Two libraries were imported for this code:

**random**:

- random.choice() was utilised in the generate_code() function for the game, and is necessary in order to create a randomly generated code of 4 numbers from 0-9.

## **Current Features**

### **Main Menu with Error Handling**

![Screenshot of the Main Menu](docs/images/main-menu.png)

The main menu screen is the first thing the player sees when they start the program. It displays the main logo graphic, and below it provides the user with three options:

![Screenshot of main menu options](docs/images/main-menu.png)

In order to progress away from the main menu, the player is required to press one of these three options to take them to their required destination in the program.

As Python automatically converts input into strings, the user input is first converted to an integer using the built-in 'int()' function. The int(input()) function sits within a try statement that assumes there will be no error in the code and directs the player to the appropriate part of the program if they enter 1, 2 or 3. A ValueError is then raised in an except statement for any input that is not a 1, 2 or 3. Shown below is an example of what the program provdes if you enter an invalid number, a letter, a special character and the text version of a number:

![Screenshot of ValueError for invalid number and letter](docs/images/invalid-main-menu.png)


#### **Main Logo Graphic**

![Screenshot of the main logo graphic in VSCode](docs/images/main-menu-graphic.png)

The main logo for this game was decided due to the time of when it was being made, Halloween. I got the pumpkin ASCII art from this website. [ASCII Art](https://www.asciiart.eu/holiday-and-events/halloween). I also used the Text to Ascii Art for all the bloody text that is used. [Text to ASCII Art](https://www.asciiart.eu/text-to-ascii-art)

#### **Instructions**

If the player would like to know the instructions to the game they can simply enter '2' when they are on the main menu screen. Once the player has entered '2' they are given a set of instructions just like this:

![Screenshot of the instructions page](docs/images/instructions.png)

Below the instructions, the player is offered 2 choices. One being 'Y' if he would like to play the game and 'N' if he would like to return to the main menu. If the user enters 'Y' then the start_game() function runs.