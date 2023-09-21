window.onload = function () {

  const sio = io();
  updateStatus('DISCONNECTED');
  sio.on('connect', () => {
    console.log('connected as', sio.id);
    sio.emit('force_update');
    updateStatus('', 'green');
  });

  sio.on('disconnect', () => {
    console.log('disconnected');
    forceState('hidden');
    updateStatus('DISCONNECTED', 'red');
  });

  // Listen for all incoming events
  sio.onAny((event, ...args) => {
    console.log(sio.id, 'Received event:', event, args[0]);
  });

  sio.on('update_state', (data) => {
    e = document.getElementById(data.element_id).style.visibility = data.visibility;
  });


  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('forceon')) {
    forceState('visible');
  }

  function forceState(state) {
    const spans = document.querySelectorAll(".wrap span");
    spans.forEach(span => {
      span.style.visibility = state;
    });
  }

  function updateStatus(msg, clr) {
    div = document.getElementById('status');
    div.innerHTML=msg;
    div.style.color=clr;
  }

};