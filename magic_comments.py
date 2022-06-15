import sublime
import sublime_plugin

LINE = "─"
LINE_LENGTH = 80
PREFIX_PAD = 4



class PrettyCommentLineCommand(sublime_plugin.TextCommand):
	# hack to avoid pulling in all of comment.py
	def uncomment_line(self, view):
		before = content = view.substr(view.line(view.sel()[0]))
		view.run_command("toggle_comment", False)
		after = content = view.substr(view.line(view.sel()[0]))
		if len(after) > len(before):
			view.run_command("toggle_comment", False)

	def run(self, edit):
		view = self.view
		self.uncomment_line(view)
		content = view.substr(view.line(view.sel()[0]))
		line = view.line(view.sel()[0])

		text = content.replace(LINE,"").strip().upper()
		right_pad = LINE_LENGTH - len(text) - PREFIX_PAD - 4
		comment = f"{LINE*PREFIX_PAD} {text} {LINE*right_pad}"

		view.replace(edit, line, comment)
		view.run_command("toggle_comment", False)
