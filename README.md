# Explore-US-Bikeshare-Data (Udacity)
Overview
In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

<img alt="" src="https://video.udacity-data.com/topher/2018/March/5aa7718d_divvy/divvy.jpg" class="chakra-image css-utgf8e">

<div class="css-pr2tx6"><div class="css-1m96lhp"><div class="css-u8svcc"><div><div class="_15vzQlp3FJ8f94suLiPCPf ureact-markdown "><h2 id="bike-share-data">Bike Share Data</h2>
<p>Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.</p>
<p>Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.</p>
<p>In this project, you will use data provided by <a target="_blank" href="https://www.motivateco.com/">Motivate</a>, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.</p>
<h2 id="the-datasets">The Datasets</h2>
<p>Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core <strong>six (6)</strong> columns:</p>
<ul>
<li>Start Time (e.g., 2017-01-01 00:07:57)</li>
<li>End Time (e.g., 2017-01-01 00:20:53)</li>
<li>Trip Duration (in seconds - e.g., 776)</li>
<li>Start Station (e.g., Broadway &amp; Barry Ave)</li>
<li>End Station (e.g., Sedgwick St &amp; North Ave)</li>
<li>User Type (Subscriber or Customer)</li>
</ul>
<p>The Chicago and New York City files also have the following two columns:</p>
<ul>
<li>Gender</li>
<li>Birth Year</li>
</ul>
</div></div></div></div><div class="css-1m96lhp"><div class="css-u8svcc"><section><div class="css-1l4w6pd"><img alt="" src="https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png" class="chakra-image css-3x5pxo"></div><div class="css-1mnskd6"><div class="_15vzQlp3FJ8f94suLiPCPf ureact-markdown "><p><em>Data for the first 10 rides in the <strong>new_york_city.csv</strong> file</em></p>
</div></div></section></div></div><div class="css-1m96lhp"><div class="css-u8svcc"><div><div class="_15vzQlp3FJ8f94suLiPCPf ureact-markdown "><p>The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them (<a href="https://www.divvybikes.com/system-data" target="_blank">Chicago</a>, <a href="https://www.citibikenyc.com/system-data" target="_blank">New York City</a>, <a href="https://www.capitalbikeshare.com/system-data" target="_blank">Washington</a>). These files had more columns and they differed in format in many cases. Some <a href="https://en.wikipedia.org/wiki/Data_wrangling" target="_blank">data wrangling</a> has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward.</p>
<h2 id="statistics-computed">Statistics Computed</h2>
<p>You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:</p>
<p><strong>#1 Popular times of travel</strong> (i.e., occurs most often in the start time) </p>
<ul>
<li>most common month</li>
<li>most common day of week</li>
<li>most common hour of day</li>
</ul>
<p><strong>#2 Popular stations and trip</strong></p>
<ul>
<li>most common start station</li>
<li>most common end station</li>
<li>most common trip from start to end (i.e., most frequent combination of start station and end station)</li>
</ul>
<p><strong>#3 Trip duration</strong></p>
<ul>
<li>total travel time</li>
<li>average travel time</li>
</ul>
<p><strong>#4 User info</strong></p>
<ul>
<li>counts of each user type</li>
<li>counts of each gender (only available for NYC and Chicago)</li>
<li>earliest, most recent, most common year of birth (only available for NYC and Chicago)</li>
</ul>
<h2 id="the-files">The Files</h2>
<p>To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided in a <strong>bikeshare.py</strong> file, and you will do your scripting in there also. You will need the three city dataset files too: </p>
<ul>
<li><strong>chicago.csv</strong></li>
<li><strong>new_york_city.csv</strong></li>
<li><strong>washington.csv</strong></li>
</ul>
<p>All four of these files are zipped up in the <strong>"all_project_files"</strong> document in the Resources tab in the sidebar on the left side of this page. (You may need to scroll down inside the Resources tab to see the "all_project_files" doc.) You can choose to download and unzip that "all_project_files" doc to access all four project files, and do your project work on your local machine. </p>
<p>If you'd prefer, the later Project Workspace page in the classroom here also has the bikeshare.py file and all the city dataset files included in it, and you can do all your work on the project with them there. If you choose this option, you don't need to download the files from the Resources tab.</p>
</div></div></div></div></div>
