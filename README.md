# Cron parser script

Cron parser script.

Created by Alexander Tolkachev (alexander.e.tolkachev@gmail.com)

## Script
### Requirements

* `Python 3.6+`

### Execution

* `python cron_parser.py -c/--cron "<your cron string>"`

Example:

`python cron_parser.py --cron "*/15 0 1,15,16-19 * 1-5 /usr/bin/find"`

Example output:

```shell script
minute			0 15 30 45 
hour			0
day_of_month            1 15 16 17 18 19  
month			1 2 3 4 5 6 7 8 9 10 11 12 
day_of_week		1 2 3 4 5 
command			/usr/bin/find
```
