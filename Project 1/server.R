function(input, output) {
  
  output$table <- DT::renderDataTable(DT::datatable({
    data <- game
    
    if (input$Platform != "All") {
      data <- data[data$Platform == input$Platform,]
    }
    
    if (input$Publisher != "All") {
      data <- data[data$Publisher == input$Publisher,]
      
    }
    
    if (input$Year != "All") {
      data <- data[data$Year == input$Year,]
    }
    
    data
    
  }))
  
  output$graph1 <- renderPlot({
    if (input$platin == 'Global'){
      ggplot(data = newgameglobal, aes(x=reorder(Platform, Global_Sales, function(x) length(x)), y=Global_Sales)) + 
        geom_bar(aes(fill=Platform), stat = "identity")
      }else if (input$platin == 'North America'){
        ggplot(data = newgamena, aes(x=reorder(Platform, NA_Sales,function(x) length(x)), y= NA_Sales)) + 
          geom_bar(aes(fill=Platform), stat = "identity")
        
      }else if (input$platin == 'Europe'){
        ggplot(data = newgameeu, aes(x=reorder(Platform, EU_Sales, function(x) length(x)), y=EU_Sales)) +
          geom_bar(aes(fill=Platform), stat = "identity")
      }else if (input$platin == 'Japan'){
        ggplot(data = newgamejp, aes(x=reorder(Platform, JP_Sales, function(x) length(x)), y= JP_Sales)) + 
          geom_bar(aes(fill=Platform), stat = "identity")
        
        
      }
  })
   
  output$graph2 <- renderPlot({
    if (input$platin2 == 'Global'){
      ggplot(data = publisherandglobal, aes(x=reorder(Publisher, Global_Sales,function(x) length(x)), y= Global_Sales)) + 
        geom_bar(aes(fill=Publisher), stat = "identity")
    }else if (input$platin2 == 'North America'){
      ggplot(data = newgamena, aes(x=reorder(Publisher, NA_Sales, function(x) length(x)), y= NA_Sales)) + 
        geom_bar(aes(fill=Publisher), stat = "identity")
    }else if (input$platin2 == 'Europe'){
      ggplot(data = newgameeu, aes(x=reorder(Publisher, EU_Sales, function(x) length(x)), y=EU_Sales)) + 
        geom_bar(aes(fill=Publisher), stat = "identity")
    }else if (input$platin2 == 'Japan'){
      ggplot(data = newgamejp, aes(x=reorder(Publisher, JP_Sales, function(x) length(x)), y=JP_Sales)) + 
        geom_bar(aes(fill=Publisher), stat = "identity")
      
    }else if (input$platin2 == "Pie"){
      ggplot(test1, aes(x="", y=share, fill=Publisher)) + geom_bar(width = 1, size = 1, color= "white", stat = "identity") + coord_polar("y") +
        geom_text(aes(label = paste0(round(share), "%")),position = position_stack(vjust = 0.5)) + labs(x = NULL, y = NULL, fill = NULL, title = "Pie Chart") + 
        guides(fill = guide_legend(reverse = TRUE)) + theme_classic() + 
        theme(axis.line = element_blank(), axis.text = element_blank(), axis.ticks = element_blank(),plot.title = element_text(hjust = 0.5, color = "#666666"))
      
    }
    
    
    
  })
  output$graph3 <- renderPlot({
    if (input$platin3 == 'Global'){
      ggplot(data = first, aes(x=Year, y=Global)) + geom_point() + geom_line(group=1)
      
    }else if (input$platin3 == 'North America'){
      ggplot(data = first, aes(x=Year, y=NorthAmerica)) + geom_point() + geom_line(group=1)
      
    }else if (input$platin3 == 'Europe'){
      ggplot(data = first, aes(x=Year, y=Europe)) + geom_point() + geom_line(group=1)
      
    }else if (input$platin3 == 'Japan'){
      ggplot(data = first, aes(x=Year, y=Japan)) + geom_point() + geom_line(group=1)
      
      
    }
    
    
    
  })
  
  
}