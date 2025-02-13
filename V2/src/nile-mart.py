

DELIVERY_MAP_CONFIG = 'M01-W01-04-Project-Assessment-Nile-Mart (1)/M01-W01-04-Project-Assessment-Nile-Mart/v2/config/delivery_map.txt'
ORDER_BATCH_CONFIG = 'M01-W01-04-Project-Assessment-Nile-Mart (1)/M01-W01-04-Project-Assessment-Nile-Mart/v2/config/order_batch.txt'

#Class Order ​stores details of an individual order, and triggers delivery via a route  
class Order:
    def __init__(self, id, item_name, customer, order_date, city, delivery_date, delivery_type):
        self._id = id
        self._item_name = item_name
        self._customer = customer
        self._order_date = order_date
        self._city = city
        self._delivery_date = delivery_date
        self._delivery_type = delivery_type

    def __str__(self):
        return f'ID - {self.id}, Item Name - {self.item_name}, Order Date - {self.order_date}, Customer - {self.customer}, City - {self.city}, Delivery Date - {self.delivery_date}, Delivery Type - {self.delivery_type}'

    @property
    def id(self):
        return self._id

    @property
    def item_name(self):
        return self._item_name

    @property
    def order_date(self):
        return self._order_date

    @property
    def customer(self):
        return self._customer

    @property
    def city(self):
        return self._city

    @property
    def delivery_date(self):
        return self._delivery_date

    @property
    def delivery_type(self):
        return self._delivery_type
        
    def dispatch(self, delivery_route):
        print(f'Dispatching order {order}')
        delivery_route.process_order(self)

#Class OrderBatch ​parses order information from ​order_batch.txt​ and creates order objects
class OrderBatch:
    def __init__(self):
        self._order_batch = []

    def __str__(self):
        pass
    # Using read_config function: Read order_batch.txt file 
    # read each order details line by line , spilt the details of each order bases on'-' delimeter and store it in a list (order_details)
    # Calls order class and pass the order details.
    # Stores the order details in Order_batch List
    def read_config(self, order_batch_config):
        with open(order_batch_config, 'r') as obatch_file:
            obatch_lines = [obatch_line.rstrip() for obatch_line in obatch_file]

        for order_entry in obatch_lines:
            order_details = order_entry.split('-')
            order = Order(order_details[0], order_details[1], order_details[2], order_details[3], order_details[4], order_details[5], order_details[6])  

            self._order_batch.append(order)

    def get_orders(self):
        return self._order_batch
#Class DeliveryMap :  Reads delivery_map.txt file  and  fetch list of destination in the file and route map details
class DeliveryMap:
    def __init__(self):
        self._destinations = []
        self._delivery_map = {}
        self._delivery_type = []

    def __str__(self):
        pass
    # Using read_config function: Read delivery_map.txt file 
    # read each route details, spilt the details of each delivery reoute based on ' ' delimeter and store spilt result destination  and stages
    # Again we split stages based on ',' and get all reoute details or delivery stages
    # Store the details in a dictionary with Key as destination and value as stages
    # Print all destinations
    

    def read_config(self, delivery_map_config):
        with open(delivery_map_config, 'r') as dmap_file:
            dmap_lines = [dmap_line.rstrip() for dmap_line in dmap_file]


        for line in dmap_lines:
            destination,delivery_type,stages = line.split(" ",2)
            
            self._destinations.append(destination)
           
            stages = stages.split(',')
            self._delivery_map[destination] = stages,delivery_type
        print(f'Destinations: {self._destinations}')

    def get_destinations(self):
        return self._destinations 
    def get_delivery_type(self):
        return self._delivery_type

    def routing_map(self):
        return self._delivery_map

    def get_stages(self, delivery_center):
        return self._delivery_map[delivery_center]
    

# Class DeliveryStage :  Gives us details of delivery stage based on the source and destination
class DeliveryStage:
    def __init__(self, source, destination):
        self._source = source
        self._destination = destination
        self._next_stage = None

    @property
    def next_stage(self):
        return self._next_stage

    @next_stage.setter
    def next_stage(self, successor):
        self._next_stage = successor

    def process_order(self, order):
        pass



class TrainDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)

    def __str__(self):
        return f'Train from {self._source} to {self._destination}'
    
    
    def process_order(self, order):
        print(f'Order {order.id} - Train Dispatch from {self._source} to {self._destination}')

        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 


class FlightDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)
    
    def __str__(self):
        return f'Flight from {self._source} to {self._destination}'
    
    
    def process_order(self, order):
        print(f'Order {order.id} - Flight Dispatch from {self._source} to {self._destination}')

        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 


class TruckDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)

    def __str__(self):
        return f'Truck from {self._source} to {self._destination}'
        
    def process_order(self, order):
        print(f'Order {order.id} - Truck Dispatch from {self._source} to {self._destination}')

        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 

class BoatDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)

    def __str__(self):
        return f'Boat from {self._source} to {self._destination}'
        
    def process_order(self, order):
        print(f'Order {order.id} - Boat Dispatch from {self._source} to {self._destination}')

        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 
            
class ShipDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)

    def __str__(self):
        return f'Ship from {self._source} to {self._destination}'
        
    def process_order(self, order):
        print(f'Order {order.id} - Ship Dispatch from {self._source} to {self._destination}')

        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None            
#DeliveryRoute ​class holds the structured route to a destination, with several stage

class DeliveryRoute:
    def __init__(self, stage_list, destination):
        self._stage_list = stage_list
        self._destination = destination
        

    def __str__(self):
        route = ','.join(str(stage) for stage in self._stage_list)
        return f'Route to {self._destination} : {route}\n'
        

    def process_order(self, order):
        self._stage_list[0].process_order(order)

#DeliverySystem ​uses DeliveryMap to create usable routes to all destinations
class DeliverySystem:
    def __init__(self):
        self.delivery_centers = []
        self.stage_routes = {}
        self.delivery_type =[]
    #Pouplating route based on center and stages
    def populate_route(self, center, stages):
        stage_list = []
        for stage in stages:
            source, dispatch_method, destination = stage.split('-')
            if (dispatch_method == 'truck'):
                stage_list.append(TruckDispatch(source, destination))
            elif (dispatch_method == 'train'):
                stage_list.append(TrainDispatch(source, destination))
            elif (dispatch_method == 'flight'):
                stage_list.append(FlightDispatch(source, destination))
            elif (dispatch_method == 'Boat'):
                stage_list.append(BoatDispatch(source, destination))
            elif (dispatch_method == 'Ship'):
                stage_list.append(ShipDispatch(source, destination))
        
        for i in range(0, len(stage_list) - 1):
            stage_list[i].next_stage = stage_list[i+1]
        
        route = DeliveryRoute(stage_list, destination)
        print(route)

        return route
    # Creates and triggers DeliveryMap to ingest destination and stage information
    def configure(self, DELIVERY_MAP_CONFIG):
        delivery_map = DeliveryMap()
        delivery_map.read_config(DELIVERY_MAP_CONFIG)

        self.delivery_centers.extend(delivery_map.get_destinations())
        self.delivery_type.extend(delivery_map.get_delivery_type())

        for center in self.delivery_centers:
            stages = delivery_map.get_stages(center)
            route = self.populate_route(center, stages[0])
            self.stage_routes[center] = route

    def get_route(self, destination,delivery_type):
            return self.stage_routes[destination,delivery_type]

        
# Client Context

normal_delivery_system = DeliverySystem()
normal_delivery_system.configure(DELIVERY_MAP_CONFIG)

premium_delivery_system = DeliverySystem()
premium_delivery_system.configure(DELIVERY_MAP_CONFIG)

order_batch = OrderBatch()
order_batch.read_config(ORDER_BATCH_CONFIG)

orders = order_batch.get_orders()

for order in orders:
    if (order.delivery_type == 'Normal'):
        route = normal_delivery_system.get_route(order.city,order.delivery_type)
    elif (order.delivery_type == 'Premium'):
        route = premium_delivery_system.get_route(order.city)
    order.dispatch(route)
    print('\n')