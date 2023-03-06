import React, {useState, useEffect} from "react"; 
import Base from "./Base";
import "../style.css";
import Card from "./Card";
import { getEvents } from "./helper/coreapicalls";

export default function Home() {


    const [events, setEvents] = useState([]);
    const [error, setError] = useState(false);
  
    const loadAllEvents = () => {
      getEvents()
        .then((data) => {
            console.log("+++++++")
            console.log(data)
            console.log("+++++++")
          if (data.error) {
            setError(data.error);
            console.log(error);
          } else {
            setEvents(data);
          }
        });
    };
  
    useEffect(() => {
        loadAllEvents();
      }, []);



    return (
        <Base title ="Home Page" description="Ticket Management System">
            <h2>Current Shows</h2>
            <div className="row">
                {events.map((event,index)=>{
                    return (
                        <div key={index} className="col-4 mb-4">
                          <Card event={event}/>
                         </div>   
                    )
                })}
            </div>
        </Base>
    )
}



// </div>
//                     <div className="col-6 mb-4">
//                         <Card />
//                     </div>
//                     <div className="col-6 mb-4">
//                         <Card />
//                     </div>
//             </div>



