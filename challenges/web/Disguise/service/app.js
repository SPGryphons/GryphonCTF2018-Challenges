const express = require('express');
const app = express();
const path = require('path');
const PORT = 3000;

// remove express header
app.use(function (req, res, next) {
  res.removeHeader("X-Powered-By");
  next();
});

// Load view engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// Index Route
app.get('/', (req, res) => {
    res.redirect('/index.html');
});

app.get('/index.html', (req, res) => {
    res.render('index');
});

app.post('/index.html', (req, res) => {
    res.send('GCTF{pr377y_L19h7_pR377Y_7R1cKy}');
});

app.get('*', function(req, res){
  res.render('404');
});

// Start listening
app.listen(PORT, () => {
    console.log('Server started on port ' + PORT + '...');
});