import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import "./Components/Productos";
import Productos from "./Components/Productos";

const diccionario = {
  Polera: {
    Product: "Polera",
    values: ["SKU1", "SKU2", "SKU3", "Ripley", "Paris", "Falabella"],
    min_value: 2500,
    max_value: 5500,
    num_distinct_markets: 3,
    EAN: "EAN1",
  },
  Jeans: {
    Product: "Jeans",
    values: ["SKU5", "SKU4", "Ripley", "Falabella"],
    min_value: 4000,
    max_value: 7000,
    num_distinct_markets: 2,
    EAN: "EAN2",
  },
  camisa: {
    Product: "camisa",
    values: ["SKU6", "Ripley"],
    min_value: 4000,
    max_value: 6000,
    num_distinct_markets: 1,
    EAN: "EAN3",
  },
  Falda: {
    Product: "Falda",
    values: ["SKU7", "Falabella"],
    min_value: 6000,
    max_value: 9000,
    num_distinct_markets: 1,
    EAN: "EAN4",
  },
};

const App = () => {
  const [inputValue, setInputValue] = useState("");
  const [data, setData] = useState(diccionario);
  const [bool, setBool] = useState(false);

  const moverAlPrincipio = (clave) => {
    setData((prevData) => {
      const nuevoData = { [clave]: prevData[clave], ...prevData };
      return nuevoData;
    });
  };

  const onSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim().length >= 1) {
      setBool(true);
    }
  };

  useEffect(() => {
    const intervalId = setInterval(() => {
      if (inputValue !== "" && bool) {
        moverAlPrincipio(inputValue);

        // setData((prevProducts) => {
        //   if (prevProducts.length > 1) {
        //     return prevProducts.slice(0, -1);
        //   } else {
        //     return prevProducts;
        //   }
        // });
      }
    }, 1000);

    return () => clearInterval(intervalId);
  }, [inputValue]);

  const onInputChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
    <form onSubmit={(e) => onSubmit(e)}>
      <input
        type="text"
        placeholder="Filtrar por nombre"
        value={inputValue}
        onChange={onInputChange}
      ></input>
      <div>
        {Object.keys(data).map((key) => (
          <Productos key={key} data={data[key]}></Productos>
        ))}
      </div>
    </form>
  );
};

export default App;
