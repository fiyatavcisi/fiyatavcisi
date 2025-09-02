const express = require('express');
const mongoose = require('mongoose');

const app = express();
const PORT = process.env.PORT || 5000;

// MongoDB bağlantısı (test connection string ile)
const mongoURI = process.env.MONGODB_URI || 'mongodb+srv://avcisifiyat_db_user:CtypmWevtpbbSDKz@fiyatavcisi-cluster.tql5nqo.mongodb.net/fiyatavcisi?retryWrites=true&w=majority';

mongoose.connect(mongoURI)
  .then(() => console.log('✅ MongoDB bağlandı'))
  .catch(err => console.error('❌ MongoDB bağlantı hatası:', err));

// Basit route
app.get('/', (req, res) => {
  res.send('🎯 FiyatAvcısı API çalışıyor!');
});

app.listen(PORT, () => {
  console.log(`🚀 Server ${PORT} portunda çalışıyor`);
});
