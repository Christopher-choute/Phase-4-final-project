import React from "react";

/////Car Slot (list) Component ////////
function CarSlot({make, model, year, used, image}){
    return (
        <li>
            <img src = {image} />
            <p>Make: {make}</p>
            <p>Model: {model}</p>
            <p>Year: {year}</p>
            <p>Condition: {used ? 'This Car is Used' : "This Car is Brand New"}</p>
        </li>
    );
}

export default CarSlot;