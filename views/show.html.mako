<%inherit file="application.html.mako"/>

<%def name="head()">
  <script type="text/javascript">
      var NICKNAME = "${nickname}";
  </script>
  <script type="text/javascript" src="/scripts/json2.js"></script>
  <script type="text/javascript" src="/scripts/irc.js"></script>
  <link rel="stylesheet" type="text/css" href="/styles/irc.css" />
</%def>

<%def name="body()">
  <div id="container">
    <div id="header">
      ${channel} on ${server}
    </div>
    <div id="chat_window"></div>
    <div id="action_console">
      <form id='send_message'>
        <input type='text' id='to_send' />
        <input type='submit' id='send_button' value='send' />
      </form>
    </div>
  </div>
</%def>
