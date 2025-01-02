
A="relational"
B="nested relational"
C="cross-table"
D="nested cross-table"


table_types = {
    # Paper 08461
    "S3.T1.6": A,
    "S3.T2.3.3": A,
    "S4.T3.6.6.6.6.4": B,
    "S4.T4.30.30": B,


    # Paper 11508
    "S5.T1.8": A,
    "S5.T2.6": A,
    "S5.T3.6": A,
    "S5.T4.9": A,
    "S5.T5.6": A,
    "S5.T6.9": A,
    "S5.T7.3": A,
    "S5.T8.3": A,
    "S5.T9.3": A,
    "S5.T10.3": A,

    # Paper 12522
    "S3.T1.9.1": B,
    "S3.T2.140": D,
    "S3.T4.1.3": A,
    "S3.T4.2.2": A,

    # Paper 19483
    "S3.T1.140.140": D,
    "S4.T2.30.30": D,
    "S4.T3.50.50": D,
    "S4.T4.14.14": A,
    "S4.T5.14.14": D,
    "S4.T6.64.64": D,

    # Paper 20164
    "S3.T1.1": A,
    "S3.T2.1": B,

    # Paper 01443
    "S3.T1.3": B,
    "S3.T3.1": A,
  
    # Paper 04960
    "S2.T1.2": A,
    "S4.T2.10": A,
    "S4.T3.2": A,
    "S4.T4.2": A,
    "S4.T5.6": D,
    "S4.T6.4": D,
    "S4.T7.8": D,
    "S4.T8.8": D,

    # Paper 05624
    "S4.T1.1.1": A,
    "S4.T2.1.1": A,
    "S5.T3.4":A,
    "S5.T4.2":A,
    "S5.T5.4":A,
    "S5.T6.4":A,
    "S5.T7.1": A,

    # Paper 07635
    "S4.T1.30": B,
    "S4.T2.30": B,

    # Paper 08509
    "S3.T1.1.1": D,
    "Sx1.T2.46.46": A
}