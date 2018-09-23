const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const cookieParser = require('cookie-parser');
const randomstring = require("randomstring");

// add cookieParser to middleware stack
app.use(cookieParser());

const KEY = randomstring.generate({
    length: 64,
    charset: 'hex'
});
// const KEY = '046820f772144342c1fbe30a66088b7002c9ee1f3785d3bbd131a45b17ac5c42';

function encrypt(input) {
    try {
        let iv = require('crypto').randomBytes(16);
        //console.info('iv',iv);
        let data = new Buffer(input).toString('binary');
        //console.info('data',data);
        
        key = new Buffer(KEY, "hex");
        //console.info(key);
        let cipher = require('crypto').createCipheriv('aes-256-cbc', key, iv);
        // UPDATE: crypto changed in v0.10

        // https://github.com/joyent/node/wiki/Api-changes-between-v0.8-and-v0.10 

        let nodev = process.version.match(/^v(\d+)\.(\d+)/);

        let encrypted;

        if( nodev[1] === '0' && parseInt(nodev[2]) < 10) {
            encrypted = cipher.update(data, 'binary') + cipher.final('binary');
        } else {
            encrypted =  cipher.update(data, 'utf8', 'binary') +  cipher.final('binary');
        }

        let encoded = new Buffer(iv, 'binary').toString('hex') + new Buffer(encrypted, 'binary').toString('hex');

        return Buffer.from(encoded, 'hex').toString('base64');
    } catch (ex) {
        // handle error
        // most likely, entropy sources are drained
        console.error(ex);
    }
}
function decrypt(encoded) {
    try {
        let combined = Buffer.from(encoded, 'base64');

        key = new Buffer(KEY, "hex");
        
        // Create iv
        let iv = new Buffer(16);
        
        combined.copy(iv, 0, 0, 16);
        edata = combined.slice(16).toString('binary');

        // Decipher encrypted data
        let decipher = require('crypto').createDecipheriv('aes-256-cbc', key, iv);

        // UPDATE: crypto changed in v0.10
        // https://github.com/joyent/node/wiki/Api-changes-between-v0.8-and-v0.10 

        let nodev = process.version.match(/^v(\d+)\.(\d+)/);

        let decrypted, plaintext;
        if( nodev[1] === '0' && parseInt(nodev[2]) < 10) {  
            decrypted = decipher.update(edata, 'binary') + decipher.final('binary');    
            plaintext = new Buffer(decrypted, 'binary').toString('utf8');
        } else {
            plaintext = (decipher.update(edata, 'binary', 'utf8') + decipher.final('utf8'));
        }
        return plaintext;
    } catch(ex) {
        return new Error('Decryption failed');
    }
}

const PORT = 3000;

// remove express header
app.use(function (req, res, next) {
  res.removeHeader("X-Powered-By");
  next();
});

// Load view engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// create application/x-www-form-urlencoded parser
const urlencodedParser = bodyParser.urlencoded({ extended: false });

// Index Route
app.get('/', (req, res) => {
    res.render('login', {
        failed: false
    });
});

app.post('/', urlencodedParser, (req, res) => {
    if (req.body.username === 'guest' && req.body.password === 'guest') {
        res.cookie('auth', encrypt('user=guest'),{ maxAge: 9000000, httpOnly: true });
        res.redirect('/profile');
    } else {
        res.render('login', {
            failed: true
        });
    }
});

// Profile Route
app.get('/profile', (req, res) => {
    if (req.cookies.auth == null) {
        res.redirect('/');
    } else {
        let result = decrypt(req.cookies.auth);
        if (result instanceof Error) {
            res.status(400);
            res.send('Error occurred');
        } else if (result === 'user=admin') {
            res.render('profile', {
                name: 'admin',
                title: 'Worthy One',
                message: 'GCTF{l34K1NG_1nF0Rm4710n_1n_Un3xP3C73d_w4YZ}'
            });
        } else {
            // res.send('scrub');
            res.render('profile', {
                name: 'guest',
                title: 'Wanderer',
                message: "I think the admin user has a more interesting profile"
            });
        }
    }
});

app.get('*', function(req, res){
  res.render('404');
});

// Start listening
app.listen(PORT, () => {
    console.log('Server started on port ' + PORT + '...');
});