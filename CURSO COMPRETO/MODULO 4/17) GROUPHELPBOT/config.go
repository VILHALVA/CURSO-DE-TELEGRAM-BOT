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
	"os"

	"gopkg.in/ini.v1"
)

// GenerateDefaultConfig Generates and saves the default configuration for the
// correct running of the bot
func GenerateDefaultConfig() *ini.File {
	conf := ini.Empty()

	conf.NewSection("Telegram")
	conf.Section("Telegram").NewKey("token", "<123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11>")

	err := conf.SaveTo("conf/app.ini")
	if err != nil {
		os.Mkdir("./conf", 0755)
		conf.SaveTo("conf/app.ini")
	}

	return conf
}
