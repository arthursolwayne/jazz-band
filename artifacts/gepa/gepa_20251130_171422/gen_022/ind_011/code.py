
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key (F major)
key = 'F'

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time in seconds for each beat
beat = 0.375
bar = 1.5

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add subtle variation in dynamics
drum_notes = [
    # Kick on beat 1
    Note(36, 100, 0, beat),
    # Snare on beat 2
    Note(38, 80, beat, beat),
    # Hihat on 8th notes
    Note(42, 60, 0, beat/2),
    Note(42, 60, beat/2, beat),
    Note(42, 60, beat, beat + beat/2),
    Note(42, 60, beat + beat/2, beat * 2),
    # Kick on beat 3
    Note(36, 100, beat * 1.5, beat),
    # Snare on beat 4
    Note(38, 80, beat * 2, beat),
    # Hihat on 8th notes
    Note(42, 60, beat * 1.5, beat/2),
    Note(42, 60, beat * 2, beat/2),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: All instruments enter

# Bass line: walking with chromatic approaches
bass_notes = [
    Note(48, 80, bar, beat),  # F
    Note(49, 80, bar + beat, beat),  # G
    Note(50, 80, bar + beat * 2, beat),  # A
    Note(51, 80, bar + beat * 3, beat),  # Bb
    Note(52, 80, bar + beat * 4, beat),  # B
    Note(51, 80, bar + beat * 5, beat),  # Bb
    Note(50, 80, bar + beat * 6, beat),  # A
    Note(49, 80, bar + beat * 7, beat),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, with dynamic shading
piano_notes = [
    # Bar 2, beat 1: rest
    # Bar 2, beat 2: F7 (F, A, C, E♭)
    Note(53, 80, bar + beat * 1, beat),
    Note(60, 80, bar + beat * 1, beat),
    Note(55, 80, bar + beat * 1, beat),
    Note(58, 80, bar + beat * 1, beat),
    # Bar 2, beat 3: rest
    # Bar 2, beat 4: F7 again but with dynamic shift
    Note(53, 70, bar + beat * 3, beat),
    Note(60, 70, bar + beat * 3, beat),
    Note(55, 70, bar + beat * 3, beat),
    Note(58, 70, bar + beat * 3, beat),
]
piano.notes.extend(piano_notes)

# Drums: same pattern as Bar 1
for note in drum_notes:
    drums.notes.append(note)

# Sax: Motif (F, G, Bb, A) with rests in between, leaving it hanging
sax_notes = [
    Note(53, 100, bar + beat * 0.5, beat/2),  # F
    Note(55, 100, bar + beat * 1.5, beat/2),  # G
    Note(58, 100, bar + beat * 2.5, beat/2),  # Bb
    # Rest on beat 3
    # Return on beat 4
    Note(55, 100, bar + beat * 3.5, beat/2),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Continue the pattern
# Bass: continue the walking line
bass_notes = [
    Note(52, 80, bar * 2, beat),  # B
    Note(51, 80, bar * 2 + beat, beat),  # Bb
    Note(50, 80, bar * 2 + beat * 2, beat),  # A
    Note(49, 80, bar * 2 + beat * 3, beat),  # G
    Note(48, 80, bar * 2 + beat * 4, beat),  # F
    Note(49, 80, bar * 2 + beat * 5, beat),  # G
    Note(50, 80, bar * 2 + beat * 6, beat),  # A
    Note(51, 80, bar * 2 + beat * 7, beat),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: continue with 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 1: rest
    # Bar 3, beat 2: F7
    Note(53, 80, bar * 2 + beat * 1, beat),
    Note(60, 80, bar * 2 + beat * 1, beat),
    Note(55, 80, bar * 2 + beat * 1, beat),
    Note(58, 80, bar * 2 + beat * 1, beat),
    # Bar 3, beat 3: rest
    # Bar 3, beat 4: F7 again, dynamic shift
    Note(53, 70, bar * 2 + beat * 3, beat),
    Note(60, 70, bar * 2 + beat * 3, beat),
    Note(55, 70, bar * 2 + beat * 3, beat),
    Note(58, 70, bar * 2 + beat * 3, beat),
]
piano.notes.extend(piano_notes)

# Drums: same pattern
for note in drum_notes:
    drums.notes.append(note)

# Sax: repeat the motif, but with variation in rhythm
sax_notes = [
    Note(53, 100, bar * 2 + beat * 0.5, beat/2),  # F
    Note(55, 100, bar * 2 + beat * 1.5, beat/2),  # G
    Note(58, 100, bar * 2 + beat * 2.5, beat/2),  # Bb
    # Rest on beat 3
    # Return on beat 4
    Note(55, 100, bar * 2 + beat * 3.5, beat/2),  # A
]
sax.notes.extend(sax_notes)

# Bar 4: Continue the pattern
# Bass: continue the walking line
bass_notes = [
    Note(51, 80, bar * 3, beat),  # Bb
    Note(50, 80, bar * 3 + beat, beat),  # A
    Note(49, 80, bar * 3 + beat * 2, beat),  # G
    Note(48, 80, bar * 3 + beat * 3, beat),  # F
    Note(49, 80, bar * 3 + beat * 4, beat),  # G
    Note(50, 80, bar * 3 + beat * 5, beat),  # A
    Note(51, 80, bar * 3 + beat * 6, beat),  # Bb
    Note(52, 80, bar * 3 + beat * 7, beat),  # B
]
bass.notes.extend(bass_notes)

# Piano: continue with 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 1: rest
    # Bar 4, beat 2: F7
    Note(53, 80, bar * 3 + beat * 1, beat),
    Note(60, 80, bar * 3 + beat * 1, beat),
    Note(55, 80, bar * 3 + beat * 1, beat),
    Note(58, 80, bar * 3 + beat * 1, beat),
    # Bar 4, beat 3: rest
    # Bar 4, beat 4: F7 again, dynamic shift
    Note(53, 70, bar * 3 + beat * 3, beat),
    Note(60, 70, bar * 3 + beat * 3, beat),
    Note(55, 70, bar * 3 + beat * 3, beat),
    Note(58, 70, bar * 3 + beat * 3, beat),
]
piano.notes.extend(piano_notes)

# Drums: same pattern
for note in drum_notes:
    drums.notes.append(note)

# Sax: repeat the motif, but this time end it
sax_notes = [
    Note(53, 100, bar * 3 + beat * 0.5, beat/2),  # F
    Note(55, 100, bar * 3 + beat * 1.5, beat/2),  # G
    Note(58, 100, bar * 3 + beat * 2.5, beat/2),  # Bb
    Note(55, 100, bar * 3 + beat * 3.5, beat/2),  # A
]
sax.notes.extend(sax_notes)

# Write the MIDI file
pm.write("jazz_intro.mid")
