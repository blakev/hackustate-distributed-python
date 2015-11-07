class: center middle inverted

# High level pseudo implementation

---

class: inverted middle center

# What's the plan?

{{ code_block('bash', 'code/pseudo_1.py') }}

???

Keep in simple

Using *Celery* Python distributed 

---

class: inverted

.left-column[
## Psuedo
### Pick a Broker
]

.right-column[
## Choices:

![Celery Brokers](./static/img/broker_table.png)

- Experience matches expectations.
- Something you've used before.
- Easy to maintain.
- Simple.

]

---
class: inverted

.left-column[
## Psuedo
### Pick a Broker
### Pick a Backend
]

.right-column[
## Choices:

![Celery Backends](./static/img/backend_table.png)

- Does it make sense for your results?
- Something you've used before.
- Simple.
]

---
class: inverted center middle

# Backend and Broker?
--

## .vivint[Redis]!

---
class: inverted

# Start the broker and backend?

```bash
# grab the things we need
sudo apt-get install redis-server redis-tools

# start up the server
sudo service redis-server start

# check it's working correctly
redis-cli --stat
```
--

### Hopefully it "just worked," it's the easiest to go with :/

---
class: inverted center middle

# What's the problem?

---
