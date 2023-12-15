# The Software Designer Mindset: Pythonic Patterns

Welcome to the Pythonic Patterns course extension! This course provides a distinct perspective on design principles beyond traditional Object-Oriented Design. Furthermore, it delves into patterns such as Registry and Function Builder, demonstrating their seamless integration with modern features in Python. Enhance your software design proficiency, make informed decisions, and contribute to the community's knowledge base.

## Table of Contents

- [The Software Designer Mindset: Pythonic Patterns](#the-software-designer-mindset-pythonic-patterns)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Modules](#modules)
    - [Strategy](#strategy)
    - [Bridge](#bridge)
    - [Template Method](#template-method)
    - [Abstract Factory](#abstract-factory)
    - [Pipeline](#pipeline)
    - [Pub/sub or event handling](#pubsub-or-event-handling)
    - [Registry](#registry)
    - [Command](#command)
    - [Functional Patterns](#functional-patterns)
  - [Prerequisites](#prerequisites)
  - [Do you want to help?](#do-you-want-to-help)

## Introduction

Hello,

I hope you're enjoying the software designer mindset courses. Your decision to acquire Pythonic patterns is one you won't regret, this course is far from ordinary when it comes to design patterns—it holds a unique twist. The design principles I delve into are not just about writing better code; they form a solid foundation for making informed design decisions.

So, what exactly is a design pattern? Think of it as a versatile, reusable solution to common problems. The traditional Object-Oriented Design, with its intricate patterns, no longer reigns supreme. We've shifted towards iterative software development has led to a pragmatic "Move fast and break things" mentality. While beneficial for quick progress, it often results in technical debt for more mature platforms.

This course takes a fresh approach. Instead of a conventional rundown of patterns, I've curated a list based on two decades of practical experience. We'll explore patterns like Registry and Function Builder, going beyond the confines of strict object-oriented programming. I'll show you how to naturally incorporate these patterns using modern features available in Python and other languages. 

This course serves as a seamless extension of the software design mindset, integrating power with a designer's perspective. I'm eager to hear your thoughts on the material, and I hope it sparks creativity in your software development endeavors.

If you're ready, let's dive into this journey together.

## Modules

### Strategy

**Topics Covered**

 - Sequence Of If-Else Statement
 - Functional And Partial Application

### Bridge

**Topics Covered**

 - Classic Bridge
 - Using Protocols
 - Types As An Abstraction Layer
 - Handling Many Imports

### Template Method


**Topics Covered**

 - Tuple to supply functions to the template
 - One large function/process with many small varieties
  
### Abstract Factory


**Topics Covered**

 - dict of functions to create something
 - when to use it: sequence of if-else statement, many imports in a file

### Pipeline


**Topics Covered**
   - Chain of Responsibility
   - List of functions where result of previous is passed to next
   - Function composition
   - pass the pipeline itself as an object with handy extra functions
   - when to use it: using temporary variables to execute chain of functions

### Pub/sub or event handling


**Topics Covered**
   - Observer pattern
   - Mediator pattern (this is closer to event bus)
     - https://lostechies.com/derickbailey/2013/03/18/event-aggregator-andorvs-mediator-a-tale-of-two-patterns/
   - with event handler functions
   - when to use it: your functions do a lot of extra stuff that's not the responsibility of the function and don't affect the outcome that much
### Registry


**Topics Covered**
   - registration process, read info from JSON or YAML file
   - when to use it: you want the user to be able to define custom elements in a structure, but the structure itself is fixed, you want to change the elements in the structure from a text file without having to look at the code.
   - Show examples of using it combined with other design patterns (i.e. registry with factory and with strategy, mention pipeline as well)
### Command


**Topics Covered**

   - with partial application (prepare command before executing it)
   - when to use it: if you need undo/redo behavior, if you keep track of previous state and it becomes cumbersome

### Functional Patterns


**Topics Covered**
   - passing a function as an argument
     - so you can call it later, or not at all if not needed
     - callback mechanism (i.e. initialize a button with an on_click handler)
   - partial function application ("function preparation") to make another function match what you expect
   - function builder: give something the data/settings it needs to create a custom function for you with different arguments
   - function adapter: function that takes a function and returns another one with a different signature (show in combination with i.e. strategy pattern to convert signature)



## Prerequisites
- Beginner knowledge of Python
- Software Designer Mindset

## Do you want to help?
We at arjancodes would love too hear suggestions, improvements and more to the courses. Is there a missing test?, Is there a typo somewhere? Or is there an exercise that should exist? Then contact support@arjancodes.com or simply make a PR, which will be reviewed, with the changes and updates you want to have.

You will be credited on your work as an contributor to the course!%