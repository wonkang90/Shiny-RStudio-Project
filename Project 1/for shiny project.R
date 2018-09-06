plat_global<-ggplot(data=game, aes(x=reorder(game$Platform, game$Global_Sales), y=game$Global_Sales)) +
  geom_bar(aes(fill=game$Platform), stat = 'identity')

plat_jp<-ggplot(data=game, aes(x=reorder(game$Platform, game$JP_Sales), y=game$JP_Sales)) +
  geom_bar(aes(fill=game$Platform), stat = "identity")

plat_na<-ggplot(data=game, aes(x=reorder(game$Platform, game$NA_Sales), y=game$NA_Sales)) +
  geom_bar(aes(fill=game$Platform), stat = "identity")

plat_eu<-ggplot(data=game, aes(x=reorder(game$Platform, game$EU_Sales), y=game$EU_Sales)) +
  geom_bar(aes(fill=game$Platform), stat = "identity")





gl<-arrange(game, desc(Global_Sales))
newgameglobal<- gl %>% filter(., gl$Global_Sales >= 10)
plat_global2 <- ggplot(data = newgame, aes(x=reorder(newgame$Platform, newgame$Global_Sales, function(x) length(x)), y=newgame$Global_Sales)) + 
  geom_bar(aes(fill=newgame$Platform), stat = "identity")


na<-arrange(game, desc(NA_Sales)) #unessasary
newgamena<-na %>% filter(., na$NA_Sales >= 6)
plat_na2 <- ggplot(data = newgamena, aes(x=reorder(Platform, NA_Sales,function(x) length(x)), y= NA_Sales)) + 
  geom_bar(aes(fill=Platform), stat = "identity")

#this one seems simpler
newgamena0 <- game %>% select(., Platform, NA_Sales) %>% filter(., NA_Sales >= 6)
plat_na0 <- ggplot(data = newgamena0, aes(x= reorder(Platform, NA_Sales, function(x) length(x)), y=NA_Sales)) + geom_bar(aes(fill=Platform), stat = "identity")



eu <- arrange(game, desc(EU_Sales))
newgameeu <- eu %>% filter(., eu$EU_Sales >= 3)
plat_eu2 <- ggplot(data = newgameeu, aes(x=reorder(Platform, EU_Sales, function(x) length(x)), y=EU_Sales)) +
  geom_bar(aes(fill=Platform), stat = "identity")


jp <- arrange(game, desc(JP_Sales))
newgamejp <- jp %>% filter(., jp$JP_Sales >= 3)
plat_jp2 <- ggplot(data = newgamejp, aes(x=reorder(Platform, JP_Sales, function(x) length(x)), y= JP_Sales)) + 
  geom_bar(aes(fill=Platform), stat = "identity")



publisherandglobal<-game %>% select(., Publisher,Global_Sales) %>% filter(., Global_Sales >= 10)
publ_gl <- ggplot(data = publisherandglobal, aes(x=reorder(Publisher, Global_Sales,function(x) length(x)), y= Global_Sales)) + geom_bar(aes(fill=Publisher), stat = "identity")


pub_na <- ggplot(data = newgamena, aes(x=reorder(Publisher, NA_Sales, function(x) length(x)), y= NA_Sales)) + geom_bar(aes(fill=Publisher), stat = "identity")


pub_eu <- ggplot(data = newgameeu, aes(x=reorder(Publisher, EU_Sales, function(x) length(x)), y=EU_Sales)) +geom_bar(aes(fill=Publisher), stat = "identity")


pub_jp <- ggplot(data = newgamejp, aes(x=reorder(Publisher, JP_Sales, function(x) length(x)), y=JP_Sales)) +geom_bar(aes(fill=Publisher), stat = "identity")



test1 <- newgameglobal %>% group_by(Platform) %>% summarise(volume = sum(Global_Sales)) %>% mutate(share = volume/sum(volume)*100.0) %>% arrange(desc(volume))


ggplot(test1, aes(x="", y=share, fill=Platform)) + geom_bar(width = 1, size = 1, color= "white", stat = "identity") + coord_polar("y") + 
  geom_text(aes(label = paste0(round(share), "%")),position = position_stack(vjust = 0.5)) + labs(x = NULL, y = NULL, fill = NULL, title = "G sales share") + 
  guides(fill = guide_legend(reverse = TRUE)) + theme_classic() + 
  theme(axis.line = element_blank(), axis.text = element_blank(), axis.ticks = element_blank(),plot.title = element_text(hjust = 0.5, color = "#666666")) 


---


datagenre <- game %>% group_by(., Year, Genre) %>% summarise(., sumgl = sum(game$Global_Sales))
datagenre2 <- datagenre %>% group_by(., Year) %>% slice(which.max(sumgl))



first = group_by(game, Year) %>% summarize(., NorthAmerica = sum(NA_Sales), Europe = sum(EU_Sales), Global = sum(Global_Sales), Japan = sum(JP_Sales))

ggplot(data = first, aes(x=Year, y=Europe)) + geom_point() + geom_line(group=1)
ggplot(data = first, aes(x=Year, y=NorthAmerica)) + geom_point() + geom_line(group=1)
ggplot(data = first, aes(x=Year, y=Japan)) + geom_point() + geom_line(group=1)
ggplot(data = first, aes(x=Year, y=Global)) + geom_point() + geom_line(group=1)
 




