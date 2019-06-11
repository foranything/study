# OOP
___

### object literal

``` javascript
var lamp = {
  brightness: 0,
  turnOn: function () {
    this.brightness = 100;
  },
  turnOff: function () {
    this.brightness = 0;
  }
};

lamp.turnOn();
lamp.turnOff();
lamp.brightness = 5000;
```
___

### Encapsulation

외부에서 내부 속성을 허용하지 않음

``` javascript

var lamp = (function () {
  // Encapsulated
  var brightness = 0;

  return {
    turnOn: function () {
      brightness = 100;
    },
    turnOff: function () {
      brightness = 0;
    }
  };
})();

lamp.turnOn();
lamp.turnOff();
// lamp.brightness = 5000;

```

___

### Abstraction

자주 쓰는 기능 모듈화
___
### Inheritance

``` javascript
function Car (owner) {
  this.owner = owner;
}

Car.prototype.soldTo = function (newOwner) {
  this.owner = newOwner;
};

var mycar = new Car('A'); //{owner: "A"}

mycar.soldTo('B'); //{owner: "B"}

//Car를 상속함
function ElectricCar (owner) {
  Car.call(this, owner);

  this.power = 0;
}

var mycar = new ElectricCar('A'); //{owner: "A", power: 0}

ElectricCar.prototype = Object.create(Car.prototype);
ElectricCar.prototype.constructor = ElectricCar;

ElectricCar.prototype.recharge = function (time) {
  var that = this;

  setTimeout(function () {
    that.power = Math.min((time / 100), 100);
  }, time);
};

var mycar = new ElectricCar('A'); //{owner: "A", power: 0}
mycar.recharge(1000) // {owner: "A", power: 10}


```

``` javascript
obj2 = Object.create(obj1)
//obj2.__proto__ 가 obj1인 객체를 생성

```


