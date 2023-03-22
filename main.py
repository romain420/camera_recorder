from record import Recorder

if __name__ == '__main__':
    print('hey')
    recorder = Recorder(width=1280,
                        height=720,
                        path='./outputs',
                        format='mp4',
                        fps=15)
    recorder.check_dir()
    recorder.record()