import { getDefaultNormalizer } from '@testing-library/react';
import React, { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom';
import Base from "../core/Base";
import { userDetailsFetch } from './helper/index';




const UserDetailsOfTicket = () => {
    const navigate = useNavigate();
    const [details, setDetails] = useState({
        name: "", 
        email: "",
        contact: ""
    })
    const {name, email, contact} = details;
    const [values, setValues]=  useState({
        ticket: "",
        error: "",
        success: false,
    });
    
    
    const {ticket, error, success} = values;

    const handleChange = name => event_case => {
        setValues({...values,error: false, [name]: event_case.target.value})
    }
    

    const displayDetails = () => {
        if (success) {
            return (
            <div className='col-md-12 text-center'>
                <button className="btn btn-warning"> name: {name} </button>
                <button className="btn btn-warning"> email: {email} </button>
                <button className="btn btn-warning"> contact: {contact} </button>
            </div>
            
            
            )
        }
    }

    
    
    const onSubmit=(event_case)=>{
        
        event_case.preventDefault();
        setValues({...values, error: false})
        console.log("ticket is ", ticket)
        userDetailsFetch({ticket})    // replace 1 and 5 with (row, col)
        .then((data)=> {
            console.log("DATA", "-------", data);
            if(data.success){
                setDetails({
                    name: data.details.name, 
                    email: data.details.email, 
                    contact: data.details.contact
                })
                setValues({
                    ...values,
                    error: false,
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
                    <div className="alert alert-success" style={{display: success ? "" : "none" }}>
                        Details fetched successfully.
                       
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
                        Please Enter a valid Ticket.
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
                              Ticket 
                          </label>
                          <input type="text"
                          className="form-control"
                          values={ticket}
                          onChange={handleChange("ticket")}/>
                      </div>
                    
                      <button onClick={onSubmit} className="btn btn-success btn-block">Submit</button>
                    </form>

                </div>
            </div>    
        )
    }
    
  return (
    <Base title = "User Details" description = "Enter Ticket and get Information of User">
    {successMessage()}
    {errorMessage()}
    {signUpForm()}
    {displayDetails()}
    
   
    </Base>
  )
}


export default UserDetailsOfTicket;