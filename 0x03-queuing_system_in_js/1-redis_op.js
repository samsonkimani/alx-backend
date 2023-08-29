import { createClient } from 'redis';
import redis from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ', error.message);
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, (err, response) => {
    if (err) {
      redis.print(err);
    } else {
      redis.print(`Reply: ${response}`);
    }
  });
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, response) => {
    if (err) {
      redis.print(err);
    } else {
      redis.print(response);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
