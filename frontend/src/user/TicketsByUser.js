import { getDefaultNormalizer } from '@testing-library/react';
import React, { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom';
import Base from "../core/Base";
import { Tickets } from './helper/index';




const TicketsByUser = () => {
    const navigate = useNavigate();
    const [values, setValues]=  useState({
        name: "",
        email:"",
        contact:"", 
        error: "",
        success: false,
    });
    
    const [tickets, setTickets] = useState([])
    const {name, email, contact, error, success} = values;

    const handleChange = name => event_case => {
        setValues({...values,error: false, [name]: event_case.target.value})
    }

    const getTickets = () =>{
        console.log("we entred value for succes is ", success, tickets)
        if (success) {
            return (
            tickets.map((ticket,index)=>{
                console.log("yep in loop")
                return (
                    <div className='col-md-12 text-center'>
                        <button className="btn btn-primary"> {ticket} </button>
                    </div>
                    
                )
            })
            );
        }
        
    }

    
    
    const onSubmit=(event_case)=>{
        
        event_case.preventDefault();
        setValues({...values, error: false})
        Tickets({name,email,contact})    // replace 1 and 5 with (row, col)
        .then((data)=> {
            console.log("DATA", "-------", data);
            if(data.success){
                setTickets(data.tickets)
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
                    <div className="alert-success" style={{display: success ? "" : "none" }}>
                        Ticket fetched successfully.
                       
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
                        Please Enter valid Credentials.
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
    {signUpForm()}
    {getTickets()}
    
    
    </Base>
  )
}


export default TicketsByUser;