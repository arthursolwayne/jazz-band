
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (43, 1.5), (42, 1.75), (43, 2.0), (45, 2.25),
    # Bar 3
    (47, 2.5), (46, 2.75), (47, 3.0), (44, 3.25),
    # Bar 4
    (43, 3.5), (42, 3.75), (43, 4.0), (45, 4.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (50, 1.5), (52, 1.5), (55, 1.5), (57, 1.5),
    # Bar 3: G7 (G B D F)
    (55, 2.5), (57, 2.5), (59, 2.5), (61, 2.5),
    # Bar 4: Cm7 (C Eb G Bb)
    (60, 3.5), (62, 3.5), (65, 3.5), (67, 3.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    (62, 1.5), (65, 1.75), (62, 2.0),
    # Bar 3: Leave it hanging
    (65, 2.5),
    # Bar 4: Come back and finish
    (62, 3.5), (65, 3.75), (62, 4.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
