import gspread

sa = gspread.service_account(filename="service_account.json")
sh = sa.open("RSC10 | Graphics Data")
wks = sh.worksheet("FixturesOutput")

tierCount = wks.get("A2:A")





## Take lineups from GSheet
## Teams to dictionary
## Split for Week number
## Set ranges on WeekNum
## Split lists for conferences
## Edit PSD text for teams and schedule
## Unhide logos