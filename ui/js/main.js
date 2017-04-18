var app;
var POLL_INTERVAL = 2000;
function init() {
    console.log('init called');
    app = new Vue({
        el: '#app',
        data: {
            message: 'Hello Vue!',
            cmds: [ { 'command': 'placeholder', 'client_id': '2'} ],
            todos: [
      { text: 'Learn JavaScript' },
      { text: 'Learn Vue' },
      { text: 'Build something awesome' }
    ]
        }
    });
    setTimeout(poll, POLL_INTERVAL);

}

function poll() {
    console.log('poll');
    console.log(app.$http);
    app.$http.get('http://localhost:8081/client/2/list').then(response => {

    // get body data
    console.log('got response')
    cmd = JSON.parse(JSON.parse(response.body));
    if (cmd.length === 0) {
        console.log('empty response, will try again later...');
    }
    else {
        console.log('setting commands');
        app.cmds = cmd;
        app.message = "command: "+cmd[0].command + ", client: "+cmd[0].client_id;
        console.log('commands set, message set');
    }
    setTimeout(poll, POLL_INTERVAL);

  }, response => {
    console.log('error');
    console.log(JSON.stringify(response));
    // error callback
  });

}