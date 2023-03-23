from record import Recorder

if __name__ == '__main__':
    print('hey')
    recorder = Recorder(width=1920,
                        height=1080,
                        path='./outputs',
                        format='mp4',
                        fps=15,
                        device=0)
    recorder.check_dir()
    recorder.record()