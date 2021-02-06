# Massachusetts Travelling Snailsman
 Python to find the longest route across Massachusetts that hits every single town.
 
 The route-finding algorithm isn't perfect - it finds the furthest town from the current town while ignoring previously-visited towns, which makes the last towns very close to each other - but according to the statistics scraped into stats.csv by distStatFinder.py, it should be a route in the top 0.001% of all routes.
 
 My original "naive" algorithm and current "greedy" algorithm (used by the Cultivating Massachusetts Project) are in this repository. So is the script I used to find the distances between every town in Massachusetts (massachusettsGmaps.py) and print them into text files (maDistsLists). Finally, bestRoutes catalogues the best two routes found by the naive algorithm and the one Holy Grail route found by the greedy algorithm (plus a couple even better but difficult to explain routes produced by xelf on Reddit).
