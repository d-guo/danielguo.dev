---
title: A Formal Approach to Propositional Logic
author: Daniel Guo
excerpt: A formal recursive construction of languages in propositional logic.
posted: Dec. 24 2019
order: 3
---

Our main goal is to learn how to construct a formal language in propositional logic. What is a formal language in propositional logic?

**Definition** A *language* is the set of all well-formed formulas (or wffs) based on some predetermined set of symbols (similar to the alphabet).

What are well-formed formulas? Intuitively, they are the sentences of our language. We will give the formal definition later.

The steps in our construction will be

1. Stating our set of symbols
2. Giving meaning to our symbols
3. Constructing wffs and extending truth assignments

Then we will go through a couple fun exercises and proofs about the language we have constructed to gain more understanding.

### Set of Symbols
We start with some set of symbols. Intuitively, these are like the letters of our language; they are the alphabet upon which we can use to write out sentences. Don't worry about what they mean for now (also ignore the "Intuitive Purpose" column); we'll get to that later. We choose the following symbols for our language

| Symbol | $\; \; \; \; \; \; \;$ | Intuitive Purpose |
|:-|:-|:-|
| ( | | grammar symbol |
| ) | | grammar symbol |
| $\lnot$ | | negation connective |
| $\land$ | | conjunctive connective |
| $\lor$ | | disjunctive connective |
| $\rightarrow$ | | conditional connective |
| $\leftrightarrow$ | | biconditional connective |
| $A_{1}$ | | first sentence symbol |
| ... | | ... |
| $A_{n}$ | | $n$th sentence symbol |
| ... | | ... |

It should be noted that our decision the use $\\{A_{1}, A_{2}, \dots\\}$ as our sentence symbols is perhaps arbitrary. We could also use an uncountable set of sentence symbols. I learned it with the countable set, but I'm not sure if there's any important difference (I would guess that there is). I know one thing is that the proof of the compactness theorem changes slightly. For the purpose of this post, I will stick with the countable set.

### Meaning of the Symbols
We want to be able to interpret our language in english. For example, if $A_{1}$ means "the sky is cloudy" and $A_{2}$ means "it is raining", then we want to have well defined meanings for statements like $A_{1} \land A_{2}$ and $(\lnot A_{1}) \land A_{2}$. With this in mind, we think of "$($" and "$)$" as the grammar symbols which we use to help interpret our sentences. The connective symbols ($\lnot, \land, \lor, \rightarrow, \leftrightarrow$) serve their expected purposes ("not", "and", "or", "implies", "implies", "if and only if") which are hopefully familiar to readers.

The sentence symbols are a bit special in this regard. We want to use them as "placeholders" of sorts which represent a proposition in english. To this end, we define something called a truth assignment.

**Definition** A *truth assignment* is some function
\\[
    v: \\{A_{i} \mid i \in \mathbb{N}\\} \to \\{T, F\\}
\\]
which "assigns" each sentence symbol a True or False value.

#### Check of Understanding
Let $A_{1}$ and $A_{2}$ be translated as above. What would we expect the statementes $A_{1} \rightarrow A_{2}$, $A_{1} \land A_{2}$, and $(\lnot A_{1}) \land (\lnot A_{2})$ to mean? <sup>1</sup>

If we had only chosen $n$ sentence symbols in our set of symbols, how many possible truth assignments could we have? What happens to this number if we removed $\lnot$ from our language? <sup>2</sup>

### Constructing Well-formed Formulas and Extending Truth Assignments
Consider a "sentence" in our language like $\land \lor A_{1}$. This doesn't really have an english translation, so we'd like to avoid "sentences" like these when we define how to construct the well-formed formulas in our language. All that said, the construction is actually pretty natural.

**Definition** The set of *well-formed formulas* can be constructed as follows
1. All sentence symbols are wffs.
2. Let $\alpha$ and $\beta$ be wffs. Then the following are also wffs

* $(\lnot \alpha)$
* $(\alpha \land \beta)$
* $(\alpha \lor \beta)$
* $(\alpha \rightarrow \beta)$
* $(\alpha \leftrightarrow \beta)$

