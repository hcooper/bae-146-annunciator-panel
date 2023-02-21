const sio = io();

sio.on('connect', () => {
  console.log('connected');
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('update', (data) => {
  console.log("Got update:", data);
  e = document.getElementById(data.element_id).style.visibility = data.visibility;
});