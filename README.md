# Lab 8: Polymorphism, Part 1

## Context

Throughout this lab and next week’s lab (lab 9), you’ll be working on a
slightly larger project, similar to how assignments 7 and 8 represent a
two-part project. You’ll complete roughly half the work in this lab and
the remaining half in the next lab. See the [Requirements](#requirements) section for a list
of the exact requirements for this lab.

> [!NOTE] 
> Because lab 9 will build off of this lab, it’s very important that you finish this lab in its entirety, and that you do not lose the code that you write for this lab. If you don’t finish the work during this lab session, please complete it at home or in office hours (you won’t be able to make up the lost points, but you’ll need the work to be completed so that you have a good starting point for next week’s lab).

> [!TIP]
> This is a challenging lab. You’ll have to think fast and work  efficiently. Use your assignment 7 code as a starting point to save time.

### High-level idea

Throughout this lab and the next, you’ll be applying polymorphism and
other techniques to implement a simple game played on a 2D grid. The
player controls a deer navigating a forest. The goal is to eat both
blueberry bushes, drink water from the pond, and make your way back to
the herd without being eaten by the hungry bears.

### The forest

The forest is a grid of `ForestPatch` objects. It must be represented as
a 2D list (a variable of type `list[list[ForestPatch]]`).

**The forest should have 5 rows and 5 columns**. This is in contrast to
Hunt the Wumpus where the player gets to decide the size of the game
board.

`ForestPatch` is a class. The `ForestPatch` class should have a private `_event`
attribute of type `Event | None`. This attribute will be
`None` for empty forest patches. For non-empty forest patches, it will
store an object whose type is a subclass of `Event` (i.e., it’s
polymorphic; more on this shortly).

### Events

There are several kinds of events that are sprawled throughout the
forest (the 2D grid). These events are generated and placed throughout
the forest when the game begins:

- The pond. <ins>One</ins> pond should be generated at the beginning of the
  game. **It should not be placed randomly**. Rather, it should be
  placed in the top-right forest patch in the grid.

- The blueberry bushes. <ins>Two</ins> blueberry bushes should be generated
  at the beginning of the game. **They should not be placed randomly**.
  Rather, they should be placed in the top-left and bottom-right forest
  patches in the grid.

- The deer herd. <ins>One</ins> deer herd should be generated at the
  beginning of the game. **It should not be placed randomly**. Rather,
  it should be placed in the bottom-left forest patch in the grid. The
  player will also start out in this forest patch.

- Bear dens. <ins>Three</ins> bear dens should be generated and placed in
  different random empty forest patches at the start of the game.

Each forest patch should have <ins>at most</ins> one event (bear dens should
not be placed in the corners of the grid where the other events are
located, nor should two or more bear dens ever be placed in the same
forest patch).

Each of the above events must be represented by a corresponding class
(`Pond`, `BlueberryBush`, `DeerHerd`, and `BearDen`). Each of these
classes must inherit from an abstract `Event` class.

Each kind of event has an **encounter behavior**, which is something
that happens when the player steps into the forest patch containing the
given event. This must be implemented using polymorphism and overrides. 
The `Event` class must have an abstract `encounter` method, and
each of its subclasses should override that method to implement a
different, special behavior. The encounter behaviors of each of the
kinds of events are as follows:

- The pond: When the player encounters the pond:

  - If the player has not yet drank from the pond, then they drink from
    the pond, and the following message is printed to the terminal:

    `You drink from the pond.`

  - Otherwise, the following message is printed to the terminal:

    `You're not thirsty.`

- Blueberry bushes: When the player encounters a blueberry bush, they
  eat it, and the following message is printed to the terminal:

  `You chow down on some tasty blueberries.`

  The blueberry bush should then be removed from the game (it should be
  changed to `None` within the given forest patch).

  Importantly, the game must somehow keep track of how many blueberry
  bushes the player has eaten (e.g., via an integer that gets
  incremented by this encounter method) since completing the game
  requires eating both blueberry bushes.

- The deer herd: When the player encounters the deer herd:

  - If the player has eaten both blueberry bushes and drank from the
    pond, then the following message should be printed to the terminal:

    `You've finished browsing for the day and arrived safely back at the herd.`

    The game should then end.

  - Otherwise, nothing should happen. The game should proceed as normal.

- Bear den: When the player encounters a bear den:

  - If it’s the player’s first time encountering that specific bear den,
    the player should be immediately moved back to their <ins>previous</ins>
    location (i.e., the forest patch that they were on just before
    encountering the bear den), and the following message should be
    printed to the terminal:

    `Whew, that was close! You almost woke a nearby bear.`

  - If it’s the player’s second time encountering that specific bear
    den, then the following message should be printed to the terminal:

    `You woke a nearby bear. It's hungry. Game over.`

    The game should then end.

At the start of the game, and additionally after each of the player’s
movements, the forest should be printed to the terminal. Events are
displayed within the forest grid in their corresponding locations, each
with their own special character. `P` is used to represent the pond; `B`
represents a blueberry bush; `H` represents the deer herd; and `D`
represents a bear den. Empty
forest patches are represented with a space character.

The player is represented as an asterisk (`*`).

For example, at the start of the game, the forest should be displayed
like so:

    ----------------
    | B|  | D|  | P|
    ----------------
    |  |  |  |  |  |
    ----------------
    |  |  | D|  |  |
    ----------------
    |  | D|  |  |  |
    ----------------
    |*H|  |  |  | B|
    ----------------
    Where would you like to go? (Use W/A/S/D to move): 

If the player is in the same forest patch as an event, then both
characters should be displayed (this is why each forest patch is two
characters wide in the above example—to keep everything aligned). Notice
that the player starts out in the bottom-left forest patch along with
the deer herd.

When printing the the forest, you must adhere to these requirements:

- Separate each row of the forest with a line of hyphen characters `-`. There
  should also by a line of hyphen characters at the very top and bottom of
  the printed forest.
- Separate each forest patch in a given row with a pipe character `|`
- Print the proper characters for each event in the proper locations.
- Render as a properly aligned grid. Each line must be the same length.
- If the game is operating in debug mode, indicate the events with the proper
  characters in the proper locations (explained below).

### The player

At the start of the game, the player should be placed in the bottom-left
forest patch (the same patch containing the deer herd).

At the start of each turn, the following message
should be printed to the terminal:

`Where would you like to go? (Use W/A/S/D to move): `

It should then wait for the user to type something in and press enter.
If the user enters “w” or “W”, then the player should move one space up
in the forest. If they enter “a” or “A”, then they should move one space
to the left. If they enter “s” or “S”, then they should move one space
down. If they enter “d” or “D”, then they should move one space to the
right. If the user enters anything other than one of these options, then
the program should print “`Invalid input`”, and the user should be
reprompted for their input.

If the player attempts to move in a direction, but they can’t because
they’re at the edge of the board (e.g., if the player is in the top row,
but they attempt to move up), then the program should print
“`Invalid direction!`”, and the user should be reprompted for their
input.

Whenever the player successfully moves, 1) if the player just moved into
a forest patch containing an event, that event’s encounter behavior
should be triggered; and 2) the game board should be printed again,
depicting the player’s newly updated location. If the game has not
ended, then the player’s next turn should begin, prompting the user for
another input.

