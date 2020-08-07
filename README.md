# Sprint Challenge: Hash Tables

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

   A hashing function is a function that takes any data as an input and returns an output that is a number. The hash function must be consistent (deterministic), meaning that given the same input, the output must be the same every time. If it is not deterministic, then it is not a hashing function. Another requirement for a function to be a hashing function is that different input data should return different output numbers. Finally, a hashing function must return numbers within a specified range.

2. Collision resolution

   Hashing functions are almost never perfect unless you know all the possible data inputs ahead of time. In reality, hashing functions do return the same numerical output for different data inputs, and when they do, this is called a collision. In order to handle these collisions that result from imperfect hashing, we allow chaining at hash indexes to accommodate values that are hashed to the same index. This chaining is most often accomplished using the singly linked list data structure. When searching for a specific value, one must identify its hash index and then traverse each node in the linked list, if there is one at that index, and return the value at that node once it is located.

3) Performance of basic hash table operations

   Performance of basic hash table operations on average are associated with a constant, O(1), runtime complexity. In worse case scenarios, when there exists a linked list at a specific hash index, the runtime complexity becomes linear or O(n), as you have to traverse the length of the list at that index until the value that is sought is located. However, these worse case scenarios are mitigated by the fact that there should only exist a few elements at a specified index at any given time and when a hash table should reach critical mass or a “load balance” of approximately 70%, the table will be resized to accommodate a longer length and therefor a greater modulo when determining a specific hash index.

4) Load factor

   The load factor of a hash table is the total number of elements that exist in the table divided by the total length of the list accommodating the table. This will give you a percentage representing how ‘full’ the table is.

5) Automatic resizing

   In most cases, when the load factor reaches 70%, the table doubles in size and all the elements are re-hashed to new indexes. Also, when the load factor is too low, around 30% or less, the table should also be resized due to the fact that memory is being wasted to house the data. In this case, it is common to halve the size of the array and rehash the values.

6) Various use cases for hash tables

   Hash tables are tremendously useful for a variety of reasons. One of the most common use case is for lookups, due to the fact that on average hash tables employ near constant time runtime complexities. One example of a lookup that is hugely important is DNS resolution, without which the internet would not exist. Another important use case for hash tables is duplicate prevention. Due to their very nature, hash tables do not allow duplicates. One final use case is for caching. Caching allows us to store information regarding computations that have already been made so that when they are needed again the expensive computations no longer need to be carried out, rather the value just need be looked up and returned to the client.

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

_Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)_

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
