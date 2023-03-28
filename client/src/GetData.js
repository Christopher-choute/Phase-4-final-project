import React, {useState,useEffect} from "react";
import BuyCars from './BuyCars';


//////HOME COMPONENT///////
//do our requests in here//

function GetData(){

    const [carData, setCarData] = useState([]);
    
    useEffect(() => {
        fetch("http://127.0.0.1:5555/cars")
        .then(res => res.json())
        .then((data) => setCarData(data))
      },[]);
    
    console.log(carData);

    return (
        <div>
            <BuyCars cars = {carData} />
        </div>
    )
}

export default GetData;