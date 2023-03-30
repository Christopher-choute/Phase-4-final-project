#!/usr/bin/env python3
from random import choice as rc
# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, Dealership, Car, DealershipCar

with app.app_context():

    print("Deleting data...")
    Car.query.delete()
    Dealership.query.delete()
    DealershipCar.query.delete()

    print("Starting seed...")

    print("Creating Cars...")
    car1 = Car(make = "Mazda" ,model = "Miata" ,year = 1990 ,price = 5000 ,used = True ,image= "https://bringatrailer.com/wp-content/uploads/2020/02/1990_mazda_mx-5_miata_158196849730e45558e7262919cIMG_3774.jpg?fit=940%2C627")
    car2 = Car(make = "BMW" ,model = "328i" ,year=2011,price=20000,used=True,image= "https://platform.cstatic-images.com/xlarge/in/v2/stock_photos/83ee8b30-b768-4702-aa2a-13bb4cea96ce/5d28c426-ddea-43a4-9e55-49a237d0a3db.png")
    car3 = Car(make="Nissan",model="Skyline",year=2002,price=100000,used=False,image="https://www.carscoops.com/wp-content/uploads/2021/05/Nissan-GT-R-R34-V-Spec-II-Nur-1a-1024x555.jpg")
    car4 = Car(make="Honda",model="Accord",year=2023,price=27000,used=False,image ="https://cdn.jdpower.com/JDP_2023%20Honda%20Accord%20Blue%20Front%20Quarter%20View.jpg")
    car5 = Car(make="Mercedes",model="CLK500",year=2006,price=6000,used=True,image= "https://www.pcarmarket.com/static/media/uploads/galleries/photos/uploads/galleries/10629-schoenfeld-clk-500/.thumbnails/DSC08465.jpg/DSC08465-tiny-2048x0-0.5x0.jpg") 
    car6 = Car(make="Acura",model="TLX",year=2023,price=39850,used=False,image="https://di-uploads-pod1.dealerinspire.com/motorcarsacura/uploads/2022/07/2207-Acura-Integra-2.jpg")
    car7 = Car(make="Toyota",model="Sienna",year=2022,price=32000,used=True,image="https://www.route22toyota.com/assets/stock/expanded/transparent/1280/2020tov11_1280/2020tov110016_1280_01.png?height=400&bg-color=FFFFFF")
    car8 = Car(make="Rolls-Royce",model="Ghost",year=2022,price=400000,used=False,image= "https://www.motortrend.com/uploads/2021/11/2022-Rolls-Royce-Ghost-Black-Badge-13.jpg")
    car9 = Car(make="Maserati",model="Granturismo",year=2020,price=150000,used=True,image= "https://www.motortrend.com/uploads/izmo/maserati/granturismo/2020/granturismo.png")
    car10 = Car(make="Acura",model="NSX",year=1995,price=82000,used=True,image= "https://platform.cstatic-images.com/xlarge/in/v2/stock_photos/2bb03c01-7037-4635-814d-d71a718585ba/21032315-8b4c-4891-a368-473c40c147fc.png")
    car11 = Car(make="Mercedes",model="AMG Project One",year=2022,price=2000000,used=False,image="https://upload.wikimedia.org/wikipedia/commons/3/3b/Mercedes-AMG_One_at_the_2022_Goodwood_Festival_of_Speed.jpg")
    car12 = Car(make="BMW",model="E36 M3",year=1993,price=24000,used=True,image= "https://images.squarespace-cdn.com/content/v1/5caed8960cf57d49530e8c60/ba57ba87-2b13-4b2c-8fad-a7ca667394a5/art-mg-bmwe36m3gtrstrassenversion05.jpg")
    car13 = Car(make="Nissan",model="370z",year=2020,price=20000,used=True,image= "https://hips.hearstapps.com/hmg-prod/images/370z-project-clubsport-23-2-1540827534.jpg")
    car14 = Car(make="Subaru",model="WRX",year="2015",price=27000,used=False,image= "https://media.ed.edmunds-media.com/subaru/wrx/2015/oem/2015_subaru_wrx_sedan_premium_fq_oem_1_1600.jpg")
    car15 = Car(make="Toyota",model="Prius",year= "2020",price=24000,used=False,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoXYCnLWYsSW2U18hbqMX6O8knVbgQduDbxw&usqp=CAU")
    car16 = Car(make= "Toyota" ,model="Highlander",year= 2008,price=15000,used=True,image="https://www.cars.com/i/large/in/v2/stock_photos/82450349-ba82-43ca-b099-e0eb68bfc592/c860aa29-b734-4ab9-9115-ac0606f023fb.png")
    car17 = Car(make="Honda", model="Civic", year=2018, price=20000, used=False, image="https://static.cargurus.com/images/forsale/2023/03/10/09/22/2018_honda_civic-pic-7210716009479945461-1024x768.jpeg")
    car18 = Car(make="Ford", model="Mustang", year=2010, price=12000, used=True, image="https://images.hgmsites.net/lrg/2010-ford-mustang-2-door-coupe-gt-premium-angular-front-exterior-view_100245369_l.jpg")
    car19 = Car(make="Chevrolet", model="Impala", year=1967, price=40000, used=True, image="https://bringatrailer.com/wp-content/uploads/2022/08/1967_chevrolet_impala_79b9bade-d13f-41ac-893b-8f006be8438d-51348.jpeg?fit=940%2C627")
    car20 = Car(make="Nissan", model="Altima", year=2016, price=16000, used=True, image="https://www.cnet.com/a/img/resize/b482a828335ca707cf7814f98372e295380eed36/hub/2016/05/11/a2043224-f818-41b1-b561-9cb55dfb2384/2016-nissan-altima-sv-6.jpg?auto=webp&width=768")
    car21 = Car(make="BMW", model="i8", year=2016, price=50000, used=True, image="https://cdn.motor1.com/images/mgl/ew9xK/s3/2016-bmw-i8.jpg")
    car22 = Car(make="Audi", model="A4", year=2018, price=28000, used=False, image="https://cars.usnews.com/static/images/Auto/izmo/i62379705/2018_audi_a4_angularfront.jpg")
    car23 = Car(make="Mercedes", model="C300", year=2019, price=35000, used=False, image="https://www.sansoneskia.com/assets/stock/expanded/transparent/640/2017mbc890003_640/2017mbc890003_640_01.png?height=400&bg-color=FFFFFF")
    car24 = Car(make="Lexus", model="ES350", year=2015, price=21000, used=True, image="https://content.homenetiol.com/849/2144166/900x600/37c9a549a8cb4c29aec9c44225888396.jpg")
    car25 = Car(make="Jeep", model="Wrangler", year=2014, price=17000, used=True, image="https://cloudflareimages.dealereprocess.com/resrc/images/c_limit,fl_lossy,w_800/v1/dvp/4162/6020341310/Used-2014-Jeep-WranglerUnlimited-UnlimitedRubicon-ID6020341310-aHR0cDovL2ltYWdlcy51bml0c2ludmVudG9yeS5jb20vdXBsb2Fkcy9waG90b3MvMC8yMDIzLTAzLTIxLzMtMTEzMDI5NjAtNjQxOWQ3N2Q5YzJkZi5qcGc=")
    car26 = Car(make="Subaru", model="Outback", year=2017, price=22000, used=True, image="https://pictures.dealer.com/h/hudsonhyundai/0637/fc282e85b63275abee8a9be7f52a7f59x.jpg?impolicy=resize&w=1024")
    car27 = Car(make="Mazda", model="CX-5", year=2016, price=19000, used=True, image="https://s3.us-east-2.amazonaws.com/dealer-inspire-vps-vehicle-images/1e50-110004279/JM3KFBCM4J0471496/52778e571948474bb87bb1e85ce3955b.jpg")
    car28 = Car(make="Toyota", model="Camry", year=2020, price=26000, used=False, image="https://cloudflareimages.dealereprocess.com/resrc/images/c_limit,fl_lossy,w_400/v1/dvp/2422/5996796599/Used-2020-Toyota-Camry-SE-ID5996796599-aHR0cDovL2ltYWdlcy51bml0c2ludmVudG9yeS5jb20vdXBsb2Fkcy9waG90b3MvMC8yMDIzLTAzLTA3LzEtMjY2MjA1MS02NDA3NGI3M2IxYWIwLmpwZw==")
    car29 = Car(make="Kia", model="Sorento", year=2019, price=24000, used=True, image="https://pictures.dealer.com/h/hudsonhyundai/1165/3a62997e5f4a6045bf77e03d65669a16x.jpg?impolicy=resize&w=1024")
    car30 = Car(make="Hyundai", model="Elantra", year=2013, price=10000, used=True, image="https://cloudflareimages.dealereprocess.com/resrc/images/c_limit,fl_lossy,w_800/v1/dvp/773/6028018076/Used-2013-Hyundai-Elantra-Limited-ID6028018076-aHR0cDovL2ltYWdlcy51bml0c2ludmVudG9yeS5jb20vdXBsb2Fkcy9waG90b3MvMC8yMDIzLTAzLTI0LzItMTE5ODIxMDUtNjQxZTg5N2Q3ZjhhNi5qcGc=")
    
    
    # car31 = Car(make="Volkswagen", model="Jetta", year=2014, price=12000, used=True, image="https://vexgateway.fastly.carvana.io/vex-1601293/spins/3864643/images/234424433.jpg?v=1678307458.437&dpr=2&optimize=low&width=1200")

    cars = [car1,car2,car3,car4,car5,car6,car7,car8,car9,car10,car11,car12,car13,car14,car15,car16,car17,car18,car19,car20,car21,car22,car23,car24,car25,car26,car27,car28,car29,car30]
    
    print("Creating Dealerships...")
    Chouter = Dealership(name = "Chouter", location = "123 Life St" )
    Elsais = Dealership(name = "Elsais", location = "456 Death Ct" )
    Danilovich = Dealership(name = "Danilovich", location = "789 Crazy Ave " )
    Taylor = Dealership(name = "Taylor", location = "135 Silly lane" )
    dealerships = [Chouter, Elsais, Danilovich, Taylor]

    print("Creating DealershipCar...")
    dc1 = DealershipCar(car = car1, dealership = Chouter)
    dc2 = DealershipCar(car= car2, dealership= Elsais)
    dc3 = DealershipCar(car= car3, dealership= Danilovich)
    dc4 = DealershipCar(car= car4, dealership= Taylor)
    dc5 = DealershipCar(car= car5, dealership= Chouter)
    dc6 = DealershipCar(car= car6, dealership= Elsais)
    dc7 = DealershipCar(car= car7, dealership= Danilovich)
    dc8 = DealershipCar(car= car8, dealership= Taylor)
    dc9 = DealershipCar(car= car9, dealership= Chouter)
    dc10 = DealershipCar(car= car10, dealership= Elsais)
    dc11 = DealershipCar(car= car11, dealership= Danilovich)
    dc12 = DealershipCar(car= car12, dealership= Taylor)
    dc13 = DealershipCar(car= car13, dealership= Chouter)
    dc14 = DealershipCar(car= car14, dealership= Elsais)
    dc15 = DealershipCar(car= car15, dealership= Danilovich)
    dc16 = DealershipCar(car= car16, dealership= Taylor)
    dc17 = DealershipCar(car= car17, dealership= Chouter)
    dc18 = DealershipCar(car= car18, dealership= Elsais)
    dc19 = DealershipCar(car= car19, dealership= Danilovich)
    dc20 = DealershipCar(car= car20, dealership= Taylor)
    dc21 = DealershipCar(car= car21, dealership= Chouter)
    dc22 = DealershipCar(car= car22, dealership= Elsais)
    dc23 = DealershipCar(car= car23, dealership= Danilovich)
    dc24 = DealershipCar(car= car24, dealership= Taylor)
    dc25 = DealershipCar(car= car25, dealership= Chouter)
    dc26 = DealershipCar(car= car26, dealership= Elsais)
    dc27 = DealershipCar(car= car27, dealership= Danilovich)
    dc28 = DealershipCar(car= car28, dealership= Taylor)
    dc29 = DealershipCar(car= car29, dealership= Chouter)
    dc30 = DealershipCar(car= car30, dealership= Elsais)


    dc31 = DealershipCar(car = car1, dealership = Danilovich)
    dc32= DealershipCar(car= car2, dealership= Taylor)
    dc33= DealershipCar(car= car3, dealership= Chouter)
    dc34= DealershipCar(car= car4, dealership= Elsais)
    dc35= DealershipCar(car= car5, dealership= Danilovich)
    dc36= DealershipCar(car= car6, dealership= Taylor)
    dc37= DealershipCar(car= car7, dealership= Chouter)
    dc38= DealershipCar(car= car8, dealership= Elsais)
    dc39= DealershipCar(car= car9, dealership= Danilovich)
    dc40 = DealershipCar(car= car10, dealership= Taylor) 
    dc41 = DealershipCar(car= car11, dealership= Chouter)
    dc42 = DealershipCar(car= car12, dealership= Elsais)
    dc43 = DealershipCar(car= car13, dealership= Danilovich)
    dc44 = DealershipCar(car= car14, dealership= Taylor)
    dc45 = DealershipCar(car= car15, dealership= Chouter)
    dc46 = DealershipCar(car= car16, dealership= Elsais)
    dc47 = DealershipCar(car= car17, dealership= Danilovich)
    dc48 = DealershipCar(car= car18, dealership= Taylor)
    dc49 = DealershipCar(car= car19, dealership= Chouter)
    dc50 = DealershipCar(car= car20, dealership= Elsais)
    dc51 = DealershipCar(car= car21, dealership= Danilovich)
    dc52 = DealershipCar(car= car22, dealership= Taylor)
    dc53 = DealershipCar(car= car23, dealership= Chouter)
    dc54 = DealershipCar(car= car24, dealership= Elsais)
    dc55 = DealershipCar(car= car25, dealership= Danilovich)
    dc56 = DealershipCar(car= car26, dealership= Taylor)
    dc57 = DealershipCar(car= car27, dealership= Chouter)
    dc58 = DealershipCar(car= car28, dealership= Elsais)
    dc59 = DealershipCar(car= car29, dealership= Danilovich)
    dc60 = DealershipCar(car= car30, dealership= Taylor)

    dealershipCars = [dc1,dc2,dc3,dc4,dc5,dc6,dc7,dc8,dc9,dc10,dc11,dc12,dc13,dc14,dc15,dc16,dc17,dc18,dc19,dc20,dc21,dc22,dc23,dc24,dc25,dc26,dc27,dc28,dc29,dc30,dc31,dc32,dc33,dc34,dc35,dc36,dc37,dc38,dc39,dc40,dc41,dc42,dc43,dc44,dc45,dc46,dc47,dc48,dc49,dc50,dc51,dc52,dc53,dc54,dc55,dc56,dc57,dc58,dc59,dc60]

    db.session.add_all(cars)
    db.session.add_all(dealerships)
    db.session.add_all(dealershipCars)
    db.session.commit()

    print("Seeding done!...")
    

     
