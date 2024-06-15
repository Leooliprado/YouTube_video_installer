from pytube import YouTube
from moviepy.editor import VideoFileClip
from colorama import Fore, Style, init


def download_video(url, output_path='.'):
    try:
        # Cria um objeto YouTube
        yt = YouTube(url)

        # Seleciona a stream de vídeo com a maior resolução
        stream = yt.streams.get_highest_resolution()

        # Faz o download do vídeo
        print(f"{Fore.GREEN}Baixando: {yt.title}{Style.RESET_ALL}")
        video_file = stream.download(output_path)
        print(f"{Fore.GREEN}Download concluído! O vídeo foi salvo em: {video_file}{Style.RESET_ALL}")

        # Converte o vídeo para MP3
        video_clip = VideoFileClip(video_file)
        audio_file = f"{output_path}/{yt.title}.mp3"
        video_clip.audio.write_audiofile(audio_file)

        print(f"{Fore.CYAN}Conversão para MP3 concluída! O áudio foi salvo em: {audio_file}{Style.RESET_ALL}")
        main()

    except Exception as e:
        print(f"{Fore.RED}Ocorreu um erro: {e}{Style.RESET_ALL}")

def main():
    init()  # Inicializa o colorama no início do programa para funcionar em todos os sistemas

    print('')

    # Solicitação para o link do vídeo
    print(f"{Fore.GREEN}Digite o link do vídeo que você deseja baixar:{Style.RESET_ALL}")
    video_url = input()

    print('')

    # Solicitação para o diretório de saída
    print(f"{Fore.GREEN}Digite o diretório onde o vídeo será salvo (deixe em branco para salvar no diretório atual):{Style.RESET_ALL}")
    output_path = input()

    print('')

    if not output_path:
        output_path = '.'

    print("")
    download_video(video_url, output_path)

if __name__ == "__main__":
    main()
