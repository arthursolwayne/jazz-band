
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

# Bass line: walking line with chromatic approaches
bass_notes = [
    (42, 1.5), (43, 1.75), (41, 2.0), (40, 2.25),
    (42, 2.5), (43, 2.75), (41, 3.0), (40, 3.25),
    (42, 3.5), (43, 3.75), (41, 4.0), (40, 4.25),
    (42, 4.5), (43, 4.75), (41, 5.0), (40, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.75), (53, 1.75), (57, 1.75), (59, 1.75),  # Gm7
    (50, 2.25), (53, 2.25), (57, 2.25), (59, 2.25),  # Gm7
    (50, 3.0), (53, 3.0), (57, 3.0), (59, 3.0),       # Gm7
    (50, 3.5), (53, 3.5), (57, 3.5), (59, 3.5),       # Gm7
    (50, 4.25), (53, 4.25), (57, 4.25), (59, 4.25),   # Gm7
    (50, 4.75), (53, 4.75), (57, 4.75), (59, 4.75)    # Gm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: short motif, make it sing. Fm (F, Ab, Bb, D)
# Motif: F (53), Ab (50), Bb (52), D (55)
# Start on 1.5s, leave it hanging, come back on bar 3
sax_notes = [
    (53, 1.5), (50, 1.75), (52, 2.0), (55, 2.25),
    (53, 3.0), (50, 3.25), (52, 3.5), (55, 3.75),
    (53, 4.5), (50, 4.75), (52, 5.0), (55, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drum fills in bar 2-4
fill_notes = [
    (38, 2.0), (42, 2.0),
    (38, 3.0), (42, 3.0),
    (38, 4.0), (42, 4.0)
]
for note, time in fill_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
