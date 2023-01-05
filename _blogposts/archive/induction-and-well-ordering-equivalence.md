---
title: Equivalence of Mathematical Induction and Well-Ordering
author: Daniel Guo
excerpt: Proof that the well-ordering principle and the principle of mathematical induction are logically equivalent.
posted: Dec. 21 2019
order: 2
---

In this post, we will see that the well-ordering principle (wop) and the principle of mathematical induction are logically equivalent. This means that given one, we are able to obtain the other. Our approach will be to prove the following statements in the given order
1. the equivalence of weak and strong induction
2. strong induction implies wop
3. wop implies strong induction

First, we give the statements of the principles.

#### Well-Ordering Principle
Any nonempty set of positive integers has a least element.


#### Principle of Induction
For the two forms of induction, let $P(n)$ be some proposition depending on $n$. For instance, $P(n)$ could be the proposition "there are n people in this room". Then "$P(n)$ holds for all $n \in \mathbb{Z}^{+}$" means "there are $n$ people in this room for every positive integer $n$" (which is impossible unless you're in an infinitely large room).

##### Weak Induction
To prove that $P(n)$ holds for all $n \in \mathbb{Z}^{+}$, we just need to show two steps <br>
**1.1** Base step: $P(1)$ holds <br>
**1.2** Inductive step: $P(k)$ implies $P(k + 1)$

##### Strong Induction
To prove that $P(n)$ holds for all $n \in \mathbb{Z}^{+}$, we just need to show two steps <br>
**2.1** Base step: $P(1)$ holds <br>
**2.2** Inductive step: $P(1) \land \dots \land P(k)$ implies $P(k + 1)$

We use $\forall n \in \mathbb{Z}^{+} P(n)$ as a shorthand for the statement that $P(n)$ holds for all $n \in \mathbb{Z}^{+}$.

### 1. Equivalence of Weak and Strong Induction
The idea here will be to show that when we are proving a statement of the form $\forall n \in \mathbb{Z}^{+} P(n)$, if we can use one form of induction, then we can also use the other form of induction.

#### Weak Implies Strong
First assume we can prove $\forall n \in \mathbb{Z}^{+} P(n)$ using weak induction, so assume 1.1 and 1.2 hold. Our approach will be to show that 2.1 and 2.2 hold as well. Clearly 2.1 holds, since it is the same as 1.1. Though not as obvious, 2.2 logically follows from 1.2. If
\begin{equation}
P(k) \rightarrow P(k + 1),
\end{equation}
then
\begin{equation}
P(1) \land \dots \land P(k) \rightarrow P(k + 1).
\end{equation}
We can show this more rigorously using truth tables and cases... left as an exercise to the reader :). I think it's simple enough to skip, but for any readers who find this unclear, I would suggest actually going through the rigorous proof. With this, we have completed one direction of the proof.

#### Strong Implies Weak
Now assume we can prove $\forall n \in \mathbb{Z}^{+} P(n)$ using strong induction, so assume 2.1 and 2.2 hold. We define a new proposition $Q(n)$ as
\begin{equation}
Q(n) = P(1) \land \dots \land P(n).
\end{equation}
It is not too difficult to see (by expanding out the conjunctions) that $\forall n \in \mathbb{Z}^{+} P(n)$ is logically equivalent to $\forall n \in \mathbb{Z}^{+} Q(n)$ (meaning one is true if and only if the other is true). Now our goal will be to show that $\forall n \in \mathbb{Z}^{+} Q(n)$ can be proven using weak induction. In other words, we want to show that 1.1 and 1.2 hold for $\forall n \in \mathbb{Z}^{+} Q(n)$. It is important to note that now we are looking at 1.1 and 1.2 for the statement involving $Q$, not $P$. See that $Q(1)$ is the same as $P(1)$, so 1.1 holds.

