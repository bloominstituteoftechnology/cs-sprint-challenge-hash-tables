# Sprint Challenge: Hash Tables
#Questions -> complete

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
2. Collision resolution
3. Performance of basic hash table operations
4. Load factor
5. Automatic resizing
6. Various use cases for hash tables

1. Hashing functions
    R: A hash function is a function where the input is any data, and the output is a number.

2. Collision resolution
    R: When two items hash to the same slot, we must have a systematic method for placing the second item in the hash table. This process is called collision resolution. We can use Chaining for collision resolution.

3. Performance of basic hash table operations
    R: The performance of hash tables for search, insertion, and deletion is constant time (O(1)) in the average case. However, in the worst case, those same operations are done in linear time (O(n)). The more collisions that our hash table has, the less performant the hash table is.

4. Load factor
    R:Hash tables use an array for storage, so to calculate the load factor we take the of items stored in the hash table divided by the number of slots.

5. Automatic resizing
    R:Resizing is considered to be an expensive operation, so we don't want to resize too often. If the Hash Table
    is too large for the data that is being stored, then memory will be wasted, if the Hast Table is too small for the data being stored then we will run out of slots/storage. One way to know when to resize your hash table is to compute the load factor whenever an item is inserted or deleted into the hash table. If the load factor is too high or too low, then you need to resize.


6. Various use cases for hash tables
    R:  1. Searching for elements within a large data set
        2. Find duplicate elements in a data set
        3. Quickly store and retrieve elements from a large data set


We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
