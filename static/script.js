console.log('hjiii')

const ws = new WebSocket(`ws://${window.location.host}/ws`);

ws.onmessage = function(event) {
    data = event.data;
    console.log("client code got data", data);

    const queryString = window.location.search;
    console.log('queryString', queryString);

    const urlParams = new URLSearchParams(queryString);
    console.log('urlparams', urlParams.get('hi'));
    ws.send("i am a client these are my params" + JSON.stringify(urlParams))


};

