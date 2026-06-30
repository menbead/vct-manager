extends HTTPRequest

# useful python -> godot tutorial:
# https://www.youtube.com/watch?v=z2MHuWEDUNw
var DIR = OS.get_executable_path().get_base_dir()
var interpreter_path = DIR.path_join("PythonFiles/venv/Scripts/python.exe")
var server_script_path  = DIR.path_join("PythonFiles/vlr.py")
var server_pid = -1

# starts the flask server 
func _ready() -> void:
	if not OS.has_feature("standalone"): # if NOT exported version
		interpreter_path = ProjectSettings.globalize_path("res://PythonFiles/venv/Scripts/python.exe")
		server_script_path  = ProjectSettings.globalize_path("res://PythonFiles/vlr.py")
	
	server_pid = OS.create_process(interpreter_path, [server_script_path])
	print("Flask server started with PID: ", server_pid)
	await get_tree().create_timer(1.0).timeout

func _http_request_completed(result, response_code, headers, body):
	if result != HTTPRequest.RESULT_SUCCESS:
		push_error("Error fetching from Flask server.")



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
