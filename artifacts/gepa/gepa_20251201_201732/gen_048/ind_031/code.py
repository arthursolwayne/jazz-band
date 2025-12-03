
import mido
from mido import Message, MidiFile, MidiTrack

# Set tempo (160 BPM)
BPM = 160
ticks_per_beat = 480
tempo = mido.bpm2tempo(BPM)

# Create a new MIDI file
mid = MidiFile(ticks_per_beat=ticks_per_beat)
track = MidiTrack()
mid.tracks.append(track)

# Add tempo
track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0))

# Define the key: Dm (D minor)
# Root: D (MIDI 62)
# Scales: Natural minor (D Dorian in this context, harmonic minor for tension)

# Define each instrument's channel
# Tenor sax: channel 0
# Piano: channel 1
# Bass: channel 2
# Drums: channel 9 (Standard MIDI drum channel)

# Bars: 4 bars at 160 BPM = 6 seconds
# Each bar = 1.5 seconds
# Each beat = 0.375 seconds
# Each tick = 0.375 / 480 ≈ 0.00078125 seconds

# Define time for each beat
beat_ticks = ticks_per_beat
bar_ticks = beat_ticks * 4  # 4 beats per bar
total_ticks = bar_ticks * 4  # 4 bars

# Function to add notes
def add_notes(track, channel, notes, time, duration_ticks):
    for note in notes:
        on = Message('note_on', note=note[0], velocity=note[1], channel=channel, time=time)
        track.append(on)
        time += duration_ticks
        off = Message('note_off', note=note[0], velocity=note[1], channel=channel, time=0)
        track.append(off)
    return time

# Start time
current_time = 0

# Bar 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Use standard MIDI drum notes:
# Kick = 36, Snare = 38, Hihat = 42

# Bar 1
current_time = add_notes(track, 9, [(36, 100), (42, 80)], current_time, beat_ticks)  # Kick on 1, Hihat on 1
current_time = add_notes(track, 9, [(42, 80)], current_time, beat_ticks // 2)      # Hihat on 2
current_time = add_notes(track, 9, [(38, 100), (42, 80)], current_time, beat_ticks // 2)  # Snare on 2, Hihat on 3
current_time = add_notes(track, 9, [(36, 100), (42, 80)], current_time, beat_ticks // 2)  # Kick on 3, Hihat on 4
current_time = add_notes(track, 9, [(38, 100), (42, 80)], current_time, beat_ticks // 2)  # Snare on 4, Hihat on 4

# Bar 2: Marcus (bass) enters — Dm7 walking line with chromatic approaches
# Dm7 = D, F, A, C
# D2 = MIDI 38 (D2)
# Walking line: D2 -> Eb2 (chromatic approach) -> F2 -> G2
# Each note is 1 beat
notes_bass = [
    (38, 64),  # D2
    (40, 64),  # Eb2
    (43, 64),  # F2
    (46, 64),  # G2
]
current_time = add_notes(track, 2, notes_bass, current_time, beat_ticks)

# Diane (piano) enters — open voicings, different chord each bar, resolve on last
# Bar 2: Dm7 (D, F, A, C) in open voicings — sparse, haunting
# Use high register for tension
notes_piano_bar2 = [
    (60, 80),  # C4
    (62, 80),  # D4
    (65, 80),  # F4
    (67, 80),  # A4
]
current_time = add_notes(track, 1, notes_piano_bar2, current_time, beat_ticks)

# Bar 3: Marcus continues walking line
# F2 -> G2 -> Ab2 (chromatic approach) -> A2
notes_bass_bar3 = [
    (43, 64),  # F2
    (46, 64),  # G2
    (47, 64),  # Ab2
    (49, 64),  # A2
]
current_time = add_notes(track, 2, notes_bass_bar3, current_time, beat_ticks)

# Diane (piano) — Bm7b5 (B, D, F, A) in open voicings
notes_piano_bar3 = [
    (61, 80),  # B4
    (64, 80),  # D5
    (66, 80),  # F5
    (69, 80),  # A5
]
current_time = add_notes(track, 1, notes_piano_bar3, current_time, beat_ticks)

# Bar 4: Marcus continues walking line
# A2 -> Bb2 -> B2 (chromatic approach) -> C2
notes_bass_bar4 = [
    (49, 64),  # A2
    (50, 64),  # Bb2
    (51, 64),  # B2
    (52, 64),  # C2
]
current_time = add_notes(track, 2, notes_bass_bar4, current_time, beat_ticks)

# Diane (piano) — G7 (G, B, D, F) in open voicings — unresolved, tension
notes_piano_bar4 = [
    (67, 80),  # G4
    (71, 80),  # B4
    (74, 80),  # D5
    (76, 80),  # F5
]
current_time = add_notes(track, 1, notes_piano_bar4, current_time, beat_ticks)

# Bar 4: You (tenor sax) — short, haunting motif — start and leave it hanging
# Motif: D4 (MIDI 62), E4 (MIDI 64), D4 (MIDI 62), rest
# Play first two notes, then rest — leave it hanging
notes_tenor = [
    (62, 100),  # D4
    (64, 100),  # E4
]
current_time = add_notes(track, 0, notes_tenor, current_time, beat_ticks // 2)

# End of track
track.append(Message('end_of_track', time=current_time))

# Save the MIDI file
mid.save('dante_intro.mid')