And these are the ONLY ways to constuct a wff in our language. This is great! We now have very specific rules on how to build wffs, so "sentences" like $\land \lor A_{1}$ will never exist in our language. Another upside is that each wff has a *unique* construction tree. For example, the wff $((A_{1} \lor A_{2}) \land A_{3})$ can be constructed by using the second construction rule on the wffs $(A_{1} \lor A_{2})$ and $A_{3}$. And the wff $(A_{1} \lor A_{2})$ can be constructed using the third construction rule on the wffs $A_{1}$ and $A_{2}$. This is useful in how a program might look at a wff.

A quick note about notation. If $S$ is the set of all sentence symbols (in our case this is $\\{A_{i} \mid i \in \mathbb{N}\\}$), then the set of wffs is sometimes denoted $S^{\text{wff}}$.

#### Check of Understanding
Is $A_{1} \land A_{2}$ a wff in the language we've defined? <sup>3</sup>

#### Extending Truth Assignments
We have now defined all the wffs, and similarly to how we gave meaning to the sentence symbols, we'd like to give these wffs meaning as well. As mentioned earlier, we already have some idea of what a wff like $(A_{1} \land A_{2})$ should mean if we know the english interpretations of $A_{1}$ and $A_{2}$. We extend our truth assignment to reflect this

**Definition** Let $S$ be the set of sentence symbols. An *extended truth assignment* is some function
\\[
    \overline{v}: S^{\text{wff}} \to \\{T, F\\}
\\]
which "assigns" each wff a True or False value according to the following rules.

Let $\alpha$ be a wff. Perhaps unsurprising, the value of $\overline{v}(\alpha)$ depends how alpha is constructed in our language.

* If $\alpha = A_{i}$ for some $i \in \mathbb{N}$, then $\overline{v}(\alpha) = v(A_{i})$.
* If $\alpha = (\lnot \beta)$ for some wff $\beta$, then
    * $\overline{v}(\alpha) = T$ if $\overline{v}(\beta) = F$;
    * $\overline{v}(\alpha) = F$ otherwise.
* If $\alpha = (\beta \land \gamma)$ for some wffs $\beta$ and $\gamma$, then
    * $\overline{v}(\alpha) = T$ if $\overline{v}(\beta) = T$ and $\overline{v}(\gamma) = T$;
    * $\overline{v}(\alpha) = F$ otherwise.
* If $\alpha = (\beta \lor \gamma)$ for some wffs $\beta$ and $\gamma$, then
    * $\overline{v}(\alpha) = F$ if $\overline{v}(\beta) = F$ and $\overline{v}(\gamma) = F$;
    * $\overline{v}(\alpha) = T$ otherwise.
* If $\alpha = (\beta \rightarrow \gamma)$ for some wffs $\beta$ and $\gamma$, then
    * $\overline{v}(\alpha) = F$ if $\overline{v}(\beta) = T$ and $\overline{v}(\gamma) = F$;
    * $\overline{v}(\alpha) = T$ otherwise.
* If $\alpha = (\beta \leftrightarrow \gamma)$ for some wffs $\beta$ and $\gamma$, then
    * $\overline{v}(\alpha) = T$ if $\overline{v}(\beta) = \overline{v}(\gamma)$;
    * $\overline{v}(\alpha) = F$ otherwise.

Another quick note about terminology. When we say truth assignment, we are usually referring to the extended truth assignment. It isn't really necessary to differentiate the two in most contexts.

To those readers who have studied basic logic propositional logic, these extensions should not be surprising. In some sense we've actually chosen our symbols and defined wffs and truth assignments to match up with what we expect each wff to mean.

### Fun Exercises and Proofs
I'd recommend attempting the problems first before looking at the solutions. A quick note: considering how we defined the construction of wffs and truth assignment, one might deduce that many proofs related to wffs can be done using mathematical induction, and this is exactly right!

**Exercise 1** (adapted from Enderton)<br>
Consider a situation where a person makes the following claim<br>
"If I am not playing tennis, then I am watching tennis. And if I am not watching tennis, then I am reading about tennis".<br>
Assuming that they can't do multiple activities at the same time, what is the person doing? Try translating this into our formal language and consider the possible truth assignments.

**Solution 1**<br>
Let $A_{1}$ be "I am playing tennis", $A_{2}$ be "I am watching tennis", and $A_{3}$ be "I am reading about tennis".

We can then translate the person's claim to our formal language as
\\[
    (((\lnot A_{1}) \rightarrow A_{2}) \land ((\lnot A_{2}) \rightarrow A_{3})).
\\]

