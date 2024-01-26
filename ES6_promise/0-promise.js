function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve('true');
        reject(new Error('API'));
      });
    });
  }
  export default getResponseFromAPI;
