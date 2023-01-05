---
title: Theory Behind Hash Tables
author: Daniel Guo
excerpt: We dive into how hash tables work from an abstract standpoint.
posted: Dec. 29 2019
order: 4
---

Hash tables are important in many computer applications, particularly for quick storage of data that's constantly changing. I think the theory behind them is really interesting, and I hope everyone can gain a deeper understanding of this particular data structure from this abstract approach.

The plan is to cover each of the following topics
1. Dictionary ADT<sup>1</sup>
2. Naive Hash Table and Collisions
3. Universal Hashing
4. Resolving Collisions
5. Perfect Hashing

### Dictionary
**Definition** A *dictionary* is an abstract data type which supports the three following operations
1. Insert $x$. puts $x$ "inside" of the dictionary.
2. Delete $x$. undoes the insertion of $x$.
3. Lookup $x$. determines whether or not $x$ is "inside" of the dictionary.

To illustrate the concept, let's look at a simple implementation of a dictionary.

#### Linked Lists
Hopefully the reader is familar with the basic concept of a linked list<sup>2</sup>. This supports the $3$ operations specified by the dictionary ADT. We can insert $x$ in $O(1)$ time by just adding $x$ to the head of the list. However, delete $x$ and lookup $x$ are $O(n)$ time, since in the worst case, we'd need to scan through the entire list.

Linked lists are very space efficient, but the time complexity of delete and lookup is pretty bad. This is why we don't typically use linked lists if we need these operations.

### Naive Hash Table and Issues
Some important notes on notation first. The *key space* or *universe* is the set of possible keys which could be inserted into our dictionary, denoted $U$. The set of keys which are actually relevant to our application (will be used in our dictionary) is denoted $S$. Typically, $|S| \ll |U|$. For convenience, let $n = |S|$ and $N = |U|$. The keys are items of some type which differ by application. For example, they could be IP addresses or names.

For our purposes, we may assume that the key space is only integers since even noninteger keys are stored as numeric values (ASCII) by computers. Thus, let us assume that $U = \\{1, 2, \dots, N\\}$.

To store the keys, we use a *table*, which is basically just an array. The table has some number of locations, denote this number by $m$, which are referenced by indices $0, 1, \dots, m - 1$. We can store our keys in the locations. An important aspect of tables is that we can access a given location by its index in $O(1)$ time (just like with arrays).

**Definition** A *hash function* is some function
\\[
    h: U \to \\{0, 1, \dots, m - 1\\},
\\]
where $U$ is some set.

We can use this to "assign" each key in our universe $U$ to some location in our table.

One thing to note is that we need to be able to compute $h(x)$ for $x \in U$ in $O(1)$ time. An example of such a hash function could be $h(x) = x \bmod m$. We will talk more about hash functions later, but this pretty much completes everything we need to implement our naive hash table.

#### Naive Hash Table Implementation
We initialize our table with all locations empty at first, and we perform each operation as follows
1. Insert $x$. put $x$ at the location indexed by $h(x)$ in our table.
2. Delete $x$. make empty the location indexed by $h(x)$ in our table.
3. Lookup $x$. check whether or not the location indexed by $h(x)$ in our table is empty.

some psuedocode

```
// Let h be the hash function
class naive_hashtable:
    int[] table

    init(int table_size):
        table = int[table_size]
    
    insert(int x):
        table[h(x)] = x
    
    delete(int x):
        table[h(x)] = empty
    
    lookup(int x):
        return table[h(x)] == x
```

#### Collisions
This may seem pretty good at first, since we have $O(1)$ time complexity for each of these operations. The problem with this is that usually $m \ll N$, since $N$ is the size of the universe (all possible inputs) and $m$ is the size of our table which we need to load in memory. By the pigeonhole principle<sup>3</sup>, there must exist $x_{1}, x_{2} \in U$ such that $h(x_{1}) = h(x_{2})$. Then if we insert $x_{1}$ and $x_{2}$, they will be sent to the same location (known as a collision) and we will have problems. We will talk about how to resolve this issue later.

