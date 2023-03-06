import React, {useState, useEffect} from "react"; 
import Base from "./Base";
import "../style.css";
import { getSeats } from "./helper/coreapicalls";
import SeatHelper from "./helper/SeatHelper";


export default function Seat() {


    const [seats, setSeats] = useState([]);
    const [error, setError] = useState(false);
  
    const loadAllSeats = () => {
      getSeats()
        .then((data) => {
            
          if (data.error) {
            setError(data.error);
            console.log(error);
          } else {
            setSeats(data);
          }
        });
    };
  
    useEffect(() => {
        loadAllSeats();
      }, []);

    function getEvent() {
      var EventName = "";
      if(typeof window !=undefined){
        if(localStorage.getItem("EventName")){
          EventName=JSON.parse(localStorage.getItem("EventName"))
        }

        return EventName
    }}
      
    return (
        <Base title ="Home Page" description="Ticket Management System">
            <h2>Current Shows</h2>

            <div className="row">
                {seats.map((seat,index)=>{
                  
                  if (getEvent() === seat.event) {
                    return (
                        <div key={index} className="col-1 mb-4">
                          <SeatHelper seat={seat}/>
                         </div>   
                    )
                  }
                    
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

