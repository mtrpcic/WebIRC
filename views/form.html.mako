<%inherit file="application.html.mako"/>

<%def name="head()">
  <script type="text/javascript" src="/scripts/form.js"></script>
  <link rel="stylesheet" type="text/css" href="/styles/form.css" />
</%def>

<%def name="body()">
  <div id="header">
  WebIRC
  </div>
  <div id="form">
    <form id='irc_options' name='irc_options' action='/irc' method='POST'>
      <p>
        <label for='server'>Server</label>
        <input type='text' name='server' id='server' />
      </p>
      
      <p>
        <label for='port'>Port</label>
        <input type='text' name='port' id='port' />
      </p>
      
      <p>
        <label for='nickname'>Nickname</label>
        <input type='text' name='nickname' id='nickname' />
      </p>
      
      <p>
        <label for='channel'>Channel</label>
        <input type='text' name='channel' id='channel' />
      </p>
      
      <p>
        <input type='submit' name='submit' value='Go!!' class='submit' />
      </p>
    </form>
  </div>
</%def>