### Universal Hashing
We haven't really talked much about what a hash function is. We've described how we use one, and our goal is to maintain the $O(1)$ time complexity for each of the operations. This gives us some ideas about what we properties we want one to have. Let $h: U \to \\{0, 1, \dots, m - 1\\}$ be a hash function.
1. We want $h$ to be easy and quick to compute.
2. We also want $h$ to distribute the keys as uniformly as possible inside the table. Imprecisely, this means that for whatever $U$ is, $h$ should spread the keys evenly among $\\{0, 1, \dots, m - 1\\}$ and not have too many collisions.

Unfortunately, this second point is impossible.

**Claim** For any hash function $h$, we can find a set of keys $S$ of size $M$ such that $h$ sends every key in $S$ to the same location.

**Proof** Consider some set of keys $S'$ of size $(M - 1)m + 1$. By the pigeonhole principle, there must exist some $i \in \\{0, 1, \dots, m - 1\\}$ such that $h$ sends $M$ elements of $S'$ to $i$. Then we just let $S$ be the set of these $M$ elements.

This is a pretty big problem. How can we use a good hash function if one doesn't exist? The solution is randomizing our construction of $h$. We will create a *family* of hash functions $H$ such that probabilistically, picking a $h \in H$ will give us the properties we want. In this sense, we want to have conditions on $H$, not each $h \in H$, to guarantee an even spread among $\\{0, 1, \dots, m - 1\\}$.

Let's make this idea a little bit more concrete. A valiant attempt would be to ask for any key to have equal probability of being mapped to each location. However, this actually isn't quite what we want. Consider $H = \\{h_{1}, \dots, h_{m}\\}$ such that $h_{i}(x) = i - 1$ for $x \in U$. Then, true enough, given any $x \in U$, the liklihood that $x$ maps to $i \in \\{0, 1, \dots, m - 1\\}$ is $\frac{1}{m}$ as we randomly pick $h \in H$. But this hash function is terrible! It maps every key to the same location. This means we need to reconsider the condition on $H$.

#### Universal Family of Hash Functions
Turns out, the condition we actually want is the following

**Definition** A family of hash function is *universal* if for any $x_{1}, x_{2} \in U$ with $x_{1} \neq x_{2}$, if we choose $h \in H$ uniformly randomly, then
\\[
    \text{Prob}[h(x_{1}) = h(x_{2})] \leq \frac{1}{m}.
\\]

It takes a little bit of work to show that this is the condition we actually want. Remember that our goal is for $H$ to be such that for any set of keys from the universe, if we uniformly randomly pick $h \in H$, we will get on average an even spread over the locations. This brings us to the next claim.

