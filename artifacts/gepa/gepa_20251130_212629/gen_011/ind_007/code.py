
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
tempo = 160
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Create instruments
bass = Instrument(program=33)  # Electric Bass
piano = Instrument(program=0)  # Acoustic Piano
drums = Instrument(program=0)  # Drums
sax = Instrument(program=64)   # Tenor Saxophone

pm.instruments = [bass, piano, drums, sax]

# Set tempo
pm.tempo_changes = [pretty_midi.TempoChange(tempo=tempo, time=0.0)]

# Time per bar: 6 seconds
# Time per beat: 0.375 seconds
# Time per note: 0.375 seconds for quarter notes, etc.

# Define bar lengths in seconds
BAR_LENGTH = 6.0
BEAT_LENGTH = 0.375

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4):
    for beat in range(4):
        time = bar * BAR_LENGTH + beat * BEAT_LENGTH
        if beat == 0 or beat == 2:
            drums.notes.append(Note(velocity=100, pitch=36, start=time, end=time + 0.1))
        if beat == 1 or beat == 3:
            drums.notes.append(Note(velocity=90, pitch=38, start=time, end=time + 0.1))
        for eighth in range(2):
            drums.notes.append(Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05))

# --- BASS: Marcus ---
# Walking line in Dm, chromatic approaches, no repeated notes
# Dm scale: D, F, G, A, Bb, C, D
bass_notes = [
    Note(velocity=100, pitch=62, start=0, end=0.375),   # D
    Note(velocity=100, pitch=64, start=0.375, end=0.75), # F
    Note(velocity=100, pitch=67, start=0.75, end=1.125), # G
    Note(velocity=100, pitch=69, start=1.125, end=1.5),  # A

    Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    Note(velocity=100, pitch=65, start=1.875, end=2.25), # F
    Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F

    Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    Note(velocity=100, pitch=71, start=3.375, end=3.75), # Bb
    Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G

    Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]

bass.notes = bass_notes

# --- PIANO: Diane ---
# 7th chords on 2 and 4, chromatic movement, rich voicings

# Dm7: D, F, A, C
# F7: F, A, C, E
# Bbm7: Bb, D, F, Ab
# Cm7: C, Eb, G, Bb

# Bar 1: rest
# Bar 2: Dm7 on beat 2
# Bar 3: F7 on beat 2
# Bar 4: Bbm7 on beat 2

# Bar 2
piano.notes.append(Note(velocity=90, pitch=62, start=1.5, end=1.875))  # D
piano.notes.append(Note(velocity=90, pitch=64, start=1.5, end=1.875))  # F
piano.notes.append(Note(velocity=90, pitch=69, start=1.5, end=1.875))  # A
piano.notes.append(Note(velocity=90, pitch=67, start=1.5, end=1.875))  # C

# Bar 3
piano.notes.append(Note(velocity=90, pitch=64, start=3.0, end=3.375))  # F
piano.notes.append(Note(velocity=90, pitch=69, start=3.0, end=3.375))  # A
piano.notes.append(Note(velocity=90, pitch=67, start=3.0, end=3.375))  # C
piano.notes.append(Note(velocity=90, pitch=71, start=3.0, end=3.375))  # E

# Bar 4
piano.notes.append(Note(velocity=90, pitch=67, start=4.5, end=4.875))  # Bb
piano.notes.append(Note(velocity=90, pitch=62, start=4.5, end=4.875))  # D
piano.notes.append(Note(velocity=90, pitch=64, start=4.5, end=4.875))  # F
piano.notes.append(Note(velocity=90, pitch=66, start=4.5, end=4.875))  # Ab

# --- SAX: Dante ---
# Short motif, one line, haunting, leaves it hanging

# This is the motif: D, F, G, A — played with space and emotion
# D (62), F (64), G (67), A (69) — quarter notes

sax.notes.append(Note(velocity=110, pitch=62, start=0.0, end=0.375))  # D
sax.notes.append(Note(velocity=110, pitch=64, start=0.75, end=1.125)) # F
sax.notes.append(Note(velocity=110, pitch=67, start=1.5, end=1.875)) # G
sax.notes.append(Note(velocity=110, pitch=69, start=2.25, end=2.625)) # A

# End on the last note of the motif, leave it hanging

# Save the MIDI file
pm.save('dante_intro.mid')

print("Done. Saved as 'dante_intro.mid'.")
