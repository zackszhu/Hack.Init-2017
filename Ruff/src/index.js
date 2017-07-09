$.ready(function (error) {
    if (error) {
        console.log(error);
        return;
    }
    
    $('#led').setRGB([0x80, 0x80, 0x80]);
    $('#led').turnOff();
    $('#led-r').turnOff();

    $('#sound').on('sound', function() {
        console.log('sound detected');
        
        var client = net.connect({port: 8383, host: "192.168.78.113"}, function() {
            console.log("connected to server!");
            client.write("Hello, it's me.");
        });

        client.on('data', function(data) {
            console.log(data.toString());
            client.end();
        });
        client.on('end', function() {
            console.log('disconnected from server');
        });
    });
});

var leds = ["led", "led-r"];

var net = require('net');
var server = net.createServer(function(c) {
    console.log('client connected');
    c.on('end', function(){
        console.log('client disconnected'); 
    });
    c.on('data', function(data){
        var ins = JSON.parse(data.toString());
        console.log(ins);
        if (ins["type"] == "Open") {
            $('#' + leds[ins["number"]]).turnOn();
        } else if (ins["type"] == "Close") {
            $('#' + leds[ins["number"]]).turnOff();
        }
        c.write('Instruct Successfully!\n');        
    });
});

server.listen(8124, function() { //'listening' listener
    console.log('server bound');
});

$.end(function () {
    $('#led-r').turnOff();
});