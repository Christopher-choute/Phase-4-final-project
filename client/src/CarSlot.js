import React from "react";
import './CarSlot.css'
import { Link } from "react-router-dom"
/////Car Slot (list) Component ////////
function CarSlot({id, make, model, price, year, used, image}){
    const linkStyle= { 
        textDecoration: "none"
    }
    
    return (
        <div className = "carslot" ><Link to={`cars/${id}` } style={linkStyle}>
            <img className ="Image" src = {image} alt = {make} />
            <p>Make: {make}</p>
            <p>Model: {model}</p>
            <p>Price: ${price}</p>
            <p>Year: {year}</p>
            <p>Condition: {used ? 'This Car is Used' : "This Car is Brand New"}</p>
            </Link>
            <Link to={`/edit/${id}`} style={linkStyle} ><button>Edit</button></Link>
        </div>
    );
}

export default CarSlot;
