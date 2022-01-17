# Discord-Bot-Membercount
**A dead simple -selfhosted- Discord Bot that can count users on a Server**

### Featurelist

- [x] Custom display for joins and leaves
- [x] Placeholders (User-Count, Servername, more on request)
- [x] Custom Status 
- [ ] Custom Status text


### Config Example
**At the first start the config-directory and the confugartions-file will be created.
In the config.ini settings can be made.
E.g. which bots are monitored. In addition, users and channels can be entered, which should be notified in the event of a failure.
(With each entry several entries are possible... each separated by a space)**
```
[Settings]
token = 
bot_prefix = !
owner_id = 
channel = 
status = Counting members... 🔄

[Messages]
# available placeholders: {0} user-ammount | {1} servername |  =  
join = 「⏫」 {0} Members on {1}
leave = 「⏬」 {0} Members {1}
```

### Future plans
Revision of the code, because the development of the library "discord.py" ended on 28th August 2021...
Rewrite of the code with Nextcord, a fork of discord.py
