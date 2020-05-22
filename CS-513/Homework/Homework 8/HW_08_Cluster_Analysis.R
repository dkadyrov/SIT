#  Course          :  
#  First Name      : Khasha
#  Last Name       : Dehnad
#  Id              : 12345
#  purpose         : HW 9 Ann  cluster Analysis 

## Step 0 clean up!!!




rm(list=ls())
file<-file.choose()

bc_raw<-  read.csv(file)
summary(bc_raw) 
summary(bc_raw$diagnosis)
table(bc_raw$diagnosis)

#mmnorm <-function(x,minx,maxx)
#{z<-((x-minx)/(maxx-minx))
#return(z)                              
#}
mmnorm2 <-function(x)
{z<-((x-min(x))/(max(x)-min(x)))
return(z)                              
}

myvector<-1:20
mmnorm2(myvector)


 
bc<- data.frame(id=as.character(bc_raw$id)
                ,diagnosis=as.factor(bc_raw$diagnosis) 
                ,     	radius_mean =mmnorm2(	bc_raw$radius_mean)
                ,      texture_mean=mmnorm2(bc_raw$texture_mean)
                ,      perimeter_mean=mmnorm2(bc_raw$perimeter_mean)
                ,      area_mean=mmnorm2(bc_raw$area_mean)
                ,      smoothness_mean=mmnorm2(bc_raw$smoothness_mean)
                ,      compactness_mean=mmnorm2(bc_raw$compactness_mean)
                ,      concavity_mean=mmnorm2(bc_raw$concavity_mean)
                ,      concave.points_mean=mmnorm2(bc_raw$concave.points_mean)
                ,      symmetry_mean=mmnorm2(bc_raw$symmetry_mean)
                ,      fractal_dimension_mean=mmnorm2(bc_raw$fractal_dimension_mean)
                ,      radius_se=mmnorm2(bc_raw$radius_se)
                ,      perimeter_se=mmnorm2(bc_raw$perimeter_se)
                ,      texture_se=mmnorm2(bc_raw$texture_se)
                ,      area_se=mmnorm2(bc_raw$area_se)
                ,      smoothness_se=mmnorm2(bc_raw$smoothness_se)
                ,      compactness_se=mmnorm2(bc_raw$compactness_se)
                ,      concavity_se=mmnorm2(bc_raw$concavity_se)
                ,      concave.points_se =mmnorm2(bc_raw$concave.points_se)
                ,      symmetry_se=mmnorm2(bc_raw$symmetry_se)
                ,       fractal_dimension_se=mmnorm2(bc_raw$fractal_dimension_se)
                ,       radius_worst=mmnorm2(bc_raw$radius_worst)
                ,       texture_worst=mmnorm2(bc_raw$texture_worst)
                ,       perimeter_worst=mmnorm2(bc_raw$perimeter_worst)
                ,       area_worst=mmnorm2(bc_raw$area_worst)
                ,       smoothness_worst=mmnorm2(bc_raw$smoothness_worst)
                ,       compactness_worst=mmnorm2(bc_raw$compactness_worst)
                ,       concavity_worst=mmnorm2(bc_raw$concavity_worst)
                ,       concave.points_worst=mmnorm2(bc_raw$concave.points_worst)
                ,      	symmetry_worst=mmnorm2(bc_raw$symmetry_worst)
                ,       fractal_dimension_worst=mmnorm2(bc_raw$fractal_dimension_worst)
) 


bc_dist<-dist(bc[,c(-1,-2)])
hclust_resutls<-hclust(bc_dist )
plot(hclust_resutls)
hclust_2<-cutree(hclust_resutls,2)
table(Cluster=hclust_2,Actual=bc[,2])

dev.off()
?kmeans

kmeans_2<- kmeans(bc[,c(-1,-2)],2,nstart = 10)
kmeans_2$cluster
table(kmeans_2$cluster,Actual=bc[,2] )
