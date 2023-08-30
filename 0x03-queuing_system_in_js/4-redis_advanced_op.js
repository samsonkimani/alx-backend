import redis, { createClient } from 'redis';
import * as util from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ', error.message);
});

function usingHset (dict) {
  for (const [key, value] of Object.entries(dict)) {
    client.hset('HolbertonSchools', key, value, (error, response) => {
      if (error) {
        console.log(error);
      } else {
        redis.print(`Reply: ${response}`);
      }
    });
  }
}

const dict = {
  Portland: 50,
  Seatle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

usingHset(dict);

client.hgetall('HolbertonSchools', (error, response) => {
  if (error) {
    redis.print(error);
  } else {
    redis.print(util.inspect(response, false, null, true));
  }
});
