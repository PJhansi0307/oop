class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        
        if self._max_speed<0:
            raise ValueError("Invalid value for max_speed")
            
        if self._tyre_friction<0:
            raise ValueError("Invalid value for max_speed")
            
        if self._acceleration<0:
            raise ValueError("Invalid value for max_speed")
        
        self._color=color
        self._current_speed=0
        self._is_engin_started=False 
    @property
    def color(self):
        return self._color
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def current_speed(self):
        return self._current_speed
    @property
    def start_engine(self):
        self._is_engine_started=True
        return self._is_engine_started
    @property
    def accelerate(self):
        if(self._is_engine_started==True):
            if(self._current_speed+self._acceleration<=self._max_speed):
                self._current_speed+=self._acceleration
            
        else:
            print("Start the engine to accelerate")
    @property
    def apply_brakes(self):
        if(self._current_speed-self._tyre_friction>=0):
            self._current_speed-=self._tyre_friction
        else:
            self._current_speed=0
    @property    
    def sound_horn(self):
        if(self._is_engin_started==True):
            print("\"Beep Beep\"")
        else:
            print("Start the engine to sound_horn")
    @property
    def stop_engine(self):
        self._is_engine_started=False
        self._current_speed=0
        return self._is_engine_started
            