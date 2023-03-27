import React, {useState,useEffect} from "react"

function carUsed(used)
    return 

function CarSlot(make, model, year, used, image){
    return (
        <div>
            <div>
                <p>{image}</p>
                <p>Make: {make}</p>
                <p>Model: {model}</p>
                <p>Year: {year}</p>
                <p>Condition: {used ? 'This Car is Used' : "This Car is Brand New"}</p>
            </div>
        </div>
    )
}

export default CarSlot;