int main() {
	int vector[5] = {10, 20, 30, 40, 50};
	int a = 3;
	int *ptr = &a;
	int *qtr = vector;
}

//         a =  int     3
//        &a = (int*)   0xaf6af5a4f
//        *a =  invalido
//
//       ptr = (int*)   0xaf6af5a4f
//      &ptr = (int**)  0xf987fa6fa
//      *ptr = (int)    3
//
//       qtr = (int*)   0xa987a9faf
//      &qtr = (int**)  0x6567789bc
//      *qtr = int      10
//
//    vector = (int*)   0xa987a9faf
//   &vector = (int(*)[5]) 0xa987a9faf
//   *vector = int      10
//
//     ++qtr = (int*)   0xa987a9fb3
//    ++*qtr = int      11
//
// ++*vector = int      11
//     *&ptr = (int*)   0xaf6af5a4f
