module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
  runtimeCompiler: true,
  productionSourceMap: false,
  filenameHashing: false,
  chainWebpack: (config) => {
    config.optimization.delete('splitChunks'); config.plugin('prefetch').tap((options) => {
      options[0].fileBlacklist = options[0].fileBlacklist || [];
      options[0].fileBlacklist.push(/\.mp3$/);
      return options;
    });
    config.plugins.delete('preload');
  },
};
