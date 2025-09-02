const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        await mongoose.connect('mongodb+srv://avcisifiyat_db_user:CtypmWevtpbbSDKz@fiyatavcisi-cluster.tql5nqo.mongodb.net/?retryWrites=true&w=majority&appName=fiyatavcisi-cluster', {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
        console.log('✅ MongoDB bağlandı');
    } catch (error) {
        console.error('❌ MongoDB bağlantı hatası:', error);
        process.exit(1);
    }
};

module.exports = connectDB;
