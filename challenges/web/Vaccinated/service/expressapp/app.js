const express = require('express');
const app = express();
const path = require('path');
const mongoose = require('mongoose');
let bodyParser = require('body-parser');
const PORT = 3000;
const CONURL = 'mongodb://mongoadmin:oAKzFPFRCXTXoRSAKe@mongo:27017/mydb?authSource=admin';

mongoose.connect(CONURL, (err) => {
    if (err) {
        console.log('Failed to connect to mongodb on startup');
        process.exit(1);
    }
});

// load model
let User = require('./models/user');

// remove express header
app.use(function (req, res, next) {
  res.removeHeader("X-Powered-By");
  next();
});

// Load view engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// create application/x-www-form-urlencoded parser
let urlencodedParser = bodyParser.urlencoded({ extended: true })

// Index Route
app.get('/', (req, res) => {
    res.render('login', {
        failed: false
    });
});

app.post('/', urlencodedParser, (req, res) => {
    User.findOne({username: req.body.username, password: req.body.password}, (err, users) => {
        if (err) {
            console.error(err);
            res.send('Error occurred');
        } else if (users != null) {
            res.send('GCTF{NO5qL_do35_noT_M34n_No_1nj3cT1on}');
        } else {
            res.render('login', {
                failed: true
            });
        }
    });
});

app.get('*', function(req, res){
  res.render('404');
});

// Start listening
app.listen(PORT, () => {
    console.log('Server started on port ' + PORT + '...');
});
