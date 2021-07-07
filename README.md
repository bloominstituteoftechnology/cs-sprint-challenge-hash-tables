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
Just riffing since there are no provided questions. Hashing functions are the functions used to take a key value pair, and through different algorithms, transform the key into a statistically unique number, that can then be used to store the value in a particular storage location. There are a couple values and purposes to doing this. One is to have keys with more meaning than an index. Two can be for cryptographic purposes (values can't easily be found without exact keys). Three for complexity improvements leveraging the "meaningfulness" of the keys, against typical structures like arrays who's indexes are mearly position indicators.
2. Collision resolution
Hashing functions do not always result it 100% unique storage locations for the values.  In the instance that your hashing function will try to store two differen key value pairs in the same place, you need to implement some method to avoid overwriting. Chaining multiple values together is one way to deal with this. But that alone is not enough, and could become taxing as values are added. See load factor and resizing.
3. Performance of basic hash table operations
Um not sure what to say here. A hash table should have a way to put key value pairs, get key values pairs, hash in and hash out of storage, calculate load factor and resize up and down.
4. Load factor
Load factor is the ratio of number of values over capacity of your storage.  Basically it is an easy way to conceptualize the likely hood of running into collisions. Since it is possible to have collisions with 8 values in an 8 capacity hashtable, we can never 100% that no collisions will happen. Ultimately too many collisions are going to impact the performance of your hastable, so load factor is a way of understanding how likely you are to have collisions, and then build some logic off of that.  See Automatic resizing.
5. Automatic resizing
Using load factor, you can resize your hashtable to improve it's performance.  If you were only worried about avoiding collisions, you could probably instantiate a hashtable large enough that your input values never collide, but it might be huge.  Alternatively, you didn't care about the lookup speed of your has table, you could jam as many values into a small amount of storage and rely on your collision handling.  But why not find a happy medium?  You can use the load factor as a trigger point for when to shrink or grow your storage automatically, ensuring your hashtable continues to perform optimally.
6. Various use cases for hash tables
Key value pairs have great potential for a meaningful relationship than index element pairs. So you can use hashtables to cleverly get around problems that cause massive complexity in arrays. Clever storage can avoid brutally long searching. Cryptographic hashing algos (not all hashing is cryptographic) is good for protecting where values are stored.

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
