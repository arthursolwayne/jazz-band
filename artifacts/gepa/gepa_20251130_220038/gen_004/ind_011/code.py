
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

# Bass line (Marcus) - walking line in F
bass_notes = [
    (45, 1.5), (47, 1.875), (44, 2.25), (46, 2.625),
    (48, 2.875), (50, 3.25), (47, 3.625), (49, 4.0),
    (51, 4.25), (53, 4.625), (50, 5.0), (52, 5.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (57, 2.0), (60, 2.0), (64, 2.0), (66, 2.0),  # F7
    # Bar 3
    (59, 3.0), (62, 3.0), (66, 3.0), (69, 3.0),  # Bb7
    # Bar 4
    (60, 4.0), (64, 4.0), (67, 4.0), (69, 4.0)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax (Dante) - short motif, starts on beat 1 of bar 2, leaves it hanging
sax_notes = [
    (62, 1.5), (66, 1.75), (69, 2.0),  # F -> A -> C
    (66, 2.5), (62, 2.75), (69, 3.0),  # A -> F -> C
    (66, 3.5), (69, 3.75), (71, 4.0),  # A -> C -> D
    (69, 4.5), (66, 4.75), (62, 5.0)   # C -> A -> F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    # Bar 3
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
