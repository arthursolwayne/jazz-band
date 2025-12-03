
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (38, 2.25), (40, 2.625),
    (43, 3.0), (41, 3.375), (38, 3.75), (40, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    (62, 1.5), (65, 1.5), (67, 1.5), (71, 1.5),
    # Bar 3: G7 (B, D, G, B)
    (71, 3.0), (74, 3.0), (76, 3.0), (76, 3.0),
    # Bar 4: Cm7 (E, G, C, E)
    (64, 4.5), (67, 4.5), (72, 4.5), (76, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (42, 2.0), (42, 2.125), (42, 2.25), (42, 2.375), (36, 2.625), (38, 3.0),
    (42, 2.625), (42, 2.75), (42, 2.875), (42, 3.0),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875), (36, 4.125), (38, 4.5),
    (42, 4.125), (42, 4.25), (42, 4.375), (42, 4.5)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (72, 1.5), (74, 1.875), (72, 2.25), (70, 2.625),  # Motif
    (72, 3.0), (74, 3.375), (72, 3.75), (70, 4.125)   # Repeat motif
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
