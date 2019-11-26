from conans import ConanFile, tools
import os


class CesiumConan(ConanFile):
	name = "cesium"
	version = "1.63.1"
	license = "Apache-2.0"
	url = "https://cesium.com/cesiumjs"
	description = "An open-source JavaScript library for world-class 3D globes and maps"
	settings = "build_type"
	options = {}
	default_options = {}
	no_copy_source = True

	def source(self):
		tools.get("https://github.com/AnalyticalGraphicsInc/cesium/releases/download/%s/Cesium-%s.zip" % (self.version, self.version))

	def build(self):
		pass

	def package(self):
		binName = "CesiumUnminified" if self.settings.build_type == "Debug" else "Cesium"
		self.copy("*", dst=os.path.join("bin", "cesium"), src=os.path.join("Build", binName))
		self.copy("*", dst="docs", src=os.path.join("Build", "Documentation"))
		self.copy("LICENSE.md", dst="license")

	def package_info(self):
		self.cpp_info.libs = []
