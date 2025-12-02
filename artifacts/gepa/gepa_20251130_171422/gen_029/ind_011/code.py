
import pretty_midi
from pretty_midi import Note, Instrument

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Key: D Major (D, E, F#, G, A, B, C#)
# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Create instruments
drums = Instrument(program=10, is_drum=True)
bass = Instrument(program=33)
piano = Instrument(program=0)
sax = Instrument(program=64)  # Tenor sax (MIDI program 64)

# Add instruments to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Set BPM
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Function to convert beat to time in seconds
def beat_to_time(beat):
    return beat / pm.time_signature_changes[0].tempo * 60

# BAR 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [
    Note(36, beat_to_time(0), beat_to_time(0) + 0.3),  # Kick on 1
    Note(36, beat_to_time(2), beat_to_time(2) + 0.3),  # Kick on 3
]
snare_notes = [
    Note(38, beat_to_time(1), beat_to_time(1) + 0.2),  # Snare on 2
    Note(38, beat_to_time(3), beat_to_time(3) + 0.2),  # Snare on 4
]
hihat_notes = [
    Note(42, beat_to_time(i / 8), beat_to_time(i / 8) + 0.1)
    for i in range(0, 8)
]

# Add to drums instrument
for note in kick_notes:
    drums.notes.append(note)
for note in snare_notes:
    drums.notes.append(note)
for note in hihat_notes:
    drums.notes.append(note)

# BAR 2: Everyone joins
# Bass line: walking chromatic line in D major
bass_notes = [
    Note(62, beat_to_time(1), beat_to_time(1) + 0.25),  # D (62)
    Note(63, beat_to_time(1.25), beat_to_time(1.25) + 0.25),  # D#
    Note(64, beat_to_time(1.5), beat_to_time(1.5) + 0.25),  # E
    Note(65, beat_to_time(1.75), beat_to_time(1.75) + 0.25),  # F
    Note(67, beat_to_time(2), beat_to_time(2) + 0.25),  # G
    Note(68, beat_to_time(2.25), beat_to_time(2.25) + 0.25),  # G#
    Note(69, beat_to_time(2.5), beat_to_time(2.5) + 0.25),  # A
    Note(70, beat_to_time(2.75), beat_to_time(2.75) + 0.25),  # A#
    Note(71, beat_to_time(3), beat_to_time(3) + 0.25),  # B
    Note(72, beat_to_time(3.25), beat_to_time(3.25) + 0.25),  # C
    Note(73, beat_to_time(3.5), beat_to_time(3.5) + 0.25),  # C#
    Note(74, beat_to_time(3.75), beat_to_time(3.75) + 0.25),  # D
]

# Add to bass instrument
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# D7 on beat 2, Bm7 on beat 4
# D7: D, F#, A, C
# Bm7: B, D, F#, A
piano_notes = [
    Note(62, beat_to_time(2), beat_to_time(2) + 0.2),  # D
    Note(67, beat_to_time(2), beat_to_time(2) + 0.2),  # A
    Note(64, beat_to_time(2), beat_to_time(2) + 0.2),  # F#
    Note(69, beat_to_time(2), beat_to_time(2) + 0.2),  # C

    Note(71, beat_to_time(3), beat_to_time(3) + 0.2),  # B
    Note(62, beat_to_time(3), beat_to_time(3) + 0.2),  # D
    Note(67, beat_to_time(3), beat_to_time(3) + 0.2),  # A
    Note(64, beat_to_time(3), beat_to_time(3) + 0.2),  # F#
]

# Add to piano instrument
for note in piano_notes:
    piano.notes.append(note)

# Tenor Sax: Your moment — a short, singing motif
# Play a D-G-A motif starting on beat 2
# D (62), G (67), A (69), rest on 4
sax_notes = [
    Note(62, beat_to_time(2), beat_to_time(2) + 0.3),  # D
    Note(67, beat_to_time(2.5), beat_to_time(2.5) + 0.3),  # G
    Note(69, beat_to_time(3), beat_to_time(3) + 0.3),  # A
]

# Add to sax instrument
for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
pm.write("jazz_intro_d_major.mid")
print("MIDI file created: jazz_intro_d_major.mid")
