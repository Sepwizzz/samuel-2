print("programa de con version de salario por horas")

A = int(input("dijite el mumero de horas que trabajo"))


if A < 40:
    A2 = A * 2600 
    print("el valor por",A, "horas de trabajo es de: " ,A2) 
    
elif A > 40: 
    B = 40 - A 
    C = B * 5000
    D = C + 104000
    print("el valor por" ,A, " horas de trabajdo",D)
    
              