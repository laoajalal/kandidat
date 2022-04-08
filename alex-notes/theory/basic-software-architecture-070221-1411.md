# Basic software architecture
Date: 07-02/2021  
Sources:  
Backlink: [What-are-the-relevant-information-to-source-out-from-the-files](What-are-the-relevant-information-to-source-out-from-the-files.md)  

---
#### Scope
When looking to describe the architecture of software one have to keep in mind
the scope of the description, e.g.:
- __Macroscopic system structure__, a higher-level abstraction of the software  
  system that consists of a collection computational components with connectors 
  that describes the interactions.
- __Targeted subsystem__, a selection of computational components and their  
  connectors.

Components can have 3 activities:
- Action
- Input
- Output
Connectors, 2 types:
- Destination
- Source

#### Modeling views
There is different ways to view a system's model, e.g. UML diagrams can represent 
two different views of a system model:
- __Static__ (or structural) view, emphasizes the static structure of the system  
  using objects, operations, attributes and relationships:
  - class diagrams
  - composite structure diagrams
- __Dynamic__ (or behavioral) view, emphasizes the dynamic behavior of the system  
  by detailing the collaborations among objects and changes to internal states
  of the objects:
  - sequence diagrams
  - activity diagrams
  - state machine diagrams
  - interaction diagrams

#### Java
Given the project we will work on is gonna be exclusively in java, we will
go further upon java-architecture-design .

----
