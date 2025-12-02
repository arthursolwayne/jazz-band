
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

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (53, 1.5), (51, 1.875), (50, 2.25), (52, 2.625),
    (53, 2.875), (51, 3.25), (50, 3.625), (52, 4.0),
    (53, 4.25), (51, 4.625), (50, 5.0), (52, 5.375),
    (53, 5.5), (51, 5.875), (50, 6.25), (52, 6.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (53, 1.5), (51, 1.5), (55, 1.5), (50, 1.5),
    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    (58, 2.875), (56, 2.875), (53, 2.875), (51, 2.875),
    # Bar 4: E7 (E, G#, B, D)
    (59, 4.25), (62, 4.25), (64, 4.25), (58, 4.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (53, 1.5), (55, 1.75), (53, 2.0), (50, 2.25),
    (53, 2.5), (55, 2.75), (53, 3.0), (50, 3.25),
    (53, 3.5), (55, 3.75), (53, 4.0), (50, 4.25),
    (53, 4.5), (55, 4.75), (53, 5.0), (50, 5.25),
    (53, 5.5), (55, 5.75), (53, 6.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
