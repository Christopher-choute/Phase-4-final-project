import React, {useState,useEffect} from "react"
import CarSlot from './CarSlot'

useEffect(() => {
    fetch("localhost")
    .then(res => res.json())
    .then((cars) => manyCars(cars))
  },[]);

function manyCars(cars){
    carData = cars.map((car) => {
        return (
            <CarSlot 
            make={car.make}
            model={car.model}
            year={car.year}
            used={car.new}
            image={car.image}
            />
        );
    });
}

   
function BuyCars(){
    return (
        <div className = 'Cars'>
            {carData}
        </div>
    )
}

export default BuyCars;