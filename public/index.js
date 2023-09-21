const sio = io();

sio.on('connect', () => {
  console.log('connected');
  sio.emit('force_update');
});

  // Listen for all incoming events
  sio.onAny((event, ...args) => {
    console.log(sio.id, 'Received event:', event, args[0]);
  });

sio.on('update_state', (data) => {
  console.log("Got update:", data);
  e = document.getElementById(data.element_id).style.visibility = data.visibility;
});