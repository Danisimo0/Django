package main

import (
	"database/postgresql"
	"fmt"
	"log"
	"os"

	"github.com/gin-gonic/gin"

)

func main() {
	 
	file, err := os.OpenFile("logs.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		log.Fatal("Ошибка открытия файла журнала:", err)
	}
	defer file.Close()

 
	log.SetOutput(file)

 
	db, err := sql.Open("postgresql", "postgres:Gosamu11@tcp(localhost:5432)/postgres")
	if err != nil {
		log.Fatal("Ошибка подключения к базе данных:", err)
	}
	defer db.Close()
 
	err = db.Ping()
	if err != nil {
		log.Fatal("Ошибка проверки соединения с базой данных:", err)
	}

	 
	router := gin.Default()

 
	router.GET("/data", func(c *gin.Context) {
		rows, err := db.Query("SELECT * FROM your_table")
		if err != nil {
			log.Println("Ошибка выполнения запроса:", err)
			c.JSON(500, gin.H{"message": "Ошибка выполнения запроса"})
			return
		}
		defer rows.Close()

	 
		for rows.Next() {
			var id int
			var name string
			err := rows.Scan(&id, &name)
			if err != nil {
				log.Println("Ошибка чтения данных из результата запроса:", err)
				c.JSON(500, gin.H{"message": "Ошибка чтения данных"})
				return
			}
	 
			fmt.Println(id, name)
		}

		c.JSON(200, gin.H{"message": "Данные успешно получены"})
	})

 
	router.Run(":8080")
}