Let $v$ be our truth assignment. We want to find the "configurations" for $v$ such that this wff evaluates to True. Since the person can only be doing one activity at once, $v(A_{i}) = T$ is only possible for one $i \in \\{1, 2, 3\\}$, and the others must evaluate to False. This makes the cases we need to consider very simple, and we find the only one which satisfies our requirements is $v$ such that $v(A_{1}) = F$, $v(A_{2}) = T$, and $v(A_{3}) = F$, so the person must be watching tennis.

**Exercise 2** (adapted from Enderton)<br>
Let $S$ be the set of all sentence symbols, and assume that $v: S \to \\{T, F\\}$ is a truth assignment. Show that there is at most one extension $\overline{v}$ which meets the conditions we previously described.<br>
Hint: Suppose there exist two such extensions $\overline{v_{1}}$ and $\overline{v_{2}}$. Then show that $\overline{v_{1}} = \overline{v_{2}}$ for all wffs in the language using mathematical induction.

**Solution 2**<br>
I won't provide a full solution because I think it's mostly just tedious work but still very informative about what these type of proofs look like,so I will provide an outline of how such an inductive proof would go.

We use induction on the number of connectives in a wff.

*Base step*: If a wff has $0$ connectives, then it is one of our sentence symbols. Since $\overline{v_{1}}$ and $\overline{v_{1}}$ are both extensions of $v$, they must agree.

*Inductive step*: Suppose that $\overline{v_{1}}$ and $\overline{v_{2}}$ agree on all wffs with $< n$ connectives. We want to show that they also agree of all wffs with $n$ connectives. Now we will want to consider all the possible ways that a arbitrary wff $\alpha$ could be constructed. I will only consider the case that $\alpha = (\lnot \beta)$ and show that $\overline{v_{1}}(\alpha) = \overline{v_{2}}(\alpha)$. A rigorous proof would consider all $5$ possible constructions.

Consider if $\alpha = (\lnot \beta)$. Then $\beta$ is a wff with $n - 1$ connectives. Certainly $n - 1 < n$, so by assumption $\overline{v_{1}}(\beta) = \overline{v_{2}}(\beta)$. Now if $\overline{v_{1}}(\beta) = \overline{v_{2}}(\beta) = T$, then by our definition of extending truth assignments, $\overline{v_{1}}(\alpha) = \overline{v_{2}}(\alpha) = F$, and similarly if $\overline{v_{1}}(\beta) = \overline{v_{2}}(\beta) = F$, then $\overline{v_{1}}(\alpha) = \overline{v_{2}}(\alpha) = T$. Thus, $\overline{v_{1}} = \overline{v_{2}}$ in this case.

Note that in this case, we didn't need the hypothesis for all wffs with $< n$ connectives; we could have just assumed for wffs with $n - 1$ connectives. However, for the other $4$ cases, we do actually need the $< n$ hypothesis.

The rest of the proof consists of showing that $\overline{v_{1}} = \overline{v_{2}}$ for wffs with $n$ connectives for the other $4$ constructions as well. Feel free to comment or ask me for clarifications!

### Concluding Remarks
I just want to point out the most of the work done in this post to construct a formal language in propositional logic was for the sake of rigor. None of the results should be particularly surprising (nor confusing) to those readers who have studied basic propositional logic. If anything, I hope the results are able to clarify any confusion readers had previously. There is a bit more I'd like to talk about eventually regarding tautologies and tautological implications (especially since that's where the inductive proofs get more interesting), but I'll leave that for a future post.

In the meantime, I hope everyone enjoyed this post and was able to learn something here. Thanks for reading, and see you next time!

##### Footnotes
<sup>1</sup> if the sky is cloudy then it is raining. the sky is cloudy and it is raining. the sky is not cloudy and it is not raining.

<sup>2</sup> $2^{n}$. nothing.

<sup>3</sup> Kind of annoying, but no. See that the construction one most likely has in mind would result in $(A_{1} \land A_{2})$ with the parentheses. This actually is important. If we had $A_{1} \land A_{2}$ (without parentheses) as a wff, then applying the third construction rule in 2, we would find that $(A_{3} \lor A_{1} \land A_{2})$ is a wff, but this is ambiguous without an order of operation defined.
