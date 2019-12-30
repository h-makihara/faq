module.exports = {
    devServer: {
        public: "yourproxy",
        port: 8080,
        disableHostCheck: true,
        watchOptions: {
            poll: true
        }
    },
};
