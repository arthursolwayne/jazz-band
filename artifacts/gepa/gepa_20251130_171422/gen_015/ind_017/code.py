
import pretty_midi

# Create a new MIDI file with tempo set to 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Instrument channels
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time signatures and bar timing
bar_length = 1.5  # seconds per bar at 160 BPM, 4/4 time
beat_length = bar_length / 4  # 0.375 seconds per beat

# ------------------
# BAR 1: DRUMS ONLY (0.0 - 1.5s)
# Little Ray sets the tone — a question in rhythm and space

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * beat_length
    # Kick on beat 1 and 3
    if beat == 0 or beat == 2:
        kick = pretty_midi.Note(
            velocity=90,
            pitch=drum_notes['kick'],
            start=time,
            end=time + 0.15
        )
        drums.notes.append(kick)
    # Snare on beat 2 and 4
    if beat == 1 or beat == 3:
        snare = pretty_midi.Note(
            velocity=85,
            pitch=drum_notes['snare'],
            start=time,
            end=time + 0.15
        )
        drums.notes.append(snare)
    # Hihat on every eighth note
    hihat = pretty_midi.Note(
        velocity=80,
        pitch=drum_notes['hihat'],
        start=time,
        end=time + 0.075
    )
    drums.notes.append(hihat)

# ------------------
# BAR 2-4: FULL QUARTET (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# F7 chord: F A C E
# Walking bass line: F, G, A, Bb, B, C, D, Eb, E, F..., chromatic and bluesy

bass_notes = [
    (1.5, 79),  # F
    (1.75, 80), # G
    (2.0, 82),  # A
    (2.25, 83), # Bb
    (2.5, 84),  # B
    (2.75, 87), # C
    (3.0, 89),  # D
    (3.25, 88), # Eb
    (3.5, 84),  # B
    (3.75, 87), # C
    (4.0, 89),  # D
    (4.25, 91), # Eb
    (4.5, 93),  # F
    (4.75, 96), # G
    (5.0, 98),  # A
    (5.25, 100), # Bb
    (5.5, 101), # B
    (5.75, 104), # C
    (6.0, 107)  # D
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(
        velocity=70,
        pitch=pitch,
        start=time,
        end=time + 0.25
    )
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4. Stay out of sax's way but keep it moving
# 2nd bar: F7, 3rd bar: Bb7, 4th bar: E7
# Chord voicings: Root, 3rd, 7th, 9th (spread out)

# Bar 2: F7 (F, A, C, E)
piano_notes = [
    (1.5, 79),  # F
    (1.5, 82),  # A
    (1.5, 87),  # C
    (1.5, 92),  # E
    (2.0, 84),  # Bb
    (2.0, 87),  # C
    (2.0, 92),  # E
    (2.0, 97),  # G
    # Leave space between bars
    (2.5, 79),  # F
    (2.5, 82),  # A
    (2.5, 87),  # C
    (2.5, 92),  # E
    (3.0, 84),  # Bb
    (3.0, 87),  # C
    (3.0, 92),  # E
    (3.0, 97),  # G

    (3.5, 87),  # E7: E, G, B, D
    (3.5, 92),  # E
    (3.5, 97),  # G
    (3.5, 101), # B
    (3.5, 104), # D
    (4.0, 87),  # E
    (4.0, 92),  # G
    (4.0, 101), # B
    (4.0, 104), # D
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(
        velocity=95,
        pitch=pitch,
        start=time,
        end=time + 0.1
    )
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F6 (F, A, C), with a descending chromatic run to Bb, then resolution

sax_notes = [
    (1.5, 79),  # F
    (1.5, 82),  # A
    (1.5, 87),  # C
    (1.75, 84),  # Bb (chromatic descent)
    (2.0, 82),  # A
    (2.25, 87),  # C
    (2.5, 84),  # Bb
    (2.75, 82),  # A
    (3.0, 87),  # C
    (3.25, 89),  # D
    (3.5, 92),  # E
    (3.75, 87),  # C
    (4.0, 84),  # Bb
    (4.25, 82),  # A
    (4.5, 87),  # C
    (4.75, 89),  # D
    (5.0, 92),  # E
    (5.25, 87),  # C
    (5.5, 84),  # Bb
    (5.75, 82),  # A
    (6.0, 87)   # C
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(
        velocity=100,
        pitch=pitch,
        start=time,
        end=time + 0.15
    )
    sax.notes.append(note)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
