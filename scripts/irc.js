  var chat_contexts = {
      'message': function(data){
          return "&lt;" + data.nickname + "&gt; " + data.message + "<br />";
      },
      'action' : function(data){
          return "* " + data.nickname + " " + data.message + "<br />";
      },
      'join'   : function(data){
          return "* Joins: " + data.nickname + "<br />";
      },
      'part'   : function(data){
          return "* Parts: " + data.nickname + "<br />";
      },
      'rename' : function(data){
          return "* " + data.old_nickname + " is now known as " + data.new_nickname + "<br />";
      },
      'quit'   : function(data){
          return "* Quits: " + data.nickname + " (" + data.message + ")<br />";
      }
  };
  
  function populateChat(msg){
      $("#chat_window").append(msg);
      
      // Move the chat window scrollbar to the bottom.
      $("#chat_window").attr({ scrollTop: $("#chat_window").attr("scrollHeight") });
  }
  
  $(document).ready(function(){
      var ws;
      if ("WebSocket" in window) {
        ws = new WebSocket("ws://localhost:8888");
        ws.onopen = function() {
            console.log("connected to the server");
        };

        ws.onmessage = function (evt) {
            var data = JSON.parse(evt.data);
            populateChat(chat_contexts[data.type](data));
        };
        
        ws.onerror = function(e) {
          console.log(e);
        }
        
        ws.onclose = function() {};
    } else {
         alert("You have no web sockets.");
    };
    
    $("#send_message").submit(function(){
        var message = $("#to_send").val();
        $("#to_send").val("")
        var data = {
            message: message,
            token: 'abc'
        }
        ws.send(JSON.stringify(data));
        populateChat(chat_contexts['message']({nickname: NICKNAME, message: message}))
//        populateChat("&lt;" + NICKNAME + "&gt; " + message + "<br>");
        return false;
    });
});
