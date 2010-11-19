# WebIRC #
WebIRC is a Twisted based Web Server/IRC Client that allows you to communicate on IRC from your browser
without the need for a Java Applet or Flash components.  It makes use of the HTML5 WebSocket technology

# Running WebIRC #
To run WebIRC, you'll need the following packages:

* Python 2.6.x
* Twisted v8.2.0+
* [Mako](http://www.makotemplates.org/)
* [txwebsockets](https://github.com/gleicon/txwebsockets)

Once all packages are installed, simply go into the root of the project and type the following into your terminal:

    python run.py

Then visit `localhost:8080` in your browser.

# Known Limitations #
* Bad form data on the home page will crash the server, as it is not validated
* Incoming messages from the IRC server are not properly escaped, so HTML/Javascript injection is possible
* Sometimes there is a race condition that causes the IRC connection to happen **before** the WebSocket is fully connected, and no data will show up in the browser chat window

# To Do #
* Sanitize incoming messages for HTML tags to stop javascript injection
* Add some form validation
* Add support for web-based actions (/nick, /action, /me)
* Add support for multiple channels


# Disclaimer #
This code is still under development, and as such, minor revisions may drastically change functionality.
Please keep this in mind when using WebIRC.
# Copyright and Licensing #
Copyright (c) 2010 Mike Trpcic, released under the MIT license
