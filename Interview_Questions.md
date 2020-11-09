1. Hashing functions

Hashing functions are used to map data of a certain size to fixed-size values. The hash function returns hash values (aka hashes) which are used to index a fix-sized table called a hash table.

2. Collision resolution

Hash collisions are unavoidable due to the "birthday problem". However, hash tables can have collision resolution strategies such as separate chaining with linked lists, list head cells, or other structures. Other strategies include open addressing such as coalesced hashing, cuckoo hashing, hopscotch hashing Robin Hood hashing, and 2-choice hashing. These are just some of the common strategies for collision resolution and all of them require that the keys or pointers to them be stored in the table together with the associated values.

3. Performance of basic hash table operations

Performance of basic hash table operations can be measured with speed analysis and memory utilization. Cache missing and cost of resizing significantly affect the latency of operations on a hash table. With increasing load factor the search and insertion performance of hash tables can be degraded significantly due tot he rise of average cache missing. Resizing also becomes an extreme time-consuming task when hash tables grow to be massive. Sometimes the memory requirement for a table needs to be minimized. One way to reduce memory usage in chaining methods is to eliminate some of the chaining pointers or to replace them with some form of abbreviated pointers.

4. Load factor

Load factor = n/k, where n is the number of entries occupied in the hash table and k is the number of buckets. As the load factor grows larger, the hash table becomes slower (and may even fail to work).

5. Automatic resizing

Hash tables perform well if the number of elements in the table remain proportional to the size of the table, so the load balance can be restricted by increasing the size of the hash table if it gets too full and decrease the size of the hash table if it gets too empty.

6. Various use cases for hash tables

Storage where both insertion and access need to be fast.
Storage where uniqueness is useful.
Storing anything where there is no need to access data in the order that data is inserted.
Search for elements within a large data set

References:

https://en.wikipedia.org/wiki/Hash_table

https://courses.csail.mit.edu/6.006/spring11/rec/rec07.pdf
