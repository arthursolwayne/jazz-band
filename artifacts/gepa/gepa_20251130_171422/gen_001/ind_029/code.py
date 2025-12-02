
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

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),
    (62, 2.625), (64, 2.875), (63, 3.25), (60, 3.625),
    (62, 3.625), (64, 3.875), (63, 4.25), (60, 4.625),
    (62, 4.625), (64, 4.875), (63, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 1.875), (67, 1.875), (69, 1.875), (71, 1.875), # D7
    # Bar 3 (3.0 - 4.5s)
    (64, 3.375), (67, 3.375), (69, 3.375), (71, 3.375), # D7
    # Bar 4 (4.5 - 6.0s)
    (64, 4.875), (67, 4.875), (69, 4.875), (71, 4.875)  # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Little Ray on drums: continue pattern
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 1.875), (38, 2.25), (42, 2.25),
    (36, 2.625), (38, 2.875), (42, 2.875),
    (36, 3.125), (38, 3.5), (42, 3.5),
    (36, 3.5), (38, 3.875), (42, 3.875),
    (36, 4.25), (38, 4.625), (42, 4.625),
    (36, 4.625), (38, 5.0), (42, 5.0),
    (36, 5.375), (38, 5.75), (42, 5.75)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante on sax: short motif, make it sing
sax_notes = [
    (62, 1.5), (64, 1.75), (66, 2.0), (62, 2.5),  # D - F - A - D
    (64, 2.75), (66, 3.0), (62, 3.5), (64, 3.75),  # F - A - D - F
    (66, 4.0), (62, 4.5), (64, 4.75), (66, 5.0)    # A - D - F - A
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
