const Productos = ({ data }) => {
  return (
    <>
      <h1>Nombre de Producto: {data.Product}</h1>
      <hr></hr>
      <h2>Valor Maximo: {data.max_value}</h2>
      <hr></hr>
      <h2>Valor minimo: {data.min_value}</h2>
      <hr></hr>
      <h2>Cantidad de mercados distintos: {data.num_distinct_markets}</h2>
    </>
  );
};

export default Productos;
