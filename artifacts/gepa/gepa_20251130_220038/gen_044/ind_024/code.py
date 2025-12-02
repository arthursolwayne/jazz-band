
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
# Bass line: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (61, 2.25), (60, 2.625),
    (62, 3.0), (63, 3.375), (61, 3.75), (60, 4.125),
    (62, 4.5), (63, 4.875), (61, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (72, 2.0), (74, 2.0), (76, 2.0), (77, 2.0),  # D7
    # Bar 3
    (72, 3.5), (74, 3.5), (76, 3.5), (77, 3.5),  # D7
    # Bar 4
    (72, 5.0), (74, 5.0), (76, 5.0), (77, 5.0)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing
# D (62), F# (64), Eb (61), D (62)
sax_notes = [
    (62, 1.5), (64, 1.75), (61, 2.0), (62, 2.25),
    (62, 3.0), (64, 3.25), (61, 3.5), (62, 3.75),
    (62, 4.5), (64, 4.75), (61, 5.0), (62, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
