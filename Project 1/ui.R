


dashboardPage(
  skin = "red",


  dashboardHeader(title = "Game data"),
  
  dashboardSidebar(
    sidebarMenu(
      menuItem("Welcome", tabName = "picture",icon = icon("th")),
      menuItem("Graph for Years", tabName = "Graph3", icon = icon("th")),
      menuItem("Graph for Platform", tabName = "Graph", icon = icon("th")),
      menuItem("Graph for publisher", tabName = "Graph2", icon = icon("th")),
      menuItem("Data Table", tabName = "Data",icon = icon("th"))
      
    )
  ),
  
  
  
  
  dashboardBody(
    tabItems(
      tabItem(tabName = "picture",
        fluidPage(
          mainPanel('Welcome',
            tabsetPanel(type = "tabs",
            tabPanel("Picture", tags$iframe(src="https://www.timothysykes.com/wp-content/uploads/2013/04/3-Video-Game-Companies-for-This.jpg",
            width = "650", height= "400")),
            
            tabPanel("Video", tags$iframe(src="https://www.youtube.com/embed/H7g8PNkV1ek", width="100%", height = "580px"))
            )
            
          ) 
        ) 
          ),
          
          
     
        
      
      
      tabItem(tabName = "Data",
        fluidRow(
          column(4,
              selectInput("Platform",
                          "Platform:",
                          c("All",
                            unique(as.character(game$Platform))))   
                 
                 
                 ),
          
          column(4, 
              selectInput("Publisher",
                          "Publisher:",
                          c("All",
                            unique(as.character(game$Publisher))))
              
              ),
          column(4,
              selectInput("Year",
                          "Year:",
                          c("All",
                            unique(as.character(game$Year))))
              )
          
       ),
        
        fluidRow(
          DT::dataTableOutput("table")
        )
        
    ),
      
      tabItem(tabName = "Graph",
        fluidRow(
          box(plotOutput('graph1'), width = 10),
          tabBox(
            title = "Graph",
            id="tabset1", height = "800px", width = "750px",
          titlePanel("Game graph"),
          sidebarLayout(
            sidebarPanel(
              selectInput(inputId = "platin", label = "Platform Graph:",
                          choices = c("Global", "North America", "Europe", "Japan"),selected = 1)),
          
          mainPanel(
            plotOutput("platgr")
          )
              
            )
            
          )
  
      
          )
        
       ),
      
    tabItem(tabName = "Graph2",
            fluidRow(
              box(plotOutput('graph2'), width = 10),
              tabBox(
                title = "Graph",
                id="tabset1", height = "800px", width = "750px",
                titlePanel("Game graph"),
                sidebarLayout(
                  sidebarPanel(
                    selectInput(inputId = "platin2", label = "Publisher Graph:",
                                choices = c("Global", "North America", "Europe", "Japan","Pie"),selected = 1)),
                  
                  mainPanel(
                    plotOutput("platgr2")
                  )
                  
                )
                
              )
              
              
            )
            
    ),
    tabItem(tabName = "Graph3",
            fluidRow(
              box(plotOutput('graph3'), width = 10),
              tabBox(
                title = "Graph",
                id="tabset1", height = "800px", width = "750px",
                titlePanel("Game graph"),
                sidebarLayout(
                  sidebarPanel(
                    selectInput(inputId = "platin3", label = "Year Graph:",
                                choices = c("Global", "North America", "Europe", "Japan"),selected = 1)),
                  

                 
                  mainPanel(

                    plotOutput("platgr3")
                 )

                )
                
              )
              
              
            )
            
    )    
            
            
            
          
    
    )
    
    
     )
   )
  
  
  





