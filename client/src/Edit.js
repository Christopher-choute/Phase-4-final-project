import React, {useState ,useEffect} from "react";
import {useHistory ,useParams} from "react-router-dom"
import {Form, Button} from"semantic-ui-react"
import './Edit.css'

function Edit({updateCar}){
    const { id } = useParams();
    const history = useHistory();
    const [make, setMake] = useState("");
    const [model, setModel] = useState("");
    const [price, setPrice] = useState("");
    const [year, setYear] = useState("");
    const [image, setImage] = useState("");
    const [used, setUsed] = useState(false);
    const [val, setVal] = useState("");
    const [isLoading, updateIsLoading] = useState(false);
    const [car, setCar] =useState([]);

    // console.log(id)

    function handleMake(make) {
        setMake(make.target.value);
      }

    function handleYear(year) {
        setYear(year.target.value);
      }

    function handleImage(image) {
        setImage(image.target.value);
      }

    function handlePrice(price) {
        setPrice(price.target.value);
      }
      
    

    function handleModel(model) {
        setModel(model.target.value);
      }

    function handleUsed(val) {
        setVal(val.target.value);
    
        // if (val === "New" || val === "new"){
        //     setUsed(false);
        // }
        // else if (val === "Used" || val === "used"){
        //     setUsed(true);
        // }
        // else {
        //     const e = new Error('Has to be "Used" or "New"');
        // }
    }

    

    function handlePatch(id){
        fetch(`/cars/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({make: make, model: model, year: year, price: price, image: image, used: used}),
        }).then((res) => {
            if (res.ok) {
                res.json().then(updatedCar => {
                    updateCar(updatedCar)
                    history.push(`/cars`)
                })
            }
        })
      }
      
    useEffect(() => {
        fetch(`/cars/${id}`)
            .then(r => r.json())
            .then(car => {
                setMake(car.make)
                setModel(car.model)
                setPrice(car.price)
                setYear(car.year) 
                setImage(car.image)
                setUsed(car.used)
            })
    }, [])
    
    
    return (
            <Form onSubmit={() => handlePatch(id)} style={{ maxWidth: '1000px' }}>
            <h3 id ="form-title">Edit The Car!</h3>
            <Form.Field>
                <label>Make: </label>
                <input
                    type="text"
                    name="make"
                    placeholder="Enter the make of the car"
                    className = "input-text"
                    onChange = {handleMake}
                    value = {make}
                />
            </Form.Field>
            <Form.Field>
            <label>Model: </label>
            <input
                type="text"
                name = "model"
                placeholder="Enter the model of the car"
                className = "input-text"
                onChange = {handleModel}
                value = {model}
            />
            </Form.Field>
            <Form.Field>
                <label>Price: </label>
                <input
                    type="text"
                    name = "price"
                    placeholder="Enter the price of the car"
                    className = "input-text"
                    onChange = {handlePrice}
                    value = {price} 
                />
            </Form.Field>
            <Form.Field>
                <label>Year: </label>
                <input
                    type="text"
                    name = "year"
                    placeholder="Enter the year of the car"
                    className = "input-text"
                    onChange = {handleYear}
                    value = {year}
                />
            </Form.Field>
            <Form.Field>
                <label>Image URL:</label>
                <input
                    type = "text"
                    name = "image"
                    placeholder="Enter the Car's URL"
                    className = "input-text"
                    onChange = {handleImage}
                    value = {image}
                />
            </Form.Field>
            <Form.Field>
                <label>New or Used:</label>
                <input 
                    type = "text"
                    name = "used"
                    placeholder="Is your car 'New' or 'Used' "
                    className = "input-text"
                    onChange = {handleUsed}
                    value = {val}
                />
            </Form.Field>
            <input type="submit" />
        </Form>
    );
}

export default Edit;