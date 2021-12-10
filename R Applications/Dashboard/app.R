# Importing the Libraries

library(shiny)
#library(shinydashboard)
library(semantic.dashboard)
library(DT)

ui <- dashboardPage( theme= "slate",
    dashboardHeader(title = "PanduDashboard"),
    dashboardSidebar(
        sidebarMenu(
            menuItem("Iris",tabName = "Iris", icon = icon("tree")),
            menuItem("Cars", tabName = "Cars" , icon = icon("car"))
        )
        
    ),
    
    dashboardBody(
        tabItems(
            tabItem("Iris",
                    
                    box(plotOutput("Correlation_Plot"),width = 8),
                    box(
                        selectInput("features","Features:",
                                    c("Sepal.Width","Petal.Length",
                                      "Petal.Width")),width = 5
                    )
                    
                    ),
            
            tabItem("Cars",
                     fluidPage(
                         h1("Cars"),
                         dataTableOutput("carstable")
                     )
                     
                     )
        )
    
      
    )
)


server <- function(input, output)
{
    output$Correlation_Plot <- renderPlot(
        {
            plot(iris$Sepal.Length,iris[[input$features]],
                 xlab="Sepal Length", ylab = "Features")
        }
    )
    output$carstable <- renderDataTable(mtcars)
}

#Run the Application

shinyApp(ui, server)