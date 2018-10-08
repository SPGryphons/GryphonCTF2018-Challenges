#!/usr/bin/env node

const HOST = '0.0.0.0';
const PORT = 5000;

const net = require('net');
const server = net.createServer().listen(PORT, HOST);

const fs = require('fs');
let banner;
fs.readFile('banner.txt', {encoding: 'utf-8'}, function(err,data){
    if (!err) {
        banner = data;
    } else {
        console.log(err);
    }
});
const exec = require('child_process').exec;

server.on('connection', sock => {
    sock.setEncoding('utf8');
    sock.write(banner);
    sock.on('data', data => {
        let recieved = data.toString('utf8').replace(/\r?\n$/, '');
        if (recieved === 'exit') {
            sock.destroy();
        } else {
            exec('/bin/bash -rc \'cowsay ' + recieved + '\'', (error, stdout, stderr) => {
                sock.write(stdout + '\n> ');
            });
        }
    });
});

console.log('Server listening on ' + HOST + ':' + PORT);
