import React from "react"; 
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";

import Home from "./core/Home"; 
import Seat from "./core/Seat";
import Signin from "./user/Signin";
import Booked from "./user/Booked";
import TicketsByUser from "./user/TicketsByUser";
import UserDetailsOfTicket from "./user/UserDetailsOfTicket";

const AvailRoutes = () => {
    return(
        <Router>
            <Routes>
                <Route path="/" exact element={<Home />} />
                <Route path='/seats' exact element={<Seat />} />
                <Route path='/book' exact element={<Signin />} />
                <Route path='/confirmation' exact element={<Booked />} />
                <Route path='/userDetails' exact element={<UserDetailsOfTicket />} />
                <Route path='/userTickets' exact element={<TicketsByUser />} />
            </Routes>
        </Router>
    );
}


export default AvailRoutes;