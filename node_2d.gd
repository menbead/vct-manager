extends Node2D

# useful python -> godot tutorial:
# https://www.youtube.com/watch?v=z2MHuWEDUNw
var DIR = OS.get_executable_path().get_base_dir()
var interpreter_path = DIR.path_join("PythonFiles/venv/Scripts/python.exe")
var script_path = DIR.path_join("PythonFiles/vlr.py")
var player

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	if not OS.has_feature("standalone"): # if NOT exported version
		interpreter_path = ProjectSettings.globalize_path("res://PythonFiles/venv/Scripts/python.exe")
		script_path = ProjectSettings.globalize_path("res://PythonFiles/vlr.py")
	
	print(get_player(4))

func get_player(playerId=0) -> String:
	var output = []
	var exit_code = OS.execute(interpreter_path, [script_path, str(playerId)], output, true)
	return output[0]
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
