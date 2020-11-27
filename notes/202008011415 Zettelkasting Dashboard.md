# Zettelkasting Dashboard
   ›[[202008011415]] 
   08-01-2020 02:15 PM

#inbox #terminal-commands 

- Getting the Ranking Of Zettel Reference Weight [[202010171623]]
- Find the Shortest And Longest Zettel [[202010181851]] 
- Shortest And Longest Zettel [[202010181851]]
         -More Quantitative Analysis
   - History Of Searches Macro [[202010282120]]

General ideas. 
1. create one unified macro group ✔︎
2. make compound file macro - componentalized ✔︎
3. have extensive readme
4. color code actions
5. have an action the reads current date ✔︎
6. us 1 10 100 and lifetime time frames
7. Number of zettel and number of words and size of archive 
8. Add trending graphs
9. number of inbox zettels
10. number of zettels on each hub
11. work on getting the weekday thing worked out.
12. Track pomodoros Moving 10 day average? Trend up or down.
13. Include a random zettel for the possibility of refactoring in the Evernote list.
14. Think how spaced repetition can help me.
15. If newNotestoday = 0 don't print new notes created so far today.
16. Add a random not in a random position in the list. ✔︎

Output format sample from https://forum.zettelkasten.de/discussion/1331/generating-a-timeline-view-of-a-zettelkasten
![](media/Time_line.png)

---
## Daily
- ✔︎ Sort the list with new first followed by most resent modified
- This work is proceeding

---
## Weekly
Monday,Tuesday
12,3

| Monday | Tuesday |
| :----: | :-----: |
|   12   |    3    |

Idea if I can get this to work??
ShopLaptop:~ will$ set i=7
ShopLaptop:~ will$ for i in {`date +"%u" -d "yesterday"`..1}; do
>   date +"%A" -d "$i days ago";
>   find . -mtime $i;
>   echo "";
> done
Suppose to output
    Monday
    Tuesday
    ./.file3
    ./.file2
    Wednesday
    Thursday
    ./.file1
    ./.file2

- Weekend Dashboard
    * ✔︎ yesterday new and modified
    * week new and modified
    * plan and keep record in a file
    * think about a chart/graph (pretty)

- Graph Pad in Keyboard Maestro
    - evernote:///view/597091/s5/e754530f-6169-44fc-a057-a447bdcb78e9/e754530f-6169-44fc-a057-a447bdcb78e9/

- Let's write out the procedure for getting the total number of zettels created in 7 days.
        Start with today’s date.
        20200809
        Find the number of new zettels 
        On the second date 20200808
        Find the number of new zettels and add this number to first number
        And so on till you have 7 days.
        
       - Or even better all this could be put into a .csv fill stored and read from and reused for monthly and maybe even a graph or chart.

Command for getting all the new zettels created in a week.
Wills-Laptop:~ will$ find ~/Dropbox/zettelkasten/*.md -mtime -8 ! -name "◆*"| egrep '20200809|20200808|20200807|20200806|20200805|20200804|20200803' | wc -l
	
---
## Month
82 new note created in the last month. 
163 notes new or modified in the last month. 
 
Zettelkasten Statistics.
           ★★★★★
     1367 - total number of notes
207805 - total word count
           ★★★★★

Notes worked with in the last month
---

- A KM macro that creates a graph or just the numbers of words written in the Zettelkasten per/week per/month per/year.
- Need to add Number of note modified (%Variable%tmp% - %Variable%temp%)
- Make table for the weekly list of new vs modified
- Might extend this for a month

Using - 2020070
82 new note created in the last month.
74 new note modified in the last month. 
156 notes total newly created  or modified in the last month. 

In a for loop the number of days can be changed to 32 and look for 
%ICUDateTimeMinus%1%month%yyyyMM%
This will limit the months to the correct number of days.

- Add a change in words from yesterday’s count
    1. Create a macro that runs at midnight the stores the total word count so far (zettelkastenWordsYesterday)
    2. Nature the total word count now and then subtract the variable zettelkastenWordsYesterday to get words added today (since midnight).


