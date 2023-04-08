package main

import (
    "fmt"
    "math/rand"
    "time"
)

// Сортировка вставками
func insertionSort(arr []int) {
    for i := 1; i < len(arr); i++ {
        key := arr[i]
        j := i - 1
        for j >= 0 && arr[j] > key {
            arr[j+1] = arr[j]
            j--
        }
        arr[j+1] = key
    }
}

func main() {

    rand.Seed(time.Now().UnixNano())
    arr100 := rand.Perm(100)
    arr1000 := rand.Perm(1000)

//  100
    start := time.Now()
    insertionSort(arr100)
    fmt.Printf("Время работы сортировки вставками для 100 элементов: %s\n", time.Since(start))
// 1000
    start = time.Now()
    insertionSort(arr1000)
    fmt.Printf("Время работы сортировки вставками для 1000 элементов: %s\n", time.Since(start))
}
f
// 1 run
// Время работы сортировки вставками для 100 элементов: 12.664µs
// Время работы сортировки вставками для 1000 элементов: 1.573059ms


// 2 run
// Время работы сортировки вставками для 100 элементов: 12.664µs
// Время работы сортировки вставками для 1000 элементов: 1.573059ms


 // 3 run
// Время работы сортировки вставками для 100 элементов: 11.327µs
// Время работы сортировки вставками для 1000 элементов: 986.005µs
