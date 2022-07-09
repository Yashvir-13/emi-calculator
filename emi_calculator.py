import streamlit as st
def cal_emi(p,n,r):
  emi=((p*r)/100)*(pow((1+r),n))/(pow(1+(r/100),n)-1)
  return emi
st.title("Emi calculator")
principal=st.slider("Select the principal value(₹)",1000,5000000)
tenure=st.slider("Select the tenure",3,120)
roi=st.slider("Select the rate of interest",0.01,0.15)
balance_tenure=st.slider("Select the period after which the Outstanding Loan Balance is calculated",1,(1-(tenure*12)))
if st.button("Calculate EMI"):
  val=cal_emi(principal,tenure,roi)
  st.write(f"The EMI is {val:.3f}")
def calculate_outstanding_balance(p,n,r,m):
  balance=p*((pow(1+(r/100),n))-(pow(1+(r/100),m)))/(pow((1+(r/100)),n)-1)
  return balance
if st.button("Calculate outstanding balance"):
  val2=calculate_outstanding_balance(principal,tenure,roi,balance_tenure)
  st.write(f"Outstanding Loan Balance is {val2:.3f}")  



  