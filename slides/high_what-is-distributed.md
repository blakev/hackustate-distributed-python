class: center middle 

# When to make a distributed application

---

.left-column[
### When?
]

.right-column[
### Functions that fit!
- Many operations that can be done at once
- A single operation called many times
- Operations that benefit `chaining`

### Scenarios
- Big-data
- Scale our applications horizontally
- Scale our applications geographically
]

---

.left-column[
### When?
### When not?
]

.right-column[
### Late Adoption
- One big operation without granularity
- Network that can't handle the bandwidth 
- Unjustifiable load

### Complexity Complexity <sup>Complexity <sup>Complexity <sup>Complexity <sup>...</sup></sup></sup></sup>
- Code complexity
- Network complexity
- Orchestration complexity
- Synchronization complexity
- Business complexity
- etc.
]

---