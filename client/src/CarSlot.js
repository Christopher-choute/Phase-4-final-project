import React from "react";
import './CarSlot.css'
/////Car Slot (list) Component ////////
function CarSlot({make, model, price, year, used, image}){
    return (
        <div className = "carslot">
            <img className ="Image" src = {image} alt = {make} />
            <p>Make: {make}</p>
            <p>Model: {model}</p>
            <p>Price: ${price}</p>
            <p>Year: {year}</p>
            <p>Condition: {used ? 'This Car is Used' : "This Car is Brand New"}</p>
        </div>
    );
}

export default CarSlot;