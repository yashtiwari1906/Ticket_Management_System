import React, { useState } from 'react'
import { redirect, useNavigate } from 'react-router-dom';

import Base from "../core/Base";
import { signup } from './helper';


const Signin = () => {
    const navigate = useNavigate();
    const [values, setValues]=  useState({
        name: "",
        email:"",
        contact:"", 
        error: "",
        success: false,
    });
    
    const {name, email, contact, error, success} = values;

    const handleChange = name => event_case => {
        setValues({...values,error: false, [name]: event_case.target.value})
    }

    function loadCart() {
        let EventName = "";
        let Row = 0; 
        let Col = 0;
        console.log("loadCart is hit")
        if (typeof window !== undefined){
            if (localStorage.getItem("EventName")){
                EventName = JSON.parse(localStorage.getItem("EventName"))
            }
        }
        if (typeof window !== undefined){
            if (localStorage.getItem("Row")){
                Row = JSON.parse(localStorage.getItem("Row"))
            }
        }
        if (typeof window !== undefined){
            if (localStorage.getItem("Col")){
                Col = JSON.parse(localStorage.getItem("Col"))
            }
        }
        
        
       
        return [EventName, Row, Col];
    }

    const HomeRedirect = () => {
        if (success){
            return(
                navigate("/confirmation")
            )
        }
        
    }
    
    const onSubmit=(event_case)=>{
        console.log("why why")
        var event = ""; 
        var col = 0;
        var row = 0;
        
        [event, row, col] = loadCart();
        
        event_case.preventDefault();
        setValues({...values, error: false})
        signup({name,email,contact, event, row, col})    // replace 1 and 5 with (row, col)
        .then((data)=> {
            console.log("DATA", "-------", data);
            if(data.details.event === event){
                setValues({
                    ...values,
                    name:"",
                    email: "",
                    contact: "",
                    error: "",
                    success: true
                })
                
            }
            else{
                console.log("error happened")
                setValues({
                    ...values,
                    error: true,
                    success: false
                })
            }
        }
        )
        .catch((err) => {
            console.log(err)
            setValues({
                ...values,
                error: true,
                success: false
            })
        })

    }

    const successMessage =() => {
        console.log("success", success)

        return (
            <div className="row">
                <div className="col-md-6 offset-sm-3 text-left">
                    <div className="alert-success" style={{display: success ? "" : "none" }}>
                        Ticket saved successfully.
                       
                    </div>
                </div>
            </div>
        )
    } 
    const errorMessage =() => {
        return (
            <div className="row">
                <div className="col-md-6 offset-sm-3 text-left">
                    <div className="alert alert-danger" style={{display: error ? "" : "none" }}>
                        something went wrong
                    </div>
                </div>
            </div>
        )
    } 

    const signUpForm=()=>{
        return (
            <div className="row">
                <div className="col-md-6 offset-sm-3 text-left">
                    <form>
                      <div className="form-group">
                          <label className="text-light">
                              Name
                          </label>
                          <input type="text"
                          className="form-control"
                          values={name}
                          onChange={handleChange("name")}/>
                      </div>
                      <div className="form-group">
                          <label className="text-light">
                              Email
                          </label>
                          <input type="text"
                          className="form-control"
                          values={email}
                          onChange={handleChange("email")}/>
                      </div>
                      <div className="form-group">
                          <label className="text-light">
                              Contact
                          </label>
                          <input type="text"
                          className="form-control"
                          values={contact}
                          onChange={handleChange("contact")}/>
                      </div>
                      <button onClick={onSubmit} className="btn btn-success btn-block">Submit</button>
                    </form>

                </div>
            </div>    
        )
    }





  return (
    <Base title = "Grab your Ticket" description = "Enter your email and name for confirmation">
    {successMessage()}
    {errorMessage()}
    {HomeRedirect()}
    {signUpForm()}
    
    </Base>
  )
}


export default Signin;