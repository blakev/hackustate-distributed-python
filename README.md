# hackustate-distributed-python
Workshop materials for HackUState Hackathon.

```bash
# grab the current project and cd into its folder
git clone git@github.com:blakev/hackustate-distributed-python.git
cd hackustate-distributed-python

# install the jinja2 runtime to the current python environment
pip install jinja2-cli lesscpy

# compile the style assets
lesscpy static/core.less > static/core.css

# tell jinja to build the presentation
jinja2 presentation.jinja info.json --format=json > ./presentation.html

# tell jinja to generate the presentation as a report
jinja2 presentation.jinja info.json --format=json -D flatpaper=True > ./paper.html

# open the presentation in the default browser window
sensible-browser ./presentation.html &
```

### Dependencies
  - [Python](https://python.org)
  - [less](http://lesscss.org) CSS pre-processor.
  - [lesscpy](https://github.com/lesscpy/lesscpy) less compiler written in Python.
  - [Remark](https://github.com/gnab/remark) HTML slideshow.
  - [Jinja2-cli](https://github.com/mattrobenolt/jinja2-cli) Templating library interface.