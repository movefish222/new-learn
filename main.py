import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class GitLearningApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.commit_count = 0

    def initUI(self):
        # 创建界面元素
        self.label = QLabel('点击按钮开始你的第一次commit！', self)
        self.button = QPushButton('进行commit', self)
        
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
        
        # 连接信号与槽
        self.button.clicked.connect(self.handle_commit)
        
        # 窗口设置
        self.setWindowTitle('Git学习助手')
        self.setGeometry(300, 300, 300, 150)
        self.show()

    def handle_commit(self):
        self.commit_count += 1
        self.label.setText(f'成功完成 {self.commit_count} 次commit!\n现在尝试在终端运行：\ngit commit -m "第{self.commit_count}次提交"')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitLearningApp()
    sys.exit(app.exec_())