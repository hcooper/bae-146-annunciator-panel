const sio = io();

sio.on('connect', () => {
  console.log('connected');
  sio.emit('force_update');
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('update_state', (data) => {
  console.log("Got update:", data);
  e = document.getElementById(data.element_id).style.visibility = data.visibility;
});