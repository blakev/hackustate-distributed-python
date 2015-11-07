class: inverted center middle

# The Implementation

---

class: inverted

# Install Celery

```bash
pip install celery[redis]
```

--

# Make sure it worked

```bash
$: celery --version
3.1.19 (Cipater)
```

---
class: inverted

# The Basics

{{ code_block('python', './code/tasks.py')}}

---
class: inverted

# Starting the Worker

**Command**
```bash
$ celery -A tasks worker --loglevel=info &
```

**Output**
```bash
 -------------- celery@blake-laptop v3.1.19 (Cipater)
---- **** ----- 
--- * ***  * -- Linux-4.2.0-16-generic-x86_64-with-Ubuntu-15.10-wily
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x7f2c3f754f60
- ** ---------- .> transport:   redis://localhost:6379//
- ** ---------- .> results:     disabled
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- 
--- ***** ----- [queues]
 -------------- .> celery           exchange=celery(direct) key=celery
```
---
class: inverted

# Let's test it out!

```python
Python 3.5.0+ (default, Oct 11 2015, 09:05:38) 
[GCC 5.2.1 20151010] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from tasks import add
>>> add(2, 2)
4
```
--

```python
>>> add.delay(2, 2)
<AsyncResult: 4baaa9a0-a517-45a7-b9b3-3ca4737255c6>
```
--

```python
>>> result = add.delay(2, 2)
>>> result.failed()
False
>>> result.successful()
True
>>> result.status
'SUCCESS'
```

--

### Neat.. :)

---

class: inverted

### A task to pull a website!

{{ code_block('python', './code/tasks_1.py') }}
--

### A task to get string length?

{{ code_block('python', './code/tasks_1-a.py') }}

---

class: inverted

### And, a task to do async addition...

{{ code_block('python', './code/tasks_1-b.py') }}

---

class: inverted middle center

# So what can we do?

---

class: inverted

.left-column[
### Fetch
]

.right-column[
# Run a single task..

```python
>>> job = core.random_site.delay()
>>> results = job.get()
...
>>> print(len(results))
100342
>>> job.status
'SUCCESS'
```
]
--

.right-column[
# Run a single task into another..

```python
>>> job = (core.random_site.s() | core.page_size.s())
>>> job
core.random_site() | core.page_size()
>>> result = job.apply_async()
>>> result.get()
121192
```
]

---
class: inverted

# Experiment

## Static run...

```python
>>> [len(core.random_site()) for x in range(10)]
```
--

## Distributed run...

```python
>>> job = group([chain(core.random_site.s() | core.page_size.s()) for x in range(10)])
>>> results = job.apply_async()
>>> results.get()
```

---
class: inverted

## Distributed run..**With Callback!**

**Expanded**
```python
chord(
	[
	chain(
		core.random_site.s() | 
		core.page_size.s()
	) for x in range(10)
	]
	)(core.xsum.s()).get()
```
--

**One-liner**
```python
>>> chord([chain(core.random_site.s() | core.page_size.s()) for x in range(10)])(core.xsum.s()).get()
```

---

