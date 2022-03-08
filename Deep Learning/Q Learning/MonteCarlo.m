# Monte Carlo tree (Reinforcement Algorithm)

N =100; #Total no of Points
n= 0; #Points inside a circle

for episode=1:N
    x = rand();
    y= rand() ;
    if (x^2+y^2<=1)
      n = n+1;
    endif
endfor

pi = 4 *(n/N);
disp(["When N =",num2str(N)," \n Estimated PI:", num2str(pi)]);