Now by 2.2, we have that $P(1) \land \dots \land P(k)$ implies $P(k + 1)$. Now consider that $A \rightarrow B$ is the same as $A \rightarrow A \land B$. <sup>1</sup> Thus, we can conclude that
\begin{equation}
P(1) \land \dots \land P(k) \rightarrow P(1) \land \dots \land P(k) \land P(k + 1).
\end{equation}
Thus, we arrive at the desired conclusion that $Q(k)$ implies $Q(k + 1)$, which is 1.2. This completes the other direction of the proof.

#### Possible Confusion
It occurs to me that there might be some confusion about why the way we proved their equivalence actually works. A concrete way to pose the question would be why does assuming weak induction works and then showing 2.1 and 2.2 prove that weak implies strong? The way to think about this is as follows. We want to show:
<p style="text-align: center;">
for some statement $\forall n \in \mathbb{Z}^{+} P(n)$, if we can prove it using weak induction, then we can also prove it using strong induction.
</p>
In other words, we want to show that whenever weak induction works, strong induction also works. So in our proof, we showed that 2.1 and 2.2 would hold if weak induction works. This means that strong induction would conclude that the statement is true; thus, strong induction works as well. The other direction of the problem has a similar reasoning.

**Edit 12/24/2019** Another point of confusion was pointed out to me. How are we equating a theorem and a proof technique? Instead of thinking about the induction principles as proof techniques, it might be useful to think of them as statements. To rephrase weak induction more clearly as a statement, we can say: if 1.1 and 1.2 hold, then $P(n)$ holds for all $n \in \mathbb{Z}^{+}$. This makes it obvious that we are actually proving the logical equivalence of statements.

### 2. Strong Induction Implies WOP
We prove this by contradiction, so assume that the well-ordering principle is false. Then there exists some nonempty set $S \subseteq \mathbb{Z}^{+}$, which does not have a least element. Now consider the following statement
<p style="text-align: center;">
$P(n)$ says that $n \not \in S$.
</p>
We will prove that $P(n)$ is true for all $n \in \mathbb{Z}^{+}$ by induction. If $1 \in S$, then it would have to be the least element, which by our assumption of $S$ cannot happen; thus $1 \not \in S$ and $P(1)$ holds. This takes care of the base step. For the inductive step, assume $P(1) \land \dots \land P(k)$, so $1 \not \in S$, $\dots$, $k \not \in S$. Then if $k + 1 \in S$, $k + 1$ would be the least element, which is impossible; thus $k + 1 \not \in S$ and $P(k + 1)$ holds. Thus by strong induction, we have shown $\forall n \in \mathbb{Z}^{+} P(n)$, or for all positive integers $n$, $n \not \in S$. Thus, $S$ must be empty, which is the desired contradiction.

### 3. WOP Implies Strong Induction
We assume the well-ordering principle and want to show that for some statement $\forall n \in \mathbb{Z}^{+} P(n)$, if 2.1 and 2.2 hold, then $\forall n \in \mathbb{Z}^{+} P(n)$ holds as well. To that end, assume 2.1 and 2.2 hold and consider the set $S$ which contains those $n$ such that $P(n)$ does not hold. More formally, define
\begin{equation}
S = \\{n \mid \lnot P(n)\\}.
\end{equation}
We will show that $S = \emptyset$ by contradiction. Suppose $S \neq \emptyset$, so by WOP, there exists some least element in $S$, denote it $k + 1$. Note that $k + 1 \neq 1$, since 2.1 asserts that $P(1)$ holds. Thus, $k + 1 > 1$. Since $k + 1$ is the least element in $S$, this means that $P(1), \dots, P(k)$ are all true. Then, it follows from 2.2 that $P(k + 1)$ must be true as well, which is the desired contradiction. Thus, $S = \emptyset$, and $\forall n \in \mathbb{Z}^{+} P(n)$ holds as desired.

### Concluding Remarks
This completes the proof of the main statement. The ideas are pretty simple, but I think it's a pretty cool result nonetheless. This is my first write-up of a math related topic, so please feel free to give me feedback (typos, lack of clarity, etc)! It is helpful for me to improve my own writing abilities and will be appreciated. I hope you all enjoyed and were able to learn something!

##### Footnotes
<sup>1</sup> This can be easily verified with truth tables.
