// import redis library using ES6 import syntax
import { createClient } from 'redis';

//configuration options for the redis client
const options = {
    url: 'redis://localhost:6379', //redis server url
};

//create a redis client with custom options
const client = createClient(options);

//event listener for successful connections
client.on('connect', () =>{
    console.log('Redis client connected to the server');  
});

//event listener for errors during connection
client.on('error', (err) => {
    console.log(`Redis client connected to the server: ${err.message}`);
});

//connect to Redis
(async () => {
    try {
        await client.connect();
    } catch (err) {
        console.error(`Failed to connect to Redis: ${err.message}`)
    }
})();