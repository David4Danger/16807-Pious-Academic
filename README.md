<h2>16807 Pious Academic, A Python Wrapper For H5</h2>
<h3>Current Version: 1.2 </h3>

<h3>Version History </h3>
<p><b>Future releases:</b> Additional tests to verify integrity, work on profile requests, working BTBnet example</p>
<p><b>Version 1.2:</b> Added getmeta.py and a copy of my current local metadata JSON files. Just run getmeta.py and it will automatically create an up-to-date local copy of all the available meta data for you. <b>NOTE:</b> I provided a copy of all my current JSON files for you to save to make the process easier. You will still need to <b>change the paths</b> used to open and write into all the JSON files in the getmeta file.
<p><b>Version 1.1:</b> Added testfile.py that gives a demo on how to use all of the request functions, and has some more in-depth explanations about various nuances in the API. Also repaired a few bugs in the parameters used in functions with optional parameters. Much more stable and usable than 1.0.</p>
<p><b>Version 1.0:</b> Cleaned up a few pieces of the code and added some documentation.</p>
<p><b>Version 0.2:</b> Fixed most of the major bugs and issues, added the rate limit and error classes to have a more operational program. Updated rate limits to support 343's new 1 request per second rate.</p>
<p><b>Version 0.1:</b> First skeleton release, full of bugs and other fun stuff.</p>
<br>

<h3>Installing Pious Academic </h3>
<p><a href="https://developer.haloapi.com/developer">Go here and sign into your microsoft account</a>, then go to your profile. You should have an API key ready for you to use. Get it, save it, and for the love of god don't let anyone other than yourself see it.</p>
<p>The other prerequisite is to have the request module installed for Python. Run this in your terminal to install the module:  
<br>
<br>
    $ pip install requests
<br>
<br>
You can find the documentation for requests <a href="http://docs.python-requests.org/en/latest/">here</a>, but it isn't important if you're just using the wrapper, only if you want to <i>understand</i> how it works.
</p>
<br>
<h3>Using Pious Academic </h3>
<p>Using the module is fairly simple. Create your entry point main file and import the PiousAcademic class.</p>
  from PiousAcademic16807 import PiousAcademic
<p>Then you'll need to define the PiousAcademic class as a variable</p>
  api = PiousAcademic()
<p>Now you're free to manipulate any of the functions in the API as you see fit. Simply include whatever parameters you are required to include and any optional parameters you want to use.</p>
  

<h3>Addendum </h3>
<p>This wrapper was made for my use with www.bigteambattle.net, a website leaderboards and more. I'll keep everyone updated on when my project is complete if I can make it public for an example of utilising the wrapper. Feel free to contact me here or at my personal website, www.davidskudra.ca, for any questions regarding this library or my work.</p>
