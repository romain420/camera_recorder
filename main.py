from record import Recorder

if __name__ == '__main__':
    print('hey')
    recorder = Recorder(width=640,
                        height=480,
                        path='./test',
                        format='mp4',
                        fps=20.0)
    recorder.check_dir()
    recorder.record()