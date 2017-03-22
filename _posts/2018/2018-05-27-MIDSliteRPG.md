---
layout: post
title: "MIDS(lite) RPG"
date: 2018-05-27 11:44:29
author: "Fabien O'Carroll"
link: "github.com/allouis"
categories: 2018 rpg
---
```
## Core Stats

  M - Moxie.
  I - Intelligence.
  D - Dexterity.
  S - Strength.

### Additional Stats

  Health = 10 + M
  Defence = D + Armour
  *Fighting = S
  *Ranged = D
  *Sneak = D
  *Smoothtalking = M
  *History = I
  etc...

*has a training level

### Training levels

  meh:    -1
  okay:    0
  good:   +1
  great:  +2
  expert: +3

  Example:
    Moxie score is 2.
    Smoothtalking training level is "meh".
    Smoothtalking skill = 1

## Stat checks

Situation has a difficulty between -2&2 (set by gm)

Roll 3 + X dice, X is your skill number without minus signs.

If skill level is negative, count three lowest die
Otherwise, count three highest die

If you beat 10 + difficulty, you succeed!
If not, you gain 1/10 of a training level! (keep track) (only once per situation, e.g. no repeated lockpicking)

### Combat

Armour is between -1&3, 2-3 is rare

The difficulty for attacking a creature is it's defence stat
The damage is between 1&3

## Character

Pick a name!
Your MIDS is 0:0:0:0
3 points to spend, can buy/sell. (max 2, min -1)

You have 10 items.

You have 10 trainable stats. (make some up!)
You're "good" at 1, "okay" at 2, and "meh" at the rest

find a DM!
```
## Author Comments 

I've been working on a game system for a while, and this is the core of it stripped down to 200 words.

The dice system is designed to reward more skilled characters, as you get better at a skill, it becomes easier to succeed with harder challenges, but also way more likely to succeed with easier ones. Whereas an unskilled character is almost guaranteed to fail on the more difficult (+1, +2) checks. This may have a side affect of keeping players focused, and not stepping on each others toes. (the barbarian picking the lock e.g.)

The levelling system is designed to take the pain out of failure, and also as a simple and automatic mechanism for character advancement. Note that as you level, you fail a lot less, so although this looks linear, it gets progressively harder.

In the fuller version, I have "modules" for magic, classes and species :)
 