## Requirements

As mentioned, you’re only going to implement about half of the game in
this lab. You’ll complete the remaining half in next week’s lab.

For this lab, complete the following:

1.  You are given a `Player` class defined in `player.py`. Review this file 
    and make sure you understand it. You shouldn't need to modify it for this
    lab.

2.  Create an `Event` class.

    - It must be an abstract class

    - It must have an abstract method named `encounter` that accepts one 
      parameter of type `Player` (in addition to the standard `self` parameter).
      It can return whatever type you wish (you will find it useful to
      return *something* from this method to signal what happened in the event).
      
    - It can have other attributes and / or methods if you’d like. It
      can even have other abstract methods. That’s up to you.

> [!TIP] 
> The various overrides of the `encounter` method need to be capable of
> modifying  the player / game state in some way. Use the Player parameter
> to keep track of game state.
>
> Some events should be removed from the board after they’re encountered 
> (specifically the blueberry bushes), but others should not. Consider 
> ways that 
> this method might communicate that information back to the function caller,
> so that the caller knows whether or not it should remove the event afterwards.

3.  Create each of the four derived classes: `Pond`, `BlueberryBush`,
    `DeerHerd`, and `BearDen`.

    - Each of these classes must inherit from the `Event` class

    - Each of these classes must override any and all abstract methods
      that they inherit from the `Event` class (including the encounter
      method, but also others if you choose to create more).

    - When you implement the various overrides of the abstract encounter
      method, you must make a good faith effort to implement them
      correctly so that they do what they’re required to do as specified in
      this document. However, these methods will not actually be called
      by the program / rigorously tested until lab 9.

    - Each of these classes may have additional attributes and / or
      methods if you’d like. That’s up to you.

