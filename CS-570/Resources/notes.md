## ADTs

Abstract Data Type (ADT):
- ADT: data and methods. data structures. 
  - facilitate storage, organization, and processing information
- User does not need to know about implementation or storage of the ADT and only interacts with public methods

Interface:

- specifies or describes an ADT to the application programmer
  - The methods and the actions that they must perform
  - what arguments, if any, must be passed to each method
  - what result the method will return
- constants are defined in the interface, variables turn into constants
- methods are abstracts
- The interface can be viewed as a contract which guarantees how the ADT will function
- A class can implement zero to multiple interfaces

Abstract Classes:

- Cannot be instantiated (represented by an instance)
- Abstract class may declare abstract methods
- A concrete class that is a subclass of an abstract class must provide an implementation of each abstract method 

## Exception Handling

Checked Exceptions:

- normally not due to programming error 
- generally beyond the control of the programmer
- all input/output

Unchecked Exceptiosn:

- programming error

## Data Structure

Data Structure: a way to store and organize data in order to faciliate access and modification

- No single data structure optimal for all purposes
- Usually optimized for a specific problem setting
- Important to know the strength and limitations of several of them. 
- Examples: 
    - Trees (binary search trees, red-black trees, b-trees, ...)
    - Stacks (last in, first out), queues (first in, first out), priority queues

Algorithms: well defined computational procedure
- Takes value or set of values as input
- produces value or set of values as output
- tool for solving a well-specified computational problem

Efficiency: computing time and memory are bounded resources
- different algorithms that solve the same problem often differ

Asymptotic performance: how does the algorithm behave as the problem size gets larger (running time, memory/storage requirements, bandwidth/power requirements).
- Asymptotoic Notation

