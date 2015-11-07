class: middle center

# High-Level

---

# Distributed vs. Not Distributed

### What a distributed application is not:
- An application installed on the same machine more than once.
- The same application on many user's devices acting independently.
- A webserver serving HTML pages.

### What is a distributed application?
#### An application that.. 
- communicates with similar apps with similar purpose.
- runs in sync with another in a different runtime.
- that demonstrates resiliency when nodes go missing.
- runs in multiple locations looking for results locally.

---
.left-column[
# Examples
]

.right-column[
### Not Distributed
- Usenet
- Snapchat
- Web site frontend
- Dropbox

### Distributed
- Bittorrent
- Bitcoin
- Web site backend (reverse proxy, stateless)
- Folding@Home
- WebRTC

### Both?
- Databases (MySQL, SQLServer, Redis, etc)
- Games
]

---
