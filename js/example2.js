// import redis library using ES6 import syntax
import {createClient} from 'redis';

// create a redis client
const client = createClient();

//event listener for successsful connection
client.on('connect', () => {
    console.log(`Redis client connected to the server`);
});

//event listener for errors during connection
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

//connect to redis
client.connect();