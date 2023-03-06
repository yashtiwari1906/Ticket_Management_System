import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { addItemToCart, removeItemFromCart, addTicket } from "./CartHelper";



const SeatHelper = ({ seat }) => {
    
    const seatBooked = seat
        ? seat.booked
        : false
    
    const seatName= seat
    ? "(" + seat.row + "," +seat.col + ")"
    : "Anonymous"
     
    var clicked = false;
    const navigate = useNavigate();
    const addToCart = () => {
       
        addTicket(seat.row, seat.col)
        navigate("/book")
    }
    
    const showButton = (seatBooked) => {
        if (seatBooked){
            return(
                <button type = "button" className="btn btn-danger">{seatName}</button>
            )
        } else {
            if (clicked) {
                return (
                    <button onClick = {addToCart} type = "button" className="btn btn-primary">{seatName}</button>
                    )
            } else {
                return (
                    <button onClick = {addToCart} type = "button" className="btn btn-success">{seatName}</button>
                    )
            }
            
        }
    }

    return (
    <div className="rounded border border-success p-2">
        {showButton(seatBooked)}
    </div>
    );
};

export default SeatHelper;

