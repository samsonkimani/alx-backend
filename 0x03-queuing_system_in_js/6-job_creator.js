import { createQueue } from 'kue';

const kue = createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

const job = kue.create('push_notification_code', jobData)
  .save(err => {
    if (!err) {
      console.log(`Notification job created ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
