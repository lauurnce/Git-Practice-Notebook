package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("How many layers of pyramid do you want? ")
    input, _ := reader.ReadString('\n')
    input = strings.TrimSpace(input)

    n, err := strconv.Atoi(input)
    if err != nil || n <= 0 {
        fmt.Println("Please enter a positive integer.")
        return
    }

    for i := 1; i <= n; i++ {
        spaces := strings.Repeat(" ", n-i)
        stars := strings.Repeat("*", 2*i-1)
        fmt.Println(spaces + stars)
    }
}