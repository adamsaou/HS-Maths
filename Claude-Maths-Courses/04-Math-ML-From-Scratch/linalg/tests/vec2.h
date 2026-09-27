#pragma once


#include <cmath>

struct Vect2 { double x, y; };

inline Vect2 add(Vect2 a, Vect2 b){

    return { a.x + b.x, a.y + b.y };

}

inline Vect2 subtract(Vect2 a, Vect2 b){
    return { a.x - b.x, a.y - b.y };
}

inline Vect2 scale(Vect2 a, double c){
    return { a.x * c, a.y * c };
}

inline Vect2 norm(Vect2 a){
    return { std::sqrt((a.x) * (a.x)) + std::sqrt((a.y) * (a.y)) };
}

inline Vect2 normalize(){
    return {  };
}