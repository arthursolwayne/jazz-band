
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
track_sax = pretty_midi.Instrument(program=64)
track_bass = pretty_midi.Instrument(program=33)
track_piano = pretty_midi.Instrument(program=0)
track_drums = pretty_midi.Instrument(program=0)

# Time per bar in seconds
time_per_bar = 6.0 / 4  # 1.5 seconds per bar
time_per_beat = time_per_bar / 4  # 0.375 seconds per beat

# ----------------------------
# DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: just kick and hihat
drum_notes = {
    'kick': pretty_midi.note_number_to_name(36),
    'snare': pretty_midi.note_number_to_name(38),
    'hihat': pretty_midi.note_number_to_name(42),
}

for bar in range(1, 5):
    time_start = (bar - 1) * time_per_bar
    if bar == 1:
        # Just kick on 1 and hihat on eighths
        for i in range(0, 4):
            time = time_start + i * time_per_beat
            track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.05))
            for eighth in range(2):
                track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * time_per_beat / 2, end=time + eighth * time_per_beat / 2 + 0.03))
    else:
        # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
        for i in range(0, 4):
            time = time_start + i * time_per_beat
            if i % 2 == 0:
                track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.05))
            else:
                track_drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.05))
            for eighth in range(2):
                track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * time_per_beat / 2, end=time + eighth * time_per_beat / 2 + 0.03))
track_drums.is_drum = True
midi.instruments.append(track_drums)

# ----------------------------
# BASS: Marcus
# Walking line, chromatic approaches, no repeated notes

# F major scale: F, G, A, B♭, B, C, D
# Chromatic approach to Bb
bass_notes = [
    # Bar 1
    (0.0, 71),  # F (bottom octave)
    (0.375, 70),  # E (chromatic approach)
    (0.75, 69),  # D
    (1.125, 68),  # C
    # Bar 2
    (1.5, 71),  # F
    (1.875, 72),  # G
    (2.25, 73),  # A
    (2.625, 71),  # F again
    # Bar 3
    (3.0, 71),  # F
    (3.375, 69),  # D
    (3.75, 71),  # F
    (4.125, 72),  # G
    # Bar 4
    (4.5, 71),  # F
    (4.875, 73),  # A
    (5.25, 71),  # F
    (5.625, 72),  # G
]

for start, pitch in bass_notes:
    track_bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))
midi.instruments.append(track_bass)

# ----------------------------
# PIANO: Diane
# 7th chords, comp on 2 and 4

# F7 = F, A, C, E♭
# F7 in different octaves
chord_notes = {
    # Bar 1: quarter note on 2 and 4
    0.75: [59, 64, 60, 62],  # F7 (C4, E♭4, F4, A4)
    1.5: [59, 64, 60, 62],
    # Bar 2: quarter note on 2 and 4
    2.25: [59, 64, 60, 62],
    3.0: [59, 64, 60, 62],
    # Bar 3: quarter note on 2 and 4
    3.75: [59, 64, 60, 62],
    4.5: [59, 64, 60, 62],
    # Bar 4: quarter note on 2 and 4
    5.25: [59, 64, 60, 62],
    6.0: [59, 64, 60, 62],
}

for start, pitches in chord_notes.items():
    for pitch in pitches:
        track_piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))
midi.instruments.append(track_piano)

# ----------------------------
# SAX: Dante
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

sax_notes = [
    # Bar 1
    (0.0, 72),  # G (F major scale)
    (0.75, 72),  # G (hold)
    # Bar 2
    (1.5, 76),  # B♭
    (1.75, 76),  # B♭ (hold)
    # Bar 3
    (3.0, 77),  # B
    (3.25, 77),  # B (hold)
    # Bar 4
    (4.5, 72),  # G
    (4.75, 72),  # G (hold)
    (5.25, 74),  # A
    (5.5, 74),  # A (hold)
]

for start, pitch in sax_notes:
    track_sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25))
midi.instruments.append(track_sax)

# Save the MIDI file
midi.write("cellar_intro.mid")
print("MIDI file saved as 'cellar_intro.mid'")
