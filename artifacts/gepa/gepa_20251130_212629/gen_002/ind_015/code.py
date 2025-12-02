
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set the key signature to F major (no sharps or flats)
pm.key_signature_changes = [pretty_midi.KeySignature(0, 0.0)]  # F major (key number 0)

# Define instrument programs
DRUMS_PROGRAM = 128
BASS_PROGRAM = 33
PIANO_PROGRAM = 0
SAX_PROGRAM = 64

# Create instruments
drums = pretty_midi.Instrument(program=DRUMS_PROGRAM)
bass = pretty_midi.Instrument(program=BASS_PROGRAM)
piano = pretty_midi.Instrument(program=PIANO_PROGRAM)
sax = pretty_midi.Instrument(program=SAX_PROGRAM)

# Add instruments to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Define the tempo (160 BPM)
tempo = 160
beat = 60.0 / tempo  # seconds per beat
bar_length = 4 * beat  # 4/4 time

# Define the time intervals for each bar
bar_times = [0.0, bar_length * 1, bar_length * 2, bar_length * 3, bar_length * 4]

# --- BAR 1: Little Ray on drums (snare on 2 & 4, kick on 1 & 3) ---

# Kick on 1 and 3
kick_notes = [36]  # MIDI note for kick drum
drum_kicks = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.1),
    pretty_midi.Note(velocity=100, pitch=36, start=beat * 2, end=beat * 2 + 0.1),
]
drums.notes.extend(drum_kicks)

# Snare on 2 and 4
snare_notes = [38]  # MIDI note for snare
drum_snare = [
    pretty_midi.Note(velocity=100, pitch=38, start=beat * 1, end=beat * 1 + 0.1),
    pretty_midi.Note(velocity=100, pitch=38, start=beat * 3, end=beat * 3 + 0.1),
]
drums.notes.extend(drum_snare)

# Hi-hat on every eighth note
for i in range(0, 4):
    for j in range(0, 2):
        note_start = beat * (i * 2 + j) + 0.05
        note_end = note_start + 0.1
        pretty_midi.Note(velocity=90, pitch=42, start=note_start, end=note_end)

# --- BAR 2: Everyone comes in --- (start at bar 1)

# Bass: Walking line in F major (F, G, A, Bb, C, D, E, F)
bass_notes = [71, 72, 74, 72, 71, 72, 74, 71]  # F, G, A, G, F, G, A, F (MIDI note numbers)
bass_velocities = [80, 85, 80, 85, 80, 85, 80, 85]

bass_start = bar_times[1]  # start at bar 1
for i in range(len(bass_notes)):
    note_start = bass_start + beat * i
    note_end = note_start + beat * 0.25  # quarter note (since it's walking)
    bass.notes.append(
        pretty_midi.Note(
            velocity=bass_velocities[i],
            pitch=bass_notes[i],
            start=note_start,
            end=note_end
        )
    )

# Piano: 7th chords on 2 and 4 (comping)
# F7 = F, A, C, E
# Bb7 = Bb, D, F, A
# C7 = C, E, G, B
# D7 = D, F, A, C
# Comp on 2 & 4 (beat 1 and beat 3 in bar 2)

bar2_start = bar_times[1]
chords = [
    # Beat 1 (C7) - comp on 2 & 4
    [60, 64, 67, 71],  # C7
    [65, 67, 71, 73],  # D7
    [58, 62, 65, 67],  # F7
    [60, 64, 67, 71],  # C7
]

for i, chord in enumerate(chords):
    start = bar2_start + beat * i
    end = start + 0.15
    for note in chord:
        piano.notes.append(
            pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
        )

# Sax: Motif (F, Bb, C, Eb — a short, mysterious phrase)
# F4 (66), Bb4 (71), C5 (60), Eb5 (64)
# Play on beat 1, then leave it hanging, then come back at the end of bar 4

# First pass: play the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=bar2_start + 0.0, end=bar2_start + 0.2),
    pretty_midi.Note(velocity=110, pitch=71, start=bar2_start + 0.2, end=bar2_start + 0.4),
    pretty_midi.Note(velocity=110, pitch=60, start=bar2_start + 0.4, end=bar2_start + 0.6),
    pretty_midi.Note(velocity=110, pitch=64, start=bar2_start + 0.6, end=bar2_start + 0.8),
]

# Second pass: repeat the motif at the end of bar 4
sax_notes_end = [
    pretty_midi.Note(velocity=110, pitch=66, start=bar_times[4] - 0.2, end=bar_times[4] - 0.0),
    pretty_midi.Note(velocity=110, pitch=71, start=bar_times[4] - 0.0, end=bar_times[4] + 0.2),
    pretty_midi.Note(velocity=110, pitch=60, start=bar_times[4] + 0.2, end=bar_times[4] + 0.4),
    pretty_midi.Note(velocity=110, pitch=64, start=bar_times[4] + 0.4, end=bar_times[4] + 0.6),
]

sax.notes.extend(sax_notes)
sax.notes.extend(sax_notes_end)

# Write the MIDI file to disk
pm.write("dante_introduction.mid")
print("MIDI file created: 'dante_introduction.mid'")
