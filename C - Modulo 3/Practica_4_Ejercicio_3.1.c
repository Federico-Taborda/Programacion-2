int vector [5] = {10, 20, 30, 40, 50};

#define SIZE 100

/* Informacion sobre la celda */
struct informacionCelda {
   char nombre[SIZE]; // nombre de la celda
   int identificador; //número identificador
   float calidad; // calidad de la señal (entre 0 y 100)
   struct informacionOp* op; // puntero a una segunda estructura
};

struct informacionOp {
    char nombre[SIZE]; // nombre del operador
    int prioridad; // prioridad de conexión
    int ultimaComprobacion; //fecha de la ultima comprobación
};
