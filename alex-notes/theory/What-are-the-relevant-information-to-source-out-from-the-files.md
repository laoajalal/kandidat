# What are the relevant information to source out from the files?
Date: 02-02/2021  
Sources:  
Backlink: [index](index)  

----

#### Why map the source code?
- similar files?
- dependencies:
    - source
    - target


#### Basic Architecture
First we have to understand programming architecture a bit better before jumping
into what is the relevant information:
[Basic software architecture](basic-software-architecture-070221-1411.md)

#### Relevant parts in the source code
*Sebastian* believes that the private tagged functions and variables are 
irrelevant in our case. Alternative 2 is to broad, and serves no purpose?
Comments can give relevant context information

- public functions
- public variable/object names
- library names
- package names
- comments

###### Alternative 1
- libraries:
    - key word, *import* "library" ;
- class names
- function names:
    - declaration of functions:
        - key word, *public {void, obj, int, etc.}* "function name"( ){
    - calls to function:
        - new?
- global variables:
    - declaration of functions
    - calls to global variables

###### Alternative 2
Only remove syntax words and characters and rely on the feature selector

#### Info taken from JabRef
I wonder, what is that we want to map out? 
Information taken from JabRef notes:
- Dependencies:
    - Target (depends on named)
    - Source (depended upon from named)
- Responsibility of the file?:
    - Back-end:
        - database
        - programming-logic
    - Front-end:
        - output:
            - graphical
        - input:
            - files
            - text
            - commands
- Modules to look for?:
    - GUI
    - CLI
    - logic
    - globals
    - model
    - pref
    - Allowed dependencies?:
        - gui -> model, logic
        - CLI -> gui, model, logic, globals, pref
        - logic -> model
        - pref -> model, logic
----
