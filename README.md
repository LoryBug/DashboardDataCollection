# DashboardDataCollection
An interactive dashboard using Dash library, from Plotly, to visualize data collected from a firewall 

### Project structure:
 - **login_page** : ????
 - **page_overview** : display the initial dashboard with live data like cpu usage, throughput, free memory and health score
 - **page_runScript** : you can run all the script or just the selected one, visualizing the collected data in a table (you can filter by script name) and a downloadable check report (filter by checkResult)
 
### Repository structure:
 - *assets*: directory with assets, and css file
 - *data*: directory all the json file and md file produced by the script
 - *app.py*: define the app variable needed by Flask
 - *index.py*: like a navigator file, manage the URLs from the different pages
 - *layout.py*: page html layout, and function with reusable components
 - *callbacks.py*: all the function that define the user interaction with the page
