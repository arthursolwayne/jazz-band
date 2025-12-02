
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

# Bass line (Marcus) - walking line, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 2.875), (46, 3.25), (44, 3.625), (43, 4.0),
    (45, 4.375), (46, 4.75), (44, 5.125), (43, 5.5)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (50, 1.875), (53, 1.875), (55, 1.875), (57, 1.875),  # C7
    (52, 3.25), (55, 3.25), (57, 3.25), (59, 3.25),  # D7
    (53, 4.75), (56, 4.75), (58, 4.75), (60, 4.75)   # E7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax (Dante) - short motif, sing it, leave it hanging
sax_notes = [
    (62, 1.5), (64, 1.875), (62, 2.125), (60, 2.5),
    (62, 2.875), (64, 3.25), (62, 3.5), (60, 3.875),
    (62, 4.375), (64, 4.75), (62, 5.0), (60, 5.375)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums continue (Bars 2-4)
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 1.875), (38, 2.25), (42, 2.25),
    (36, 2.625), (38, 2.875), (42, 2.875),
    (36, 3.25), (38, 3.625), (42, 3.625),
    (36, 4.0), (38, 4.375), (42, 4.375),
    (36, 4.75), (38, 5.125), (42, 5.125),
    (36, 5.5), (38, 5.875), (42, 5.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_introduction.mid')
