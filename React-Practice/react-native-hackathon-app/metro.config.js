module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: fals,
        inlineRequires: false,
      },
    }),
  },
};