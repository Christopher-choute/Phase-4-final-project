import React, {useState,useEffect} from "react";
import Nav from './Nav';
import Header from './Header';
import BuyCars from './BuyCars';


//////HOME COMPONENT///////
//do our requests in here//

function Home(){

    const [carData, setCarData] = useState([]);
    
    useEffect(() => {
        fetch("http://127.0.0.1:5555/cars")
        .then(res => res.json())
        .then((data) => setCarData(data))
      },[]);
    
    console.log(carData);

    return (
        <div>
            <Header />
            <Nav />
            <p>Welcome to New York Customs. Feel free to buy or sell a car.</p>
            <BuyCars cars = {carData} />
        </div>
    )
}

export default Home;