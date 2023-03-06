import React from 'react';
import { Link } from 'react-router-dom'; 


const currentTab = (history, path) => {
    if (history.location.pathname === path){
        return {color: "#2ecc72"}
    } else {
        return {color: "#FFFFFF"}
    }
}; 

const Menu =({history, path}) => {
    
  return (
    <div>
    <ul className="nav nav-tabs bg-dark">
        <li className="nav-item">
            <Link 
                
                className = "nav-link"
                to="/"
            >
            HOME
            </Link>
        </li>
        <li className="nav-item">
            <Link 
               
                className = "nav-link"
                to="/userDetails"
            >
            User Details
            </Link>
        </li>
        <li className="nav-item">
            <Link 
                
                className = "nav-link"
                to="/userTickets"
            >
            Tickets
            </Link>
        </li>
    </ul>
    </div>
  )
}

export default Menu;
