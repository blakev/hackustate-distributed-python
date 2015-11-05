# hackustate-distributed-python
Workshop materials for HackUState Hackathon.

```bash
# grab the current project and cd into its folder
git clone git@github.com:blakev/hackustate-distributed-python.git
cd hackustate-distributed-python

# install the jinja2 runtime to the current python environment
pip install jinja2-cli

# tell jinja to build the presentation
jinja2 presentation.jinja info.json --format=json > ./presentation.html

# tell jinja to generate the presentation as a report
jinja2 presentation.jinja info.json --format=json -D flatpaper=True > ./paper.html

# open the presentation in the default browser window
sensible-browser ./presentation.html &
```