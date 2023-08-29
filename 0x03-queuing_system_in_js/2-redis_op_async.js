import { createClient } from 'redis';
import { promisify } from 'util';
import redis from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ', error.message);
});

const promisifiedGet = promisify(client.get).bind(client);
const promisifySet = promisify(client.set).bind(client);

async function setNewSchool (schoolName, value) {
	try {
		const result = await promisifySet(schoolName, value);
		redis.print(`Reply: ${result}`);
	} catch (error) {
		redis.print(error.message);
	}
}

async function displaySchoolValue (schoolName) {
  try {
    const result = await promisifiedGet(schoolName);
    redis.print(result);
  } catch (error) {
    redis.print(error.message);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