4.  Create a `ForestPatch` class. It should have a private attribute of
    type `Event | None`, indicating that a given `ForestPatch`
    object *may* have an `Event` object inside it, or it may not (some
    forest patches are empty, indicated by this attribute having the
    value `None` for the given `ForestPatch` object).

    You’ll also need to create some methods in your `ForestPatch` class
    to fulfill the other requirements of this lab. It’s up to you to
    design these methods and implement them.

    The `ForestPatch` class may also have some other attributes if you’d
    like.

> [!TIP]
> Refer to your `Room` class from assignment 7. The `ForestPatch` class
> is very similar.

5.  In `main.py`, create a function named `create_forest` that   
    has no parameters and a return type of 
    `list[list[ForestPatch]]`. It should instantiate your forest as a 
    5x5 2D list, populate it with all events as described below,
    and return it. The events should be placed as follows:

    A `DeerHerd` object should be constructed and placed in the
    bottom-left forest patch (index `[4][0]`). Two `BlueberryBush` objects
    should be constructed and placed in the top-left
    (index `[0][0]`) and bottom-right (index `[4][4]`) forest patches.
    A `Pond` object should be constructed and placed in the
    top-right (index `[0][4]`) forest patch. Three `BearDen` objects
    should be constructed and placed into different random forest
    patches within the forest. The rest of the
    forest patches should be initialized to be empty. Remember: each forest
    patch can contain at most one event.

6.  When the program is executed via `python main.py`, it should use the
    `create_forest` function to create the forest. It should also somehow
    construct the player and place them in the bottom-left forest patch,
    along with the deer herd.

7.  As suggested, you may need to create some additional attributes,
    methods, and / or entire classes beyond those explicitly stated in
    order to fulfill all the above requirements.

> [!IMPORTANT]
> You do not need to implement player movement, winning / losing,
> etc. Some behaviors should be *partially* implemented within
> your `encounter` method overrides, but those overrides do not
> yet need to be *called* anywhere within the program. You’ll
> complete those aspects of the program in lab 9.

## Unit tests

Your program should pass
the unit tests that come with this repository. The TAs will run these
tests to compute a grade. You can run them yourself by running the following
shell command in your terminal within your project's directory:

`python -m pytest tests`

## Rubric
The rubric for this lab is as follows:

- (1.5 pts) for the `Event` class existing in `event.py`,
  being abstract, and having an
  abstract `encounter` method.

- (1 pt) for the `Pond` class existing in `pond.py`, inheriting from the `Event`
  class, and implementing all inherited abstract methods.

- (1 pt) for the `BlueberryBush` class existing in
  `blueberrybush.py`, inheriting from the
  `Event` class, and implementing all inherited abstract methods.

- (1 pt) for the `DeerHerd` class existing in `deer.py`, inheriting from the
  `Event` class, and implementing all inherited abstract methods.

- (1 pt) for the `BearDen` class existing in `bearden.py`,
  inheriting from the `Event`
  class, and implementing all inherited abstract methods.

- (1.5 pts) for the `ForestPatch` class existing in `forestpatch.py` with a
  private `_event` attribute of type `Event | None`.

- (1 pt) for the forest patches in the forest being populated with the
  proper events in the proper places as described

- (1 pt) for your code passing through Mypy (in strict mode) without errors

Manual verification:

- (1 pt) for each `Event` subclass having a reasonable implementation of the 
  `encounter` method.

Possible penalties:

- (-1 pt) for any violations of the course’s style and design guide. If there
  are multiple violations, you will only be penalized -1 pt total.

  As a reminder, here's a summary of the rules:

  - Single Responsibility Principle (SRP) proxy: A
    function shouldn't have more
    than 15 logical lines of code.
  - Don't Repeat Yourself (DRY) principle: Don't copy and paste the same block
    of code several times. Instead, move it into a function and just call the
    function several times.
  - Don't use global variables (global constants, which aren't modified during
    the program's runtime after initialization, are okay).
  - A line of code shouldn't be longer than 80 characters.
  - If your code is very hard to understand, explain it with adjacent comments.

# Acknowledgements
author: Alexander Guyer (<guyera@oregonstate.edu>), CS 162
