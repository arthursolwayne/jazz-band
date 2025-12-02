
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS, name="Marcus")
piano = Instrument(program=Program.PIANO, name="Diane")
sax = Instrument(program=Program.SAXOPHONE, name="Dante")

pm.instruments = [drums, bass, piano, sax]

# Time per bar: 1.5 seconds
# Time per beat: 0.375 seconds
# Time per eighth note: 0.1875 seconds

# -------------------------------------
# BAR 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# -------------------------------------

# Define MIDI note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: 0.0 to 1.5s
# Kick on 0.0 and 0.75s
drums.notes.append(Note(velocity=100, pitch=KICK, start=0.0, end=0.05))
drums.notes.append(Note(velocity=100, pitch=KICK, start=0.75, end=0.8))

# Snare on 0.375 and 1.125s
drums.notes.append(Note(velocity=100, pitch=SNARE, start=0.375, end=0.4))
drums.notes.append(Note(velocity=100, pitch=SNARE, start=1.125, end=1.15))

# Hi-hats on every eighth
for i in range(8):
    time = i * 0.1875
    drums.notes.append(Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.05))

# -------------------------------------
# BAR 2: Everyone enters
# Marcus on bass: walking line, chromatic approach
# Diane on piano: 7th chords, comp on 2 and 4
# Dante on sax: melody — a short motif, start and leave it hanging
# -------------------------------------

# Marcus: Walking line in D minor (Dm7)
bass_notes = [
    (Note(velocity=100, pitch=62, start=1.5, end=1.55)),  # D
    (Note(velocity=100, pitch=63, start=1.75, end=1.8)),  # Eb
    (Note(velocity=100, pitch=60, start=2.0, end=2.05)),  # C
    (Note(velocity=100, pitch=62, start=2.25, end=2.3)),  # D
]
bass.notes.extend(bass_notes)

# Diane: Dm7 on beat 2 and 4
# Dm7 = D, F, A, C
# Comp on 2 and 4: 2 = 1.75s, 4 = 2.25s
piano_notes = [
    # Beat 2 (1.75s)
    Note(velocity=90, pitch=62, start=1.75, end=1.8),
    Note(velocity=90, pitch=65, start=1.75, end=1.8),
    Note(velocity=90, pitch=67, start=1.75, end=1.8),
    Note(velocity=90, pitch=60, start=1.75, end=1.8),
    
    # Beat 4 (2.25s)
    Note(velocity=90, pitch=62, start=2.25, end=2.3),
    Note(velocity=90, pitch=65, start=2.25, end=2.3),
    Note(velocity=90, pitch=67, start=2.25, end=2.3),
    Note(velocity=90, pitch=60, start=2.25, end=2.3),
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax — short motif, start and leave it hanging
# Motif: D (62) -> Eb (64) -> C (60) — on beat 1 (1.5s), then silence
# Repeat on beat 3 (2.25s)
sax_notes = [
    Note(velocity=100, pitch=62, start=1.5, end=1.55),
    Note(velocity=100, pitch=64, start=1.75, end=1.8),
    Note(velocity=100, pitch=60, start=2.0, end=2.05),
    
    # Repeat of the same motif, but with a space
    Note(velocity=100, pitch=62, start=2.25, end=2.3),
    Note(velocity=100, pitch=64, start=2.45, end=2.5),
    Note(velocity=100, pitch=60, start=2.75, end=2.8)
]
sax.notes.extend(sax_notes)

# Add more hi-hats in bar 2
for i in range(8):
    time = 1.5 + i * 0.1875
    drums.notes.append(Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.05))

# Save the MIDI file
pm.write("dante_intro.mid")
