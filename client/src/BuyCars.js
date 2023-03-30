import React, {useState} from "react";
import CarSlot from './CarSlot';

 
function BuyCars({cars}){


    const carList = cars.map((car) => {
        return (
            <CarSlot
            key = {car.id}
            id = {car.id}
            make = {car.make}
            model = {car.model}
            year = {car.year}
            price = {car.price}
            used = {car.used}
            image = {car.image}
            /> 
            
        )
    })

    
    return (
        
        <ul className = "cars">{carList}</ul>     
    );
}

export default BuyCars;