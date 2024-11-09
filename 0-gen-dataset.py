import yt_dlp as youtube_dl
from moviepy.editor import VideoFileClip
import json
import os
import tempfile

def download_and_split_video_to_png(url, n_fragments, output_dir="video_fragments"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Download the video to a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]',
            'outtmpl': os.path.join(temp_dir, 'video.mp4')
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_title = info.get('title')
            video_path = os.path.join(temp_dir, 'video.mp4')

        # Load the video with moviepy and get duration
        video_clip = VideoFileClip(video_path)
        duration = video_clip.duration
        fragment_duration = duration / n_fragments

        # Capture a single frame at the midpoint of each fragment
        for i in range(n_fragments):
            # Calculate the midpoint time for the fragment
            midpoint_time = (i * fragment_duration) + (fragment_duration / 2)
            frame_path = os.path.join(output_dir, f"fragment_{i + 1}.png")

            # Save the frame as a PNG at the calculated time
            video_clip.save_frame(frame_path, t=midpoint_time)

        # Create info.json file
        info_data = {
            "title": video_title,
            "url": url
        }
        with open(os.path.join(output_dir, "info.json"), "w") as f:
            json.dump(info_data, f, indent=4)

    print(f"Video downloaded, split into {n_fragments} images as PNG files, and saved in the '{output_dir}' directory.")

FRAGMENTS = 100
video_list = [
    {
        "name": "bad_bunny_la_dificil",
        "url": "https://www.youtube.com/watch?v=fEYUoBgYKzw"
    },
    {
        "name": "larevuelta_mariocasas",
        "url": "https://www.youtube.com/watch?v=bYDh4Gzqja8"
    },
    {
        "name": "taylor_swift_shake_it_off",
        "url": "https://www.youtube.com/watch?v=nfWlot6h_JM"
    },
    {
        "name": "bad_bunny_yo_perreoso_sola",
        "url": "https://www.youtube.com/watch?v=GtSRKwDCaZM"
    },
    {
        "name": "taylor_swift_fortnight",
        "url": "https://www.youtube.com/watch?v=q3zqJs7JUCQ"
    },
    {
        "name": "webinar_php",
        "url": "https://www.youtube.com/watch?v=Jp2iUdiX-d0"
    },
    {
        "name": "nate_llm",
        "url": "https://www.youtube.com/watch?v=W2YwMuxzyJY"
    },
    {
        "name": "larevuelta_carrileon",
        "url": "https://www.youtube.com/watch?v=cI0zpg6AGqE"
    },
    # Music videos
    {
        "name": "bad_bunny_la_dificil",
        "url": "https://www.youtube.com/watch?v=fEYUoBgYKzw"
    },
    {
        "name": "taylor_swift_shake_it_off",
        "url": "https://www.youtube.com/watch?v=nfWlot6h_JM"
    },
    {
        "name": "coldplay_viva_la_vida",
        "url": "https://www.youtube.com/watch?v=dvgZkm1xWPE"
    },
    {
        "name": "ed_sheeran_shape_of_you",
        "url": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
    },
    {
        "name": "michael_jackson_thriller",
        "url": "https://www.youtube.com/watch?v=sOnqjkJTMaA"
    },

    # Science and technology videos
    {
        "name": "documentary_hubble_the_universe",
        "url": "https://www.youtube.com/watch?v=oAVjF_7ensg"
    },
    {
        "name": "elon_musk_spacex_mars",
        "url": "https://www.youtube.com/watch?v=zSv0Y7qrzQM"
    },
    {
        "name": "neil_degrasse_tyson_origins_universe",
        "url": "https://www.youtube.com/watch?v=9D05ej8u-gU"
    },
    {
        "name": "how_big_is_the_universe",
        "url": "https://www.youtube.com/watch?v=Iy7NzjCmUf0"
    },
    {
        "name": "future_of_artificial_intelligence",
        "url": "https://www.youtube.com/watch?v=7Pq-S557XQU"
    },

    # Tutorials and educational videos
    {
        "name": "python_programming_full_course",
        "url": "https://www.youtube.com/watch?v=_uQrJ0TkZlc"
    },
    {
        "name": "how_to_cook_the_perfect_steak",
        "url": "https://www.youtube.com/watch?v=a03U45jFxOI"
    },
    {
        "name": "intro_to_machine_learning",
        "url": "https://www.youtube.com/watch?v=Gv9_4yMHFhI"
    },
]

for video in video_list:
    data_path = f"data/{video['name']}"
    if os.path.exists(data_path):
        print(f"Video '{video['name']}' already downloaded and split into {FRAGMENTS} fragments.")
        continue
    download_and_split_video_to_png(video["url"], FRAGMENTS, data_path)
    print(f"Downloaded and split video '{video['name']}' into {FRAGMENTS} fragments.")
