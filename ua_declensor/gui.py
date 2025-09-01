from __future__ import annotations

import sys
from typing import Dict

from PyQt6.QtWidgets import (
	QApplication,
	QComboBox,
	QGridLayout,
	QHBoxLayout,
	QHeaderView,
	QLabel,
	QLineEdit,
	QMainWindow,
	QPushButton,
	QTableWidget,
	QTableWidgetItem,
	QVBoxLayout,
	QWidget,
	QFileDialog,
	QMessageBox,
)

from .engine import decline_full_name_all_cases, CASES_ORDER, CASE_LABELS_UA


class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		self.setWindowTitle("UA Declensor")
		central = QWidget()
		self.setCentralWidget(central)

		self.input_edit = QLineEdit()
		self.input_edit.setPlaceholderText("Прізвище Ім’я По батькові")
		self.gender_combo = QComboBox()
		self.gender_combo.addItems(["auto", "m", "f"])

		self.btn_decline = QPushButton("Decline")
		self.btn_clear = QPushButton("Clear")
		self.btn_export = QPushButton("Export to Excel")

		self.table = QTableWidget(0, 2)
		self.table.setHorizontalHeaderLabels(["Відмінок", "Результат"])
		self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
		self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
		self.table.verticalHeader().setVisible(False)

		top = QHBoxLayout()
		top.addWidget(QLabel("Full Name:"))
		top.addWidget(self.input_edit)
		top.addWidget(QLabel("Gender:"))
		top.addWidget(self.gender_combo)

		btns = QHBoxLayout()
		btns.addWidget(self.btn_decline)
		btns.addWidget(self.btn_clear)
		btns.addWidget(self.btn_export)

		layout = QVBoxLayout()
		layout.addLayout(top)
		layout.addLayout(btns)
		layout.addWidget(self.table)
		central.setLayout(layout)

		self.btn_decline.clicked.connect(self.on_decline)
		self.btn_clear.clicked.connect(self.on_clear)
		self.btn_export.clicked.connect(self.on_export)

	def on_decline(self) -> None:
		text = self.input_edit.text().strip()
		if not text:
			QMessageBox.warning(self, "UA Declensor", "#UA_ERR: Invalid input format")
			return
		gender = self.gender_combo.currentText()
		try:
			results = decline_full_name_all_cases(text, gender=gender)  # type: ignore[arg-type]
			self.populate_table(results)
		except Exception as e:
			QMessageBox.critical(self, "UA Declensor", f"#UA_ERR: {e}")

	def populate_table(self, results: Dict[str, str]) -> None:
		self.table.setRowCount(len(CASES_ORDER))
		for row, case in enumerate(CASES_ORDER):
			label = CASE_LABELS_UA[case]
			self.table.setItem(row, 0, QTableWidgetItem(label))
			self.table.setItem(row, 1, QTableWidgetItem(results[case]))

	def on_clear(self) -> None:
		self.input_edit.clear()
		self.table.setRowCount(0)

	def on_export(self) -> None:
		if self.table.rowCount() == 0:
			QMessageBox.information(self, "UA Declensor", "Немає даних для експорту")
			return
		path, _ = QFileDialog.getSaveFileName(self, "Save Excel", "cases.xlsx", "Excel Files (*.xlsx)")
		if not path:
			return
		try:
			import pandas as pd
			rows = []
			for r in range(self.table.rowCount()):
				rows.append({
					"Case": self.table.item(r, 0).text(),
					"Result": self.table.item(r, 1).text(),
				})
			df = pd.DataFrame(rows)
			df.to_excel(path, index=False)
			QMessageBox.information(self, "UA Declensor", f"Збережено: {path}")
		except Exception as e:
			QMessageBox.critical(self, "UA Declensor", f"#UA_ERR: {e}")


def run() -> None:
	app = QApplication(sys.argv)
	w = MainWindow()
	w.resize(800, 480)
	w.show()
	sys.exit(app.exec())


if __name__ == "__main__":  # pragma: no cover
	run()