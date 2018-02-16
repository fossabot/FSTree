from crontab import CronTab as ct

jobs = ct(user=True).crons
any_good = any(
	(str(job)).__contains__('fileListScript')
	for job in jobs
)
if any_good:
	print('Job already scheduled')
else:
	print('Adding job')
