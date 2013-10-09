Outline for a Location App
==============

The structure of a location app could be:

* Front end
	* gets your [location information](http://www.w3schools.com/html/html5_geolocation.asp)
	* gets [directional information](http://www.html5rocks.com/en/tutorials/device/orientation/)
	* passes those to the backend using an [ajax POST](http://api.jquery.com/jQuery.post/) call with location
	information as arguments
	* gets the return information from the [ajax call](http://api.jquery.com/jQuery.post/)
	* use [jquery/javascript](http://api.jquery.com/html/) to fill an html `<div>` with the text
	* is sized for [use on mobile](https://developer.mozilla.org/en-US/docs/Mozilla/Mobile/Viewport_meta_tag)
	* has the [browser chrome removed](http://stackoverflow.com/questions/6440386/is-it-possible-hide-ios-browser-chrome-on-a-normal-webpage) when saved to the home screen on an iOS device
* Middleware - on the server
	* [Flask](http://flask.pocoo.org/)/[Django](https://www.djangoproject.com/) server
	* Capture the AJAX call from javascript with the users location information - probably using [tastypie](http://django-tastypie.readthedocs.org/en/latest/cookbook.html) as the API interface (Django)
	* Query the database for previous entries nearby
	* Call other python functions to get natural language responses/find the best path between points
	* return json with the info
* Database - SQL: sqlite or mySQL or postGIS, suggested tables:
	* Note, contains lat,long,description,date,category(food, entertainment etc)
	* User, one to many relation to notes
	* FriendsWith, many-to-many table connecting friends
	
Each of these can be built separately. The first thing to do is create a standalone web-page that just displays the users location. That can be entirely written in html without any middleware or backend.