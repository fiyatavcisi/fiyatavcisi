const express = require('express');
const connectDB = require('./backend/db');

const app = express();
const PORT = process.env.PORT || 5000;

// MongoDB bağlantısı
connectDB();

app.get('/', (req, res) => {
    res.send('🎯 FiyatAvcısı API çalışıyor!');
});

app.listen(PORT, () => {
    console.log(`🚀 Server ${PORT} portunda çalışıyor`);
});