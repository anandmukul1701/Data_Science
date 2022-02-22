airquality <- datasets::airquality
head(airquality,10)
tail(airquality, 10)

#columns
airquality[ ,c(1,2)]
df <- airquality[ , -6]
df

airquality$Temp

summary(airquality$Ozone)

summary(airquality)


#################
plot(airquality$Wind)
plot(airquality$Temp, airquality$Wind, type = "p")

plot(airquality)
#############Plot and lines

plot(airquality$Wind, type = 'l') # p: Points, l: Lines, b: Both
plot(airquality$Wind, xlab = 'Ozone Concentration',
     ylab = 'No of Instances', main = 'Ozone levels in NY City',
     col = 'blue')

#Horizontal Bar Plot

barplot(airquality$Ozone, main = 'Ozone Concentration in air', 
        ylab = 'Ozone levels', col = 'blue', horiz = F, axes = T)


# Histogram 
hist(airquality$Temp)
hist(airquality$Temp,
     main = 'Solar Radiation Values in Air',
     xlab = 'Solar rad.',
     col = 'blue')

# Single Box Plot
boxplot(airquality$wind, main = "Boxplot")
boxplot.stats(airquality$Wind)$out

# Multiple box plots
boxplot(airquality[,1:4], main='Multiple')

# Margin of the grid (mar),
# No of rows and columns (mfrow)
# wether a border is to be included(bty)
# and position of the labels (las: 1 for Horizontal, las:0 for Vertical)
# bty - box around the plot

par(mfrow = c(3,3), mar=c(2,5,2,1), las=0, bty = 'o')

plot(airquality$ozone)
plot(airquality$Ozone, airquality$wind)
plot(airquality$ozone, type = 'l')
plot(airquality$ozone, type = 'l')
plot(airquality$ozone, type = 'l')
barplot(airquality$Ozone, main = 'Ozone Concentration in air', 
        xlab = 'ozone levels', col = 'green', horiz = TRUE)
hist(airquality$Solar.R)
boxplot(airquality$Solar.R)
boxplot(airquality[,0:4], main = 'Multiple Box Plots')
