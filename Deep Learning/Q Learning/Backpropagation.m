#Theta1=ones(10,11)
#Theta2=2*ones(10,11)
#Theta3=3*ones(1,11)

#thetaVector = [ Theta1(:); Theta2(:); Theta3(:); ]
#size (thetaVector)
#deltaVector = [ D1(:); D2(:); D3(:) ]

#Theta1 = reshape(thetaVector(1:110),10,11)
#Theta2 = reshape(thetaVector(111:220),10,11)
#Theta3 = reshape(thetaVector(221:231),1,11)

epsilon = 1e-4;
n=1000
for i = 1:n,
  thetaPlus = theta;
  thetaPlus(i) += epsilon;
  thetaMinus = theta;
  thetaMinus(i) -= epsilon;
  gradApprox(i) = (J(thetaPlus) - J(thetaMinus))/(2*epsilon)
end;