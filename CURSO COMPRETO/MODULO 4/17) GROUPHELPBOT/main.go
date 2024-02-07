/* RinTinTin - a better GroupHelpBot for your network
Copyright (C) 2020 - Bryan Pedini

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>. */

package main

import (
	"fmt"
	"log"

	"gopkg.in/ini.v1"
)

func main() {
	config, err := ini.Load("conf/app.ini")

	if err != nil {
		log.Println("No config file found, generating default config...")
		config = GenerateDefaultConfig()
	}

	telegramToken := config.Section("Telegram").Key("token")

	// Debug:
	fmt.Println(telegramToken)
}
