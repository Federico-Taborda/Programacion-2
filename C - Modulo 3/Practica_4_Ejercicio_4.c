struct pack3 {
    int a;
};

struct pack2 {
    int b;
    struct pack3 *next;
};

struct pack1 {
    int c;
    struct pack2 *next;
};

int main(){
    struct pack1 data1 , *dataPtr;
    struct pack2 data2;
    struct pack3 data3;
    data1.c = 30;
    data2.b = 20;
    data3.a = 10;
    dataPtr = &data1;
    data1.next = &data2;
    data2.next = &data3;
    return 1;
}

/* 
data1.c:                correcto -> salida:30
dataPtr->c:             correcto -> salida:30
dataPtr.c:              incorrecto
data1.next->b:          correcto -> salida: 20
dataPtr->next->b:       correcto -> salida: 20
dataPtr.next.b          incorrecto
dataPtr->next.b         incorrecto
(*(dataPtr->next)).b    correcto -> salida: 20
data1.next->next->a     correcto -> salida: 10
dataPtr->next->next.a   correcto -> salida: 10
dataPtr->next->next->a  incorrecto
dataPtr->next->a        incorrecto
dataPtr->next->next->b  incorrecto
 */