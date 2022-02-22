e_quakes <- datasets::quakes


head(e_quakes,10)
tail(e_quakes, 10)


summary(e_quakes$depth)

summary(e_quakes)


#################
plot(e_quakes$depth)
plot(e_quakes$mag, e_quakes$depth, type = "p")

plot(e_quakes)


#############Plot and lines

plot(e_quakes$depth, type = 'l') # p: Points, l: Lines, b: Both
plot(e_quakes$depth, xlab = 'Depth',
     ylab = 'No of Instances', main = 'Depth of Earthquake',
     col = 'blue')

#Horizontal Bar Plot

barplot(e_quakes$mag, main = 'Magnitude of the Earthquake', 
        ylab = 'Magnitude', col = 'blue', horiz = F, axes = T)


# Histogram 
hist(e_quakes$mag)
hist(e_quakes$mag,
     main = 'Magnitude of the Earthquaker',
     xlab = 'Magnitude',
     col = 'blue')

hist(e_quakes$depth,
     main = 'Depth of the Earthquake',
     xlab = 'Depth',
     col = 'blue')

# Single Box Plot
boxplot(e_quakes$mag, main = "Boxplot of Magnitude")
boxplot.stats(e_quakes$mag)$out

# Multiple box plots
boxplot(e_quakes[,3:4], main='Multiple')

# Margin of the grid (mar),
# No of rows and columns (mfrow)
# wether a border is to be included(bty)
# and position of the labels (las: 1 for Horizontal, las:0 for Vertical)
# bty - box around the plot

par(mfrow = c(3,3), mar=c(2,5,2,1), las=0, bty = 'o')

plot(e_quakes$mag)
plot(e_quakes$mag, e_quakes$depth)
plot(e_quakes$mag, type = 'l')
plot(e_quakes$mag, type = 'l')
plot(e_quakes$mag, type = 'l')
barplot(e_quakes$mag, main = 'Magnitude of the earthquake', 
        xlab = 'Magnitude', col = 'green', horiz = TRUE)
hist(e_quakes$depth)
boxplot(e_quakes$depth)
boxplot(e_quakes[,0:4], main = 'Multiple Box Plots')

# Standard deviation
sd(e_quakes$depth, na.rm = T) # by removing the NA values
skewness(e_quakes$depth)
kurtosis(e_quakes$depth)
