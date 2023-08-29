import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ', error.message);
});

const promisifiedGet = promisify(client.get).bind(client);

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, (err, response) => {
    if (err) {
      console.log(err);
    } else {
      console.log('Reply:', response);
    }
  });
}

async function displaySchoolValue (schoolName) {
  try {
    const result = await promisifiedGet(schoolName);
    console.log(result);
  } catch (error) {
    console.log(error.message);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
