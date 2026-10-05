import streamlit as st
import time
import re
arithmetic={
    "+":"a+b",
    "-":"a-b",
    "*":"a*b",
    "/":"a/b",
    "square":"a**2",
    "cube":"a**3",
    "square root":"a**0.5",
    "cube root":"a**0.33"
}
st.header("Welcome to Alithm by Mohd. Ali")
st.divider()
math_input=st.text_input("Enter your question to solve :")
isError=True
if(st.button("Send",type="primary")):
    for operator in sorted(arithmetic,key=len,reverse=True): #getting all keys{operators} of arithmatic
        if operator in math_input: #checking if the operator exists in user's query
            isError=False
            numbers=re.findall(r"\d+(?:\.\d+)?",math_input) #finding all numbers from input
            expr=arithmetic[operator] #getting the value{expression} for operators
            for i,number in enumerate(numbers): #(0,7),(1,3) for 7+3, 0 and 1 are index->value of i
                expr=expr.replace(chr(97+i),number) #for i=0 replace a{97+0} with 7{number}
            math_output=eval(expr)
            st.write_stream(
                time.sleep(0.05) or char for char in f"The answer is {math_output}."
            )
            break
    if(isError):
        st.write_stream(
                    time.sleep(0.05) or char for char in """Looks like your question is not of the types supprted..
                        Kindly provide the direct question like 7 + 3 
                        instead of what is 7 + 3 ?\n
                        Supported operations are:\n
                        1.Addition\n
                        2.Substraction\n
                        3.Multiplication\n
                        4.Division\n
                        5.Sqaure and square root\n
                        6.Cube and cube root""")

