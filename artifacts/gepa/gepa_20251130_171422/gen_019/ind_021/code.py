
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Time signature: 4/4
# Tempo: 160 BPM
# 4 bars, each bar is 6 seconds = 160 BPM → 1 beat = 0.375s, 1 bar = 1.5s

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define the key: Dm (D minor)
key = 'Dm'

# Define the instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS, name="Marcus - Bass")
piano = Instrument(program=Program.ELECTRIC_PIANO_1, name="Diane - Piano")
sax = Instrument(program=Program.TENOR_SAX, name="Dante - Saxophone")

pm.instruments = [drums, bass, piano, sax]

# FUNCTION TO CREATE NOTES
def create_note(pitch, start, end, velocity=100):
    note = Note(pitch=pitch, start=start, end=end, velocity=velocity)
    return note

# BAR 1: Little Ray on drums (alone)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
bar_1 = 0.0

# Kick on 1 and 3
drums.notes.extend([
    create_note(36, bar_1 + 0.0, bar_1 + 0.1),
    create_note(36, bar_1 + 0.75, bar_1 + 0.85)
])

# Snare on 2 and 4
drums.notes.extend([
    create_note(38, bar_1 + 0.375, bar_1 + 0.475),
    create_note(38, bar_1 + 0.75, bar_1 + 0.85)
])

# Hi-hat on every eighth
for i in range(0, 8):
    create_note(42, bar_1 + i * 0.375, bar_1 + i * 0.375 + 0.05)

# BAR 2: Everyone in - saxophone takes the melody
bar_2 = bar_1 + bar_length

# Saxophone Melody (short motif in Dm)
# Dm = D, F, Ab, C
# Let's use D, F, Ab, and make it sing
sax.notes.extend([
    create_note(62, bar_2 + 0.0, bar_2 + 0.3),
    create_note(65, bar_2 + 0.3, bar_2 + 0.6),
    create_note(67, bar_2 + 0.6, bar_2 + 0.9),
    create_note(69, bar_2 + 0.9, bar_2 + 1.2)
])

# Bass line: Walking, chromatic approach
bass_notes = [62, 63, 60, 61, 62, 63, 64, 65]  # D, Eb, C, Db, D, Eb, E, F
for i, pitch in enumerate(bass_notes):
    start = bar_2 + i * 0.375
    bass.notes.append(create_note(pitch, start, start + 0.375, velocity=80))

# Piano: 7th chords on 2 and 4, comping
# Dm7 = D, F, A, C
# We'll use a Dm7 voicing on downbeats and a rich comp on 2 and 4
# 2 & 4: 2nd beat (0.375), 4th beat (0.75)
piano.notes.extend([
    create_note(60, bar_2 + 0.375, bar_2 + 0.475),  # F
    create_note(62, bar_2 + 0.375, bar_2 + 0.475),  # D
    create_note(64, bar_2 + 0.375, bar_2 + 0.475),  # A
    create_note(67, bar_2 + 0.375, bar_2 + 0.475),  # C

    create_note(60, bar_2 + 0.75, bar_2 + 0.85),  # F
    create_note(62, bar_2 + 0.75, bar_2 + 0.85),  # D
    create_note(64, bar_2 + 0.75, bar_2 + 0.85),  # A
    create_note(67, bar_2 + 0.75, bar_2 + 0.85),  # C
])

# BAR 3: Continue the rhythm
bar_3 = bar_2 + bar_length

# Drums: same pattern
for i in range(0, 8):
    create_note(42, bar_3 + i * 0.375, bar_3 + i * 0.375 + 0.05)

# Bass: continue walking line
bar_3_notes = [65, 66, 64, 65, 66, 67, 68, 69]
for i, pitch in enumerate(bar_3_notes):
    start = bar_3 + i * 0.375
    bass.notes.append(create_note(pitch, start, start + 0.375, velocity=80))

# Piano: chromatic approach on 2 and 4
piano.notes.extend([
    create_note(61, bar_3 + 0.375, bar_3 + 0.475),
    create_note(63, bar_3 + 0.375, bar_3 + 0.475),
    create_note(64, bar_3 + 0.375, bar_3 + 0.475),
    create_note(66, bar_3 + 0.375, bar_3 + 0.475),

    create_note(61, bar_3 + 0.75, bar_3 + 0.85),
    create_note(63, bar_3 + 0.75, bar_3 + 0.85),
    create_note(64, bar_3 + 0.75, bar_3 + 0.85),
    create_note(66, bar_3 + 0.75, bar_3 + 0.85)
])

# BAR 4: Ending of the intro, saxophone returns with resolution
bar_4 = bar_3 + bar_length

# Saxophone returns to finish the motif
sax.notes.extend([
    create_note(62, bar_4 + 0.0, bar_4 + 0.3),
    create_note(65, bar_4 + 0.3, bar_4 + 0.6),
    create_note(67, bar_4 + 0.6, bar_4 + 0.9),
    create_note(69, bar_4 + 0.9, bar_4 + 1.2)
])

# Bass: resolve to D
bass.notes.append(create_note(62, bar_4 + 0.0, bar_4 + 0.375, velocity=80))

# Piano: Dm7 on beat 4
piano.notes.extend([
    create_note(60, bar_4 + 0.75, bar_4 + 0.85),  # F
    create_note(62, bar_4 + 0.75, bar_4 + 0.85),  # D
    create_note(64, bar_4 + 0.75, bar_4 + 0.85),  # A
    create_note(67, bar_4 + 0.75, bar_4 + 0.85)   # C
])

# Drum fill at the end
drums.notes.extend([
    create_note(36, bar_4 + 1.2, bar_4 + 1.3),
    create_note(38, bar_4 + 1.2, bar_4 + 1.3)
])

# Write the MIDI file
pm.write("dante_intro.mid")
print("MIDI file written: 'dante_intro.mid'")
