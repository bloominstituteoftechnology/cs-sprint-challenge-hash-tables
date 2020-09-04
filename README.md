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
-Any functions that can be used to map data size to fixed-size values. The valuses are returned by a hash function called hash values, hash codes, digets, or hashes. The values are used to index a hash table 

2. Collision resolution
-When two items hash the same slot, there must be a systematic mythod for placing the item in the table. this process is called Collision resolution.
-Open addressing: with this method a hash collision is resolved by probing which indicates that there is no such key in the table.
-Probing: Is searching through alternate location sin the array until it either the target record is found, or an unused array slot is found
    - Linear probing: in which the interval between probes is fixed — often set to 1
    - Quadratic probing: in which the interval between probes increases quadratically 
    - Double hashing: in which the interval between probes is fixed for each record but is computed by another hash function

3. Performance of basic hash table operations
-Hash tables suffer from `O(n)` worst time complexity due to two reasons:
    1. If too many elements were hashed into the same key: looking inside this key may take O(n) time.
    2. Once a hash table has passed its load balance - it has to rehash [create a new bigger table, and re-insert each element to the table].
-However, it is said to be O(1) average and amortized case because:
    1. It is very rare that many items will be hashed to the same key [if you chose a good hash function and you don't have too big load balance.
    2. The rehash operation, which is `O(n)`, can at most happen after n/2 ops, which are all assumed O(1): Thus when you sum the average time per op, you get : (n*O(1) + O(n)) / n) = O(1)

4. Load factor
-The load factor is a measure that decides when ot increase the hashmap capacity to maintain the get() and put() operations of O(1). The default load factor is 0.75f

5. Automatic resizing
-When you resize the table, double the size and then round up to the first prime number larger than that.

6. Various use cases for hash tables
-Search for elements within a large data set
-Find duplicate elements in a data set
-Quickly store and retive elements from a large data set

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
