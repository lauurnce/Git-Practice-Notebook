module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: fae,
        inlineRequires: false,
      },
    }),
  },
};