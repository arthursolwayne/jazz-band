
import pretty_midi
import numpy as np

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
sax = pretty_midi.Instrument(program=64)  # Tenor sax
bass = pretty_midi.Instrument(program=33)  # Double bass
piano = pretty_midi.Instrument(program=0)  # Acoustic piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define the key: F major
F_MAJOR = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, C, D, E, F#
F_MINOR = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, C, D, E, F# (same for natural minor in this case)

# Tempo and timing
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = BEAT * 4  # 6 seconds per bar
NOTE_DURATION = BEAT / 4  # quarter note

# ----------------------------- DRUMS (Little Ray) -----------------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4):
    for beat in range(4):
        time = bar * BAR + beat * BEAT
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=80, pitch=35, start=time, end=time + NOTE_DURATION)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + NOTE_DURATION)
            drums.notes.append(note)
        # Hi-hat on every eighth
        for eighth in range(2):
            hihat_time = time + eighth * BEAT / 2
            note = pretty_midi.Note(velocity=60, pitch=42, start=hihat_time, end=hihat_time + BEAT / 4)
            drums.notes.append(note)

# ----------------------------- BASS (Marcus) -----------------------------
# Walking line in F major
# F -> G -> A -> Bb (chromatic approach to Bb)
bass_notes = [
    65, 67, 69, 70,  # F, G, A, Bb
    72, 74, 76, 77,  # C, D, E, F#
    77, 76, 74, 72,  # F#, E, D, C
    70, 69, 67, 65   # Bb, A, G, F (finish on F)
]

for i, note in enumerate(bass_notes):
    time = (i // 4) * BAR + (i % 4) * BEAT
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + NOTE_DURATION)
    bass.notes.append(note_obj)

# ----------------------------- PIANO (Diane) -----------------------------
# Comp on 2 and 4 with 7th chords
# Chords: F7, Bb7, C7, E7
chords = [
    [65, 69, 72, 76],  # F7
    [70, 74, 77, 82],  # Bb7
    [72, 76, 79, 84],  # C7
    [77, 80, 84, 89]   # E7
]

for beat in range(4):
    time = beat * BEAT
    if beat == 1 or beat == 3:
        for pitch in chords[beat]:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + NOTE_DURATION)
            piano.notes.append(note)

# ----------------------------- SAX (You) -----------------------------
# A simple, personal motif — 4 notes
# F -> G -> Bb -> F (question, unresolved)
# Start on bar 1, leave it hanging, return on bar 3 to finish it
sax_notes = [
    # Bar 1: Start the motif
    pretty_midi.Note(velocity=100, pitch=65, start=0, end=NOTE_DURATION),
    pretty_midi.Note(velocity=100, pitch=67, start=NOTE_DURATION, end=2*NOTE_DURATION),
    # Bar 2: Nothing, leave it hanging
    # Bar 3: Return to finish it
    pretty_midi.Note(velocity=100, pitch=70, start=2*BAR, end=2*BAR + NOTE_DURATION),
    pretty_midi.Note(velocity=100, pitch=65, start=2*BAR + NOTE_DURATION, end=2*BAR + 2*NOTE_DURATION)
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI file
midi.instruments = [sax, bass, piano, drums]

# Save the MIDI file
midi.write("dante_intro.mid")
