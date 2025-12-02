
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums - Bar 2
for i in range(4):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time + 0.125, end=time + 0.125 + 0.125))

# Drums - Bar 3
for i in range(4):
    time = 2.25 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time + 0.125, end=time + 0.125 + 0.125))

# Drums - Bar 4
for i in range(4):
    time = 3.0 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time + 0.125, end=time + 0.125 + 0.125))

# Bass line (Marcus) - Walking line in D
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (62, 2.625),
    (64, 2.625), (65, 2.625), (62, 3.0), (64, 3.375),
    (65, 3.75), (62, 4.125), (64, 4.5), (65, 4.875),
    (62, 5.25), (63, 5.625), (60, 6.0), (62, 6.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (67, 2.0), (69, 2.0), (71, 2.0), (65, 2.0),  # D7
    (72, 3.0), (74, 3.0), (76, 3.0), (70, 3.0),  # F#7
    (74, 4.0), (76, 4.0), (78, 4.0), (72, 4.0),  # A7
    (76, 5.0), (78, 5.0), (80, 5.0), (74, 5.0)   # C#7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Saxophone (Dante) - Motif: D, F#, A, D
sax_notes = [
    (62, 1.5), (66, 1.875), (69, 2.25), (62, 2.625),  # First statement
    (62, 3.375), (66, 3.75), (69, 4.125), (62, 4.5),  # Repeat
    (62, 5.25), (66, 5.625), (69, 6.0), (62, 6.375)   # Final statement
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
