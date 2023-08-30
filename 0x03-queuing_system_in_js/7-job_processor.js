import { createQueue } from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
      job.progress(100);
      done();
    }, 2000);
  }
}

const queue = createQueue({ concurrency: 2 });

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
