
Sebastian will be the Supervisor and provider:
    - will cause less friction
__Questions for the 1st meeting:__
1. What is the motivation behind this work?
2. What work will we be doing?
3. What is the goals of this theisis?
4. Will you be our supervisor? Sebastian
5. How available will that person be?:
    - Gonna have 1 meeting once a week
    - Will be available through email and if neccessary zoom.
6. What is the prefered way of communication?
7. Do we need access to any special equipment/tools?  
   - have training data for testing
8. Any specific work or litterature that you recomend we start with?

Topic:
- Software architecture 
- reaserch and develop a machine learning technique:
    - if machine learning can be applied to source code processing
    - which MLP techniques that works well with this
Sometimes you want to structure your source code into larger units than 
source code files, e.g. "want to say this part of the system is interface
code, this is database code, how the dependencies in this course grained units
shouldent access eachother."

- There are tools that can do these checks, whether the source code conforms  
  to the architecture:
    - there is a need to map the source code manually:
        - larger projekts makes this work teadious and boring:
            - sometimes it is scattered
        - it isn't always appearant
        - there is processes that tries to automate this 
          
    - want to explore the ability to use machine learning to do this task:
        - text processing machine learning techniques
            - apply these techniques to source code:
                - to interpretate the source code
                - look at a example of a source code with a kategory

- classification techique
- how to preprocess the source code / how to extract which kind of information  
  in the source code
  
  - then the machine understands the example, then use this to find similar  
    source code

- uppstartsmöte:
    - skapa ett schema
- Split up the work, sugestion:
    - preprocessing
    - classifier

#### Motivation & Background
With larger programming projects the need arises for structuring the source code into larger units than source code files, e.g. we want to classify a certain part of the system as user interface code, and another is database code. 
These two parts have certain dependencies where they shouldn't access each other.
There are tools that can do these checks, whether the code conforms to the architecture of the system. 
To utilize these tools there is a need to manually map out the source code. 
This mapping isn't always apparent and sometimes the files are scattered throughout the system.  
With larger projects this work becomes the tedious and tiresome, and thus arises the need to automate this process. 

