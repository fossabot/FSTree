# FSTree
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fkaranrajpal14%2FFSTree.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fkaranrajpal14%2FFSTree?ref=badge_shield)


## What?

FSTree is a script I use to maintain snapshots of my file system. I use Linux's **tree** command to do list the contents of my filesystem in a tree format.

## Why?

To maintain a snapshot of my filesystem. If I ever find myself in a situation where I lose all my data on my device, I can at least know what I had and download most of it back. The critical data is backed up, of course. This is mainly for data that I can re-download if need be. 

I did come across a similar situation of late when my HDD died. I couldn't do much since it was unreadable and I _**obviously**_ don't remember everything that was on it :(

## How do I set this up?

1. Clone the repo

2. Open your crontab by running `crontab -e` in your terminal

3. Add the following line to the end of your crontab `30 14 * * * python3 <PATH_TO_REPO>/FSTree.py`

4. Profit

## Note:

You need to have Python 3.x installed to run this. That's the only requirement.

Also, in case you haven't noticed, I'm running the cron job at 2.30 PM everyday. You can modify that as per your requirement by modifying the crontab. To know more on how to schedule the cron job as you deem fit, go through it's syntax [here](https://www.computerhope.com/unix/ucrontab.htm)


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fkaranrajpal14%2FFSTree.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fkaranrajpal14%2FFSTree?ref=badge_large)