**Claim** Suppose $H$ is universal. If we pick $h \in H$ uniformly randomly and $S$ is the set of keys relevant to our application (the ones we will hash), then for some key $x \in S$,
\\[
    E[\text{# collisions with $x$}] < \frac{n}{m},
\\]
where $|S| = n$, and there are $m$ slots in our table.

See that this is exactly the property we refer to when we describe an even spread. Now let's prove it.

**Proof** Let $C_{y}$ be $1$ if $h(y) = h(x)$ with $y \neq x$ and $0$ otherwise, and let $C$ be the # of keys which collide with $x$. Then,
\\[
    \text{E}[C] = \text{E}[\sum_{y \in S \setminus \\{x\\}} C_{y}] = \sum_{y \in S \setminus \\{x\\}} \text{E}[C_{y}] \leq \sum_{y \in S \setminus \\{x\\}} \frac{1}{m} = \frac{n - 1}{m} < \frac{n}{m}.
\\]

In particular, if $m = n$, then we would expect $< 1$, or $0$ collisions.

#### Constructing a Universal Family of Hash Functions
We now discuss one method to construct a universal family of hash functions. This is called the *Matrix Method*.

Assume that the keys are $u$-bits long, so the size of the universe is $N = 2^{u}$, and also assume that the size of the table is $m = 2^{b}$ (is a power of $2$). $H$ is the set of all $b \times u$ binary matrices. Let $h \in H$ and $x \in U$. Then, $h(x) = hx \bmod 2$ denoting binary matrix vector multiplication. The result is a vector of length $b$, which represents a particular location in the table.

**Claim** $H$ is universal.

**Proof** Consider $x_{1}, x_{2} \in H$ with $x_{1} \neq x_{2}$. There must exist some bit $i$ in $x_{1}$ and $x_{2}$ which differs. Without loss of generality, assume $x_{1}[i] = 1$ and $x_{2}[i] = 0$. Now consider the hash functions in $H$ which are identical except in the $i$th column, call this set $H'$. Now see that for any $h_{1}, h_{2} \in H'$, $h_{1}(x_{2}) = h_{2}(x_{2})$. We now claim that for any two distinct $h_{1}, h_{2} \in H$, $h_{1}(x_{1}) \neq h_{2}(x_{1})$.

To see this, consider what happens if two hash functions $h_{1}, h_{2} \in H'$ are different in the $i$th column. There must be some bit which is different, let it be the $j$th one. Now see that necessarily $h_{1}(x_{2})[j] \neq h_{2}(x_{2})[j]$, which is the desired result.

Now see that $H'$ is of size $2^{b}$ and there exists only one $h \in H'$ such that $h(x_{1}) = h(x_{2})$. Thus, if we uniformly randomly pick $h \in H$, $\text{Prob}[h(x_{1}) = h(x_{2})] \leq \frac{1}{2^{b}} = \frac{1}{m}$, and so $H$ is universal.

### Resolving Collisions
We still need to deal with the fact that no matter what, we will probably still have collisions in our hash table even with a universal family of hash functions, so we need a method to deal with that. There are two main ways to change the 3 operations defined by the dictionary ADT: open addressing and separate chaining. For both these methods, assume $h \in H$ is a hash function we've uniformly randomly picked from the universal family of hash functions $H$.

#### Open Addressing
The idea is when we have a collision when we insert some $x$, we just keep moving through the table until we find an empty slot and put $x$ there.
1. Insert $x$. check location $h(x)$ in the table. if it is not empty, then check location $(h(x) + 1) \bmod m$. keep checking until we find an empty location and put $x$ there. if we return to location $h(x)$, then the table is full.
2. Delete $x$. check location $h(x)$ in the table. if $x$ is not there, then check location $(h(x) + 1) \bmod m$. keep checking until we find $x$ and set that location to empty. if we return to locatiom $h(x)$, then $x$ is not in the table.
3. Lookup $x$. check location $h(x)$ in the table. if $x$ is not there, then check location $(h(x) + 1) \bmod m$. keep checking until we find $x$. if we return to location $h(x)$, then $x$ is not in the table.

This specific method is called linear probing. Instead of checking $(h(x) + 1) \bmod m$ after $h(x)$, we might check $(h(x) + i^{2}) \bmod m$, where $i$ is the iteration. This is quadratic probing.

some psuedocode
    {% raw %}
    // Let h be the hash function
    class naive_hashtable:
        int[] table

        init(int table_size):
            table = int[table_size]
        
        insert(int x):
            for i in 0 to table.size - 1:
                if(table[(h(x) + i) % m] == empty):
                    table[(h(x) + i) % m] = x
                    return
            return error: table is full

        delete(int x):
            for i in 0 to table.size - 1:
                if(table[(h(x) + i) % m] == x):
                    table[(h(x) + i) % m] = empty
                    return
            return error: x is not in table
        
        lookup(int x):
            for i in 0 to table.size - 1:
                if(table[(h(x) + i) % m] == x):
                    return True
            return False
    {% endraw %}

#### Separate Chaining
The idea is we will have a list at each location in the table. Whenever we have a collision, instead of moving $x$ to a different location in the table, we just append it to the list.
1. Insert $x$. append $x$ to the list at the location indexed by $h(x)$ in our table.
2. Delete $x$. search through the list at the location indexed by $h(x)$ in our table and remove $x$ when we find it.
3. Lookup $x$. check whether or not $x$ is in the list at the location indexed by $h(x)$ in our table is empty.

some psuedocode
    {% raw %}
    // Let h be the hash function
    class naive_hashtable:
        list[] table

        init(int table_size):
            table = list[table_size]
        
        insert(int x):
            table[h(x)].append(x)
        
        delete(int x):
            for i in 0 to table[h(x)].size - 1:
                if(table[h(x)][i] == x):
                    table[h(x).remove(i)]
                    return
        
        lookup(int x):
            for i in 0 to table[h(x)].size - 1:
                if(table[h(x)][i] == x):
                    return True
            return False
    {% endraw %}

##### Time Complexity Analysis
We will perform time complexity analysis on the separate chaining method. Since we expect $< \frac{n}{m}$ collisions at each slot, we would expect that each list at each location of the table has length has than $\frac{n}{m}$. Now remember that $m$ is the size of the table and $n$ is the size of the set of relevant keys to our application. Thus, as long as we have an approximation of $n$, we can pick $m = O(n)$, so then each list is expected to have length less than some constant $c$. Thus, each operation can be expected to have $O(1)$ time complexity.

In the case where we don't know the size of $n$ beforehand, we can do something called dynamic resizing. I'm not too sure on how this works, but I do know that the dynamic resizing allows each operation to have amortized $O(1)$ time complexity.

### Perfect Hashing
We've constructed a pretty great hash table with the methods we've discussed so far. However, universal hashing only guaranteed us $O(1)$ *expected* time complexity; what we actually want is a guarantee about the worst case performance. Can we achieve $O(1)$ worst case time complexity for each of the operations if we fix $S$? Yes, using perfect hashing.

**Definition** A hash function is *perfect* if using it allows all operations to have $O(1)$ worst case time complexity.

**Corollary** A hash function is perfect if using it results in no collisions.

I will describe one method to achieve perfect hashing using $O(n^{2})$ space, but there does exist a method using $O(n)$ space<sup>4</sup>.

**Claim** If we use a table of size $m = n^{2}$ and uniformly randomly pick $h \in H$, where $H$ is a universal family of hash functions, then the probability that $h$ results in no collisions is $> \frac{1}{2}$.

**Proof**<sup>5</sup> There are $\binom{n}{2}$ pairs of keys in $S$. Since $H$ is a universal family of hash functions, and using our previous result, we know that for any two keys $x_{1}, x_{2} \in S$ with $x_{1} \neq x_{2}$, $\text{Prob}[h(x_{1}) = h(x_{2})] = \frac{1}{m}$. Thus, the probability of no collisions is
\\[
    1 - \frac{\binom{n}{2}}{m} > \frac{1}{2}.
\\]

Since the probability is $> \frac{1}{2}$, we can just try a random $h \in H$. If it results in collisions, then we try a different $h' \in H$. On average, we will only need to do this twice.

#### Putting It All Together
We've built up a lot of concepts; now let's just implement (in our minds) a hash table with worst case $O(1)$ operations, where we have fixed $S$. We first build a universal family of hash tables $H$. Then, we create an empty table of size $|S|^{2}$. We uniformly randomly choose a $h' \in H$ and hash everything in $S$. If we get any collisions, we choose another $h'' \in H$ and repeat until we get no collisions. Now using this hash function $h$, we have a hash table with worst case $O(1)$ operations.

##### Footnotes
<sup>1</sup> An abstract data type (or ADT) is basically a description of a data structure which specifies its behavior but not its implementation. A data structure is an implementation of an ADT.

<sup>2</sup> If not, just google "linked list data structure". Just the basic understanding is necessary, since we're only looking at it as an example of a dictionary.

<sup>3</sup> Pigeonhole principle is the idea that if we try to fit $m$ pigeons into $n$ holes, where $m > n$, then one hole will have more than one pigeon. I'll probably talk more about this principle in some other post, since it has a lot of fun applications in proofs.

<sup>4</sup> The method which uses $O(n^{2})$ is a bit more complicated. The basic idea is we have regular table of size $m$. When we hash everything into it, we will have collisions. Then for each location in the table, we do the same thing as the $O(n^{2})$ method. It takes some analysis to show that this is $O(n)$ which is the main reason I'm just talking about the $O(n^{2})$ method.

<sup>5</sup> This proof shares a lot of themes with the birthday paradox.