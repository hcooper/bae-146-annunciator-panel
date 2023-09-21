    updateStatus('', 'green');
    updateStatus('DISCONNECTED', 'red');

  // Listen for all incoming events
  sio.onAny((event, ...args) => {
    console.log(sio.id, 'Received event:', event, args[0]);
  });

  function updateStatus(msg, clr) {
    div = document.getElementById('status');
    div.innerHTML=msg;
    div.style.color=clr;
  }
