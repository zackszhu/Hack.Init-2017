const Leap = require("leapjs");
const http = require('http');
const net = require("net");

function equals(a, b) {
    var a0 = a[0], a1 = a[1], a2 = a[2];
    var b0 = b[0], b1 = b[1], b2 = b[2];
    return (Math.abs(a0 - b0) <= Math.max(1.0, Math.abs(a0), Math.abs(b0)) && Math.abs(a1 - b1) <= Math.max(1.0, Math.abs(a1), Math.abs(b1)) && Math.abs(a2 - b2) <= Math.max(1.0, Math.abs(a2), Math.abs(b2)));
};

function getDirections(username, fn) {
    console.log("get");
    return http.get({
        host: '192.168.78.145',
        port: 8000,
        path: '/get_furniture?username='+username
    }, function(response) {
        console.log("res");
        // Continuously update stream with data
        var body = '';
        response.on('data', function (d) { body += d; });
        response.on('end', function() {
            console.log("end");
            // Data reception is done, do whatever with it!
            var parsed = JSON.parse(body);
            fn(parsed);
        });
    });
};


const server = net.createServer((socket)=>{
  console.log("Client connected.");

  socket.on('data', ()=>{
    console.log("Data in\n");
    // socket.write("Hello");
    // const buf = new Buffer.from(JSON.stringify(currFrame));
    const hands = currFrame.hands;
    if (hands.length <= 0) {
      return;
    }
    else {
      const finger = currFrame.hands[0].indexFinger.direction;
      console.log(finger);
      try {
        getDirections('zcj', function(json) {
          const vec = Leap.vec3.create();
          for (var index = 0; index < json.directions.length; index++) {
            var element = json.directions[index];
            vec[0] = element[0];
            vec[1] = element[1];
            vec[2] = element[2];
            console.log(element);
            if (equals(vec, finger)) {
              const client = new net.Socket();
              const sendCommand = function (command, num) {
                  client.connect(8124, '192.168.78.1', function () {
                      console.log('Connected to RUFF');
                      client.write(JSON.stringify({
                          "type": command,
                          "number": num
                      }));
                      client.destroy();
                  });

                  client.on('close', function() {
                      // console.log('Connection closed');
                  });
              }
              sendCommand('Open', index);
            }
          }
        })
      }
      catch(e) {

      }
    }
  });
})

server.listen(8383, ()=>{
  console.log("Server started.");
});


const controllerOptions = {};
let currFrame = {};
let prevFinger = Leap.vec3.create();
let currFinger = Leap.vec3.create();

Leap.loop(controllerOptions, (frame) => {
  currFrame = frame;
  prevFinger = Leap.vec3.clone(currFinger);
  if (currFrame.hands.length > 0) {
    currFinger = currFrame.hands[0].indexFinger.direction;
  }
  else {
    currFinger = Leap.vec3.create();
  }
})