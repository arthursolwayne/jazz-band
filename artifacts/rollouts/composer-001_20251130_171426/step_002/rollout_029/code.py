
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
    
    (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line - Dm7, walking line with chromatic approach
bass_notes = [
    (50, 1.5, 1.5),  # D
    (49, 1.875, 2.125),  # C
    (51, 2.25, 2.625),  # Eb
    (52, 2.625, 3.0),  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano - Dm7 comp on 2 and 4
piano_notes = [
    (60, 1.875, 2.125),  # F
    (62, 1.875, 2.125),  # A
    (64, 1.875, 2.125),  # C
    (67, 1.875, 2.125),  # D
    (60, 2.625, 2.875),  # F
    (62, 2.625, 2.875),  # A
    (64, 2.625, 2.875),  # C
    (67, 2.625, 2.875),  # D
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax - motif: D -> Eb -> F -> D
sax_notes = [
    (62, 1.5, 1.6875),  # D
    (64, 1.6875, 1.875),  # Eb
    (65, 1.875, 2.0625),  # F
    (62, 2.0625, 2.25),  # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line - Dm7, walking line with chromatic approach
bass_notes = [
    (50, 3.0, 3.375),  # D
    (49, 3.375, 3.75),  # C
    (51, 3.75, 4.125),  # Eb
    (52, 4.125, 4.5),  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano - Dm7 comp on 2 and 4
piano_notes = [
    (60, 3.375, 3.625),  # F
    (62, 3.375, 3.625),  # A
    (64, 3.375, 3.625),  # C
    (67, 3.375, 3.625),  # D
    (60, 4.125, 4.375),  # F
    (62, 4.125, 4.375),  # A
    (64, 4.125, 4.375),  # C
    (67, 4.125, 4.375),  # D
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax - motif: D -> Eb -> F -> D
sax_notes = [
    (62, 3.0, 3.1875),  # D
    (64, 3.1875, 3.375),  # Eb
    (65, 3.375, 3.5625),  # F
    (62, 3.5625, 3.75),  # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line - Dm7, walking line with chromatic approach
bass_notes = [
    (50, 4.5, 4.875),  # D
    (49, 4.875, 5.25),  # C
    (51, 5.25, 5.625),  # Eb
    (52, 5.625, 6.0),  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano - Dm7 comp on 2 and 4
piano_notes = [
    (60, 4.875, 5.125),  # F
    (62, 4.875, 5.125),  # A
    (64, 4.875, 5.125),  # C
    (67, 4.875, 5.125),  # D
    (60, 5.625, 5.875),  # F
    (62, 5.625, 5.875),  # A
    (64, 5.625, 5.875),  # C
    (67, 5.625, 5.875),  # D
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax - motif: D -> Eb -> F -> D
sax_notes = [
    (62, 4.5, 4.6875),  # D
    (64, 4.6875, 4.875),  # Eb
    (65, 4.875, 5.0625),  # F
    (62, 5.0625, 5.25),  # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Drums - Bar 3 and 4
drum_notes = [
    (36, 3.0, 3.375), (38, 3.375, 3.75), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (42, 4.5, 0.1875),
    
    (36, 4.5, 4.875), (38, 4.875, 5.25), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
