---
layout: post
title: "Turing Story Machine"
date: 2017-04-23 18:54:02
author: "Michael Such"
link: "https://twitter.com/shadeinshades"
categories: 2017 rpg
---
```
**DESCRIPTION**

An abstract machine for generating stories.

**COMPONENTS**

A TAPE made of one or more CELLs (4-10 suggested), stores the fiction.

Each CELL (= index card), stores (=write down) a single story ELEMENT (character, location, etc). 

STATE (= token) is the current focus of the story. Can be set equal to (=place on) the ELEMENT in any CELL or BLANK, which is the empty ELEMENT.

HEAD (= token) is the narrator, always (placed) on a CELL, can perform the following OPERATIONS on that CELL: 

WRITE; change the CELL ELEMENT based on the STATE, narrate this transformation, set the STATE to BLANK. Writing to a BLANK CELL introduces a new ELEMENT to the story in that CELL. If the STATE is BLANK this is arbitrary. If you write a BLANK STATE to a CELL with a ELEMENT which is not BLANK, narrate an epilogue for this ELEMENT, set the CELL to BLANK.

READ; set the STATE to the CELL ELEMENT; narrate details about this ELEMENT.

MOVE; the HEAD to a new CELL, narrate thoughts, emotions or change in story direction.

**PROCEDURE**

Perform OPERATIONS with the HEAD. The TAPE and STATE begin BLANK. START with a WRITE. STOP when the TAPE is all BLANK again.
```
## Author Comments 

This isn’t actually a Turing machine, but it is inspired by the concept and by word/sentence at a time story games.

Thanks to the members of London Indie RPG Meetup, at which an earlier iteration of this was tested. 
