import React, {useState,useEffect} from "react"
import Nav from './Nav'
import Header from './Header'





function Home(){
    return (
        <div>
            <Header />
            <Nav />
            <p>Welcome to New York Customs. Feel free to buy or sell a car.</p>
        </div>
    )
}

export default Home;