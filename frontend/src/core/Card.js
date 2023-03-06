import React from 'react'
import ImageHelper from './helper/ImageHelper';
import { Link, useNavigate } from 'react-router-dom';

const Card = ({
    event
}) => {

    const CardTitle = event ? event.event_name : "A photo from pexels"
    const CardDescription = event ? event.description : "default description"

    const navigate = useNavigate();

    const getAredirect = () => {
      addEventName(event.event_name)
      navigate("/seats")
      
    }

    const addEventName =(item) =>{
      let EventName  = ""
      console.log("event name added", item)
      if(typeof window !=undefined){
          if(localStorage.getItem("EventName")){
            EventName=JSON.parse(localStorage.getItem("EventName"))
          }
          localStorage.setItem("EventName",JSON.stringify(""));
          EventName = item;
          localStorage.setItem("EventName",JSON.stringify(EventName));
          
      }
  };

    return (
      <div className="card text-white bg-dark border border-info ">
        <div className="card-header lead">{CardTitle}</div>
        <div className="card-body">
          <div className="rounded border border-success p-2">
            <ImageHelper event = {event}/>
          </div>
          <p className="lead bg-success font-weight-normal text-wrap">
            {CardDescription}
          </p>
          <p className="btn btn-success rounded  btn-sm px-4">tickets booked: {event.tickets_booked}</p>
          <p className="btn btn-danger rounded  btn-sm px-4"> tickets left: {event.tickets_left}</p>
          <div className="row">
            <div className="col-12">
              <button
                onClick={getAredirect}
                className="btn btn-block btn-outline-success mt-2 mb-2"
              >
                BooK Tickets
                
               
              </button>
            </div>
           
          </div>
        </div>
      </div>
    );
  };

export default Card;