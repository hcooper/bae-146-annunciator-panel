import socketio
from simconnect_mobiflight import SimConnectMobiFlight
from mobiflight_variable_requests import MobiFlightVariableRequests
from queue import Queue

q = Queue(maxsize=100)
sm = SimConnectMobiFlight()
vr = MobiFlightVariableRequests(sm, q)
vr.clear_sim_variables()

VARS = {

    # Side block
    "(L:L_ANNUNS_Att_amber_il)",
    "(L:L_ANNUNS_Hdg_amber_il)",
    "(L:L_ANNUNS_Cat2_green_il)",
    "(L:L_ANNUNS_Cat2_amber_il)",
    "(L:L_ANNUNS_WhiteBars_il)",
    "(L:L_ANNUNS_Splr_Y_il)",
    "(L:L_ANNUNS_Splr_G_il)",
    "(L:L_ANNUNS_AirBrk_il)",
    "(L:L_ANNUNS_Gsl_dev_il)",
    "(L:L_ANNUNS_Loc_dev_il)",

    # Main block
    "(L:L_ANNUNS_YD_amber_il)",
    "(L:L_ANNUNS_Ail_amber_il)",
    "(L:L_ANNUNS_AP_il)",
    "(L:L_ANNUNS_Pitch_il)",
    "(L:L_ANNUNS_GSL_white_il)",
    "(L:L_ANNUNS_GSL_green_il)",
    "(L:L_ANNUNS_ALT_white_il)",
    "(L:L_ANNUNS_ALT_green_il)",
    "(L:L_ANNUNS_LOC_white_il)",
    "(L:L_ANNUNS_LOC_green_il)",
    "(L:L_ANNUNS_Vor_white_il)",
    "(L:L_ANNUNS_Vor_green_il)",
    "(L:L_ANNUNS_Rnav_green_il)",
    "(L:L_ANNUNS_BckLoc_white_il)",
    "(L:L_ANNUNS_BckLoc_green_il)",
    "(L:L_ANNUNS_Hdg_green_il)",
    "(L:L_ANNUNS_Mach_il)",
    "(L:L_ANNUNS_IAS_il)",
    "(L:L_ANNUNS_GA_il)",
    "(L:L_ANNUNS_VS_il)",
    "(L:L_ANNUNS_Turb_il)",
    "(L:L_ANNUNS_El_trim_il)",
    "(L:L_ANNUNS_Outer_il)",
    "(L:L_ANNUNS_Nav1_il)",
    "(L:L_ANNUNS_Nav2_il)",
    "(L:L_ANNUNS_Sync_white_il)",
    "(L:L_ANNUNS_Roll_green_il)",
    "(L:L_ANNUNS_Wpt_green_il)",
    "(L:L_ANNUNS_Lnav_green_il)",
    "(L:L_ANNUNS_Airway_il)",
    "(L:L_ANNUNS_Middle_il)",
    "(L:L_ANNUNS_Msg_amber_il)"
}
status={}

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './public/'
})

@sio.event
async def connect(sid, environ):
    sio.start_background_task(task, sid)
    print(sid, 'connected')


@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')

@sio.event
async def force_update(sid):
    print("Replying to forced update request!")
    for k,v in status.items():
        await send_state(k, v, sid)

async def task(sid):
    while True:
        await sio.sleep(0.1)
        while not q.empty():
            event = q.get()
            status[event.name] = event.float_value
            await send_state(event.name, event.float_value, sid)

async def send_state(k, v, sid):
    visibility = 'visible' if v else 'hidden'
    payload = {'element_id': k, 'visibility': visibility}
    print(f"Sending: {payload} to {sid}")
    await sio.emit('update_state', payload, to=sid)

for var in VARS:
    vr.get(var)
