class: middle center inverted

# Low-Level
---
class: middle center inverted

# Terms and Concepts
---
class: inverted

.left-column[
## Terminology
### 1 / 3
]

.right-column[
## Synchronous
An operation that beings execution to process results before the proceding operation can begin.

**One at a time; Lockstep**

## Asynchronous
An operation that begins on reciept that the preceding operation is finished.

**"Set it and forget it"; Whenever you're ready**

]


---
class: inverted

.left-column[
## Terminology
### 2 / 3
]

.right-column[
## Worker
An application that does work, arbitrary tasks.

## Producer / Consumer
Producer adds tasks to the Queue.

Consumer removes tasks from the Queue.

## Serialization / Coercion
Turning the input parameters and task result into a format the result backend can use; as well as the producers / consumers if they are looking to use the data as well.

]

---
class: inverted

.left-column[
## Terminology
### 3 / 3
]

.right-column[
## (Messaging) Queue
An externally accessible structure managing task flow.

## Broker
An application that manages the Queues.

## (Results) Backend
When tasks finish or fail, their status is stored here.
]

---