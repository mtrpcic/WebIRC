  var message_contexts = {
      'message': function(data){
          populateChat("&lt;" + data.nickname + "&gt; " + data.message + "<br />");
      },
      'action' : function(data){
          populateChat("* " + data.nickname + " " + data.message + "<br />");
      },
      'join'   : function(data){
          $("#names_window").append("<span class='name' id='user_" + data.nickname + "'>" + data.nickname + "</span>");
          populateChat("* Joins: " + data.nickname + "<br />");
      },
      'part'   : function(data){
          $("#user_" + data.nickname).remove();
          populateChat("* Parts: " + data.nickname + "<br />");
      },
      'rename' : function(data){
          $("#user_" + data.old_nickname).html(data.new_nickname);
          $("#user_" + data.old_nickname).attr('id', "user_" + data.new_nickname);
          populateChat("* " + data.old_nickname + " is now known as " + data.new_nickname + "<br />");
      },
      'quit'   : function(data){
          $("#user_" + data.nickname).remove();
          populateChat("* Quits: " + data.nickname + " (" + data.message + ")<br />");
      },
      'names'  : function(data){
          console.log(data.names);
          for(var i = 0; i < data.names.length; i++){
              $("#names_window").append("<span class='name' id='user_" + data.names[i] + "'>" + data.names[i] + "</span>");
          }
          //populate the names here
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
            message_contexts[data.type](data);
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
        message_contexts['message']({nickname: NICKNAME, message: message})
        return false;
    });
